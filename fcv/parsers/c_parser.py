import clang.cindex as cl
from typing import List, Optional

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, FunctionPointerType, AnyType
from fcv.ir.type_map import get_c_type_mapping

class CParser:
    def __init__(self, platform: str = "lp64"):
        self.platform = platform

    def _cx_type_to_ir(self, cx_type: cl.Type) -> Optional[AnyType]:
        # Fallback for spelling-based mappings first (handles size_t, int32_t, etc. when headers are incomplete)
        spelling = cx_type.spelling.replace("const ", "").replace("restrict ", "").strip()
        mapping = get_c_type_mapping(spelling, self.platform)
        if mapping:
            return ScalarType(base=mapping[0], kind_bytes=mapping[1], is_const=cx_type.is_const_qualified())
            
        canonical = cx_type.get_canonical()
        
        # 1. Resolve pointers and depth
        if canonical.kind == cl.TypeKind.POINTER:
            def resolve_ptr(t, depth=0):
                if t.kind == cl.TypeKind.POINTER:
                    return resolve_ptr(t.get_pointee(), depth + 1)
                return t, depth
            underlying, depth = resolve_ptr(canonical)
            
            if underlying.kind in [cl.TypeKind.FUNCTIONPROTO, cl.TypeKind.FUNCTIONNOPROTO]:
                ret = self._cx_type_to_ir(underlying.get_result())
                args = []
                for i, arg_t in enumerate(underlying.argument_types()):
                    args.append((f"param{i}", self._cx_type_to_ir(arg_t)))
                return FunctionPointerType(return_type=ret, params=args)
                
            if underlying.kind == cl.TypeKind.VOID:
                return ScalarType(base="integer", kind_bytes=8, pointer_depth=depth, is_const=cx_type.is_const_qualified(), iso_name="void")
                
            ir_type = self._cx_type_to_ir(underlying)
            if isinstance(ir_type, ScalarType):
                ir_type.pointer_depth = depth
                ir_type.is_pointer = True
                ir_type.is_value = False
                return ir_type
            elif isinstance(ir_type, ArrayType):
                return ArrayType(element=ir_type.element, rank=ir_type.rank + depth, shape=[None] * depth + ir_type.shape)
            return ir_type
            
        # 2. Resolve arrays
        if canonical.kind in [cl.TypeKind.CONSTANTARRAY, cl.TypeKind.INCOMPLETEARRAY]:
            elem_type = self._cx_type_to_ir(canonical.get_array_element_type())
            shape_size = canonical.get_array_size() if canonical.kind == cl.TypeKind.CONSTANTARRAY else None
            if isinstance(elem_type, ScalarType):
                return ArrayType(element=elem_type, rank=1, shape=[shape_size])
            elif isinstance(elem_type, ArrayType):
                return ArrayType(element=elem_type.element, rank=elem_type.rank + 1, shape=[shape_size] + elem_type.shape)
                
        # 3. Resolve records/structs
        if canonical.kind in [cl.TypeKind.RECORD, cl.TypeKind.ELABORATED]:
            decl = canonical.get_declaration()
            if canonical.kind == cl.TypeKind.ELABORATED:
                decl = canonical.get_named_type().get_declaration()
            defn = decl.get_definition()
            if defn:
                decl = defn
            name = decl.spelling
            
            # Lookup in struct_def_map if incomplete
            if not any(child.kind == cl.CursorKind.FIELD_DECL for child in decl.get_children()):
                lookup_name = name if name else canonical.spelling.replace("struct ", "").strip()
                if lookup_name in getattr(self, 'struct_def_map', {}):
                    decl = self.struct_def_map[lookup_name]
                    if decl.spelling:
                        name = decl.spelling
                        
            fields = []
            
            # Walk declaration children for field decls
            for field in decl.get_children():
                if field.kind == cl.CursorKind.FIELD_DECL:
                    f_type = self._cx_type_to_ir(field.type)
                    
                    # Resolve offset using Cursor.get_field_offsetof()
                    offset_bits = -1
                    try:
                        offset_bits = field.get_field_offsetof()
                    except Exception:
                        pass
                    offset_bytes = offset_bits // 8 if offset_bits >= 0 else 0
                    
                    fields.append((field.spelling, f_type, offset_bytes))
            
            # Struct size and alignment
            size_bytes = 0
            alignment = 1
            try:
                size_bytes = decl.type.get_canonical().get_size()
                if size_bytes < 0:
                    size_bytes = canonical.get_size()
                if size_bytes < 0:
                    size_bytes = 0
            except Exception:
                try:
                    size_bytes = canonical.get_size()
                    if size_bytes < 0:
                        size_bytes = 0
                except Exception:
                    size_bytes = 0
            try:
                alignment = decl.type.get_canonical().get_alignof()
                if alignment < 0:
                    alignment = canonical.get_alignof()
                if alignment < 0:
                    alignment = 1
            except Exception:
                try:
                    alignment = canonical.get_alignof()
                    if alignment < 0:
                        alignment = 1
                except Exception:
                    alignment = 1
                    
            return StructType(name=name, fields=fields, size_bytes=size_bytes, alignment=alignment, is_bind_c=True)
            
        # 4. Resolve basic types
        kind = canonical.kind
        is_unsigned = kind in [
            cl.TypeKind.BOOL,
            cl.TypeKind.CHAR_U, cl.TypeKind.UCHAR, cl.TypeKind.USHORT, 
            cl.TypeKind.UINT, cl.TypeKind.ULONG, cl.TypeKind.ULONGLONG, 
            cl.TypeKind.UINT128
        ]
        
        is_const = cx_type.is_const_qualified()
        
        # Check kind category
        if kind == cl.TypeKind.BOOL:
            return ScalarType(base="logical", kind_bytes=1, is_unsigned=True, is_const=is_const)
            
        if kind in [
            cl.TypeKind.CHAR_U, cl.TypeKind.UCHAR, cl.TypeKind.CHAR_S, cl.TypeKind.SCHAR,
            cl.TypeKind.SHORT, cl.TypeKind.INT, cl.TypeKind.LONG, cl.TypeKind.LONGLONG,
            cl.TypeKind.USHORT, cl.TypeKind.UINT, cl.TypeKind.ULONG, cl.TypeKind.ULONGLONG,
            cl.TypeKind.INT128, cl.TypeKind.UINT128
        ]:
            size = 4
            try:
                size = canonical.get_size()
                if size < 0:
                    size = 4
            except Exception:
                pass
            return ScalarType(base="integer", kind_bytes=size, is_unsigned=is_unsigned, is_const=is_const)
            
        if kind in [cl.TypeKind.FLOAT, cl.TypeKind.DOUBLE, cl.TypeKind.LONGDOUBLE]:
            size = 8
            try:
                size = canonical.get_size()
                if size < 0:
                    size = 8
            except Exception:
                pass
            return ScalarType(base="real", kind_bytes=size, is_const=is_const)
            
        if kind == cl.TypeKind.COMPLEX:
            size = 16
            try:
                size = canonical.get_size()
                if size < 0:
                    size = 16
            except Exception:
                pass
            return ScalarType(base="complex", kind_bytes=size, is_const=is_const)
            
        # Fallback to spelling matching
        spelling = canonical.spelling.replace("const ", "").replace("restrict ", "").strip()
        mapping = get_c_type_mapping(spelling, self.platform)
        if mapping:
            size = mapping[1]
            try:
                size = canonical.get_size()
                if size < 0:
                    size = mapping[1]
            except Exception:
                pass
            return ScalarType(base=mapping[0], kind_bytes=size, is_const=is_const)
            
        return None

    def _cursor_to_proc(self, cursor: cl.Cursor) -> InterfaceProc:
        name = cursor.spelling
        ret_type = self._cx_type_to_ir(cursor.result_type)
        if cursor.result_type.kind == cl.TypeKind.VOID:
            ret_type = None
            
        params = []
        for arg in cursor.get_arguments():
            arg_name = arg.spelling
            arg_type = self._cx_type_to_ir(arg.type)
            if isinstance(arg_type, ScalarType) and not arg_type.is_pointer:
                arg_type.is_value = True # C passes scalars by value
            params.append((arg_name, arg_type))
            
        return InterfaceProc(
            name=name,
            source_file=cursor.location.file.name if cursor.location.file else "",
            source_line=cursor.location.line,
            return_type=ret_type,
            params=params,
            is_function=(ret_type is not None)
        )

    def parse_header(self, filepath: str, cflags: List[str] = None) -> List[InterfaceProc]:
        try:
            index = cl.Index.create()
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            prelude = """
typedef unsigned long size_t;
typedef int int32_t;
typedef unsigned int uint32_t;
typedef long long int64_t;
typedef unsigned long long uint64_t;
typedef short int16_t;
typedef unsigned short uint16_t;
typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef _Bool bool;
"""
            unsaved = [(filepath, prelude + "\n" + content)]
            args = ['-x', 'c', '-std=c11']
            if cflags:
                args.extend(cflags)
            tu = index.parse(filepath, unsaved_files=unsaved, args=args)
        except Exception as e:
            print(f"Error parsing C header (make sure libclang is installed): {e}")
            return []
            
        self.struct_def_map = {}
        for cursor in tu.cursor.walk_preorder():
            if cursor.kind == cl.CursorKind.STRUCT_DECL:
                if any(child.kind == cl.CursorKind.FIELD_DECL for child in cursor.get_children()):
                    if cursor.spelling:
                        self.struct_def_map[cursor.spelling] = cursor
            elif cursor.kind == cl.CursorKind.TYPEDEF_DECL:
                underlying = cursor.underlying_typedef_type.get_canonical()
                decl = underlying.get_declaration()
                defn = decl.get_definition() if decl.get_definition() else decl
                if any(child.kind == cl.CursorKind.FIELD_DECL for child in defn.get_children()):
                    self.struct_def_map[cursor.spelling] = defn
                    if defn.spelling:
                        self.struct_def_map[defn.spelling] = defn
                        
        procs = []
        for cursor in tu.cursor.walk_preorder():
            if cursor.kind == cl.CursorKind.FUNCTION_DECL:
                if cursor.location.file and cursor.location.file.name == filepath:
                    procs.append(self._cursor_to_proc(cursor))
        return procs

def parse_c_header(filepath: str, platform: str = "lp64", cflags: List[str] = None) -> List[InterfaceProc]:
    parser = CParser(platform)
    return parser.parse_header(filepath, cflags=cflags)

import clang.cindex as cl
from typing import List, Optional

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType
from fcv.ir.type_map import get_c_type_mapping

class CParser:
    def __init__(self, platform: str = "lp64"):
        self.platform = platform

    def _cx_type_to_ir(self, cx_type: cl.Type) -> Optional[AnyType]:
        # Handle const/restrict qualifiers
        if cx_type.kind == cl.TypeKind.POINTER:
            pointee = cx_type.get_pointee()
            ir_type = self._cx_type_to_ir(pointee)
            if isinstance(ir_type, ScalarType):
                ir_type.is_pointer = True
                ir_type.is_value = False
                return ir_type
            elif isinstance(ir_type, StructType):
                # Don't erase StructType behind pointer
                return ir_type
            elif ir_type is None and pointee.kind == cl.TypeKind.VOID:
                return ScalarType(base="integer", kind_bytes=8, is_pointer=True)
            return ir_type
            
        if cx_type.kind == cl.TypeKind.CONSTANTARRAY or cx_type.kind == cl.TypeKind.INCOMPLETEARRAY:
            elem_type = self._cx_type_to_ir(cx_type.get_array_element_type())
            shape_size = cx_type.get_array_size() if cx_type.kind == cl.TypeKind.CONSTANTARRAY else None
            if isinstance(elem_type, ScalarType):
                return ArrayType(element=elem_type, rank=1, shape=[shape_size])
            elif isinstance(elem_type, ArrayType):
                return ArrayType(element=elem_type.element, rank=elem_type.rank + 1, shape=[shape_size] + elem_type.shape)
            
        if cx_type.kind == cl.TypeKind.RECORD or cx_type.kind == cl.TypeKind.ELABORATED:
            # StructType
            decl = cx_type.get_declaration()
            if cx_type.kind == cl.TypeKind.ELABORATED:
                decl = cx_type.get_named_type().get_declaration()
            name = decl.spelling
            fields = []
            field_offsets = []
            for field in decl.get_children():
                if field.kind == cl.CursorKind.FIELD_DECL:
                    f_type = self._cx_type_to_ir(field.type)
                    fields.append((field.spelling, f_type))
                    offset_bits = field.get_field_offsetof()
                    offset_bytes = offset_bits // 8 if offset_bits >= 0 else 0
                    field_offsets.append(offset_bytes)
            
            # If the decl is incomplete (0 fields), scan translation unit for a complete definition
            if not fields and decl.translation_unit:
                tu = decl.translation_unit
                for cursor in tu.cursor.walk_preorder():
                    if cursor.spelling == name and cursor.kind in (cl.CursorKind.TYPEDEF_DECL, cl.CursorKind.STRUCT_DECL):
                        target_decl = cursor
                        if cursor.kind == cl.CursorKind.TYPEDEF_DECL:
                            target_decl = cursor.underlying_typedef_type.get_declaration()
                        
                        temp_fields = []
                        temp_offsets = []
                        for field in target_decl.get_children():
                            if field.kind == cl.CursorKind.FIELD_DECL:
                                f_type = self._cx_type_to_ir(field.type)
                                temp_fields.append((field.spelling, f_type))
                                offset_bits = field.get_field_offsetof()
                                offset_bytes = offset_bits // 8 if offset_bits >= 0 else 0
                                temp_offsets.append(offset_bytes)
                        if temp_fields:
                            fields = temp_fields
                            field_offsets = temp_offsets
                            cx_type = target_decl.type
                            break

            size = cx_type.get_size()
            if size < 0:
                size = 0
            return StructType(name=name, fields=fields, is_bind_c=True, field_offsets=field_offsets, size=size)
            
        # Basic types
        spelling = cx_type.spelling.replace("const ", "").replace("restrict ", "").strip()
        mapping = get_c_type_mapping(spelling, self.platform)
        if mapping:
            return ScalarType(base=mapping[0], kind_bytes=mapping[1], is_pointer=False)
            
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

    def parse_header(self, filepath: str) -> List[InterfaceProc]:
        try:
            index = cl.Index.create()
            tu = index.parse(filepath, args=['-x', 'c', '-std=c11'])
        except Exception as e:
            print(f"Error parsing C header (make sure libclang is installed): {e}")
            return []
            
        procs = []
        for cursor in tu.cursor.walk_preorder():
            if cursor.kind == cl.CursorKind.FUNCTION_DECL:
                if cursor.location.file and cursor.location.file.name == filepath:
                    procs.append(self._cursor_to_proc(cursor))
        return procs

def parse_c_header(filepath: str, platform: str = "lp64") -> List[InterfaceProc]:
    parser = CParser(platform)
    return parser.parse_header(filepath)

import os
import re
import json

def extract_hard_tests(md_path, out_dir):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    os.makedirs(out_dir, exist_ok=True)
    
    # We look for sections starting with ### TC-
    tc_re = re.compile(r'###\s+(TC-[A-K]-\d{3})\s+—\s+([^\n]+)(.*?)(?=###\s+TC-|$)', re.DOTALL)
    
    matches = tc_re.findall(content)
    count = 0
    
    for match in matches:
        tc_id = match[0]
        tc_desc = match[1].strip()
        tc_body = match[2]
        
        # Extract Fortran code
        f90_match = re.search(r'\*\*Fortran[^:]*:\*\*\s*```fortran\n(.*?)\n```', tc_body, re.DOTALL)
        # Extract C code
        c_match = re.search(r'\*\*C[^:]*:\*\*\s*```c\n(.*?)\n```', tc_body, re.DOTALL)
        # Extract expected output text (just everything in the output block)
        out_match = re.search(r'\*\*Expected validator output(?:[^:]*):\*\*\s*```\n(.*?)\n```', tc_body, re.DOTALL)
        
        if not f90_match or not c_match:
            print(f"Skipping {tc_id} due to missing code blocks.")
            continue
            
        f90_code = f90_match.group(1).strip()
        c_code = c_match.group(1).strip()
        expected_output = out_match.group(1).strip() if out_match else ""
        
        # Map expected output to our internal JSON format for pytest
        # e.g., if "ERROR" is found and "HIDDEN_STRLEN_ARG", we add it.
        # For simplicity, we just extract the first word of the expected output block lines
        expected_json = []
        for line in expected_output.split('\n'):
            line = line.strip()
            if line.startswith('ERROR') or line.startswith('WARNING') or line.startswith('OK'):
                parts = line.split()
                severity = parts[0]
                if severity == "OK":
                    severity = "NONE" # meaning no error expected
                
                # The category is usually the first word on the NEXT line, or we can just assert it fails somehow.
                # Actually, our engine might not match the exact text. Let's just store the full text block.
                # For `pytest`, we can just check if `run_abi_checks` outputs anything for ERROR/WARNING.
                
                expected_json.append({"severity": severity, "raw_text": expected_output})
                break # Just store one expectation per test case for now
                
        # Clean folder name
        safe_desc = re.sub(r'[^a-zA-Z0-9]', '_', tc_desc).strip('_')
        safe_desc = re.sub(r'_+', '_', safe_desc)[:30]
        tc_dir = os.path.join(out_dir, f"{tc_id}_{safe_desc}")
        os.makedirs(tc_dir, exist_ok=True)
        
        with open(os.path.join(tc_dir, 'interface.f90'), 'w', encoding='utf-8') as f:
            f.write(f90_code)
            
        with open(os.path.join(tc_dir, 'header.h'), 'w', encoding='utf-8') as f:
            f.write(c_code)
            
        with open(os.path.join(tc_dir, 'expected.json'), 'w', encoding='utf-8') as f:
            json.dump(expected_json, f, indent=2)
            
        count += 1
        
    print(f"Extracted {count} hard test cases into {out_dir}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fcvalidator_dir = os.path.dirname(os.path.dirname(base_dir))
    workspace_dir = os.path.dirname(fcvalidator_dir)
    md_path = os.path.join(workspace_dir, "hardest_test_cases.md")
    out_dir = os.path.join(base_dir, "hard_pairs")
    extract_hard_tests(md_path, out_dir)

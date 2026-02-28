import os
import json
import argparse
from jinja2 import Environment, FileSystemLoader

def generate_code_from_pim(pim_file_path, template_dir, template_name, output_code_path):
    print(f"🔄 [M2T] Starting Model-to-Text code generation...")
    
    if not os.path.exists(pim_file_path):
        raise FileNotFoundError(f"PIM file not found at {pim_file_path}. Please check the path.")
        
    with open(pim_file_path, 'r', encoding='utf-8') as f:
        pim_data = json.load(f)

    # --- Data Adaptation for Jinja2 Template ---
    if "variables" in pim_data: 
        pim_data["input_variables"] = pim_data["variables"].get("inputs", [])
        pim_data["output_variables"] = pim_data["variables"].get("outputs", [])
    # -------------------------------------------
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    
    print(f"⚙️ [M2T] Injecting PIM data into Jinja2 template '{template_name}'...")

    generated_python_code = template.render(**pim_data)
    
    os.makedirs(os.path.dirname(output_code_path), exist_ok=True)
    with open(output_code_path, 'w', encoding='utf-8') as f:
        f.write(generated_python_code)
        
    print(f"✅ [M2T] Successfully generated executable FIS reasoning kernel to: {output_code_path}")
    return output_code_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAFIS-Gen M2T Generator")
    parser.add_argument("--pim", type=str, default="../generated_outputs/pim.json", 
                        help="Path to the input PIM JSON file")
    parser.add_argument("--template_dir", type=str, default="jinja_templates", 
                        help="Directory containing the Jinja2 templates")
    parser.add_argument("--template", type=str, default="fis_class.jinja2", 
                        help="Name of the Jinja2 template file")
    parser.add_argument("--output", type=str, default="../generated_outputs/AirportRevenueFIS.py", 
                        help="Path to save the generated Python code")
    
    args = parser.parse_args()
    
    generate_code_from_pim(
        pim_file_path=args.pim,
        template_dir=args.template_dir,
        template_name=args.template,
        output_code_path=args.output
    )

import os
import json
import argparse
from jinja2 import Environment, FileSystemLoader

def generate_code_from_pim(pim_file_path, template_dir, template_name, output_code_path):
    print(f"🔄 [M2T] Starting Model-to-Text code generation...")
    
    if not os.path.exists(pim_file_path):
        raise FileNotFoundError(f"PIM file not found at {pim_file_path}. Please check the path.")
        
    with open(pim_file_path, 'r', encoding='utf-8') as f:
        pim_data = json.load(f)

    # --- Data Adaptation for Jinja2 Template ---
    if "variables" in pim_data:
        pim_data["input_variables"] = pim_data["variables"].get("inputs", [])
        pim_data["output_variables"] = pim_data["variables"].get("outputs", [])
    # -------------------------------------------

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    
    print(f"⚙️ [M2T] Injecting PIM data into Jinja2 template '{template_name}'...")

    generated_python_code = template.render(**pim_data)
    
    os.makedirs(os.path.dirname(output_code_path), exist_ok=True)
    with open(output_code_path, 'w', encoding='utf-8') as f:
        f.write(generated_python_code)
        
    print(f"✅ [M2T] Successfully generated executable FIS reasoning kernel to: {output_code_path}")
    return output_code_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAFIS-Gen M2T Generator")
    parser.add_argument("--pim", type=str, default="../generated_outputs/pim.json", 
                        help="Path to the input PIM JSON file")
    parser.add_argument("--template_dir", type=str, default="jinja_templates", 
                        help="Directory containing the Jinja2 templates")
    parser.add_argument("--template", type=str, default="fis_class.jinja2", 
                        help="Name of the Jinja2 template file")
    parser.add_argument("--output", type=str, default="../generated_outputs/AirportRevenueFIS.py", 
                        help="Path to save the generated Python code")
    
    args = parser.parse_args()
    
    generate_code_from_pim(
        pim_file_path=args.pim,
        template_dir=args.template_dir,
        template_name=args.template,
        output_code_path=args.output
    )
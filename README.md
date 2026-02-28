<!--
 * @Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @Date: 2026-02-28 03:54:55
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2026-02-28 03:55:11
 * @FilePath: /python_test/MAFIS-Gen/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

# MAFIS-Gen: Model-Driven Automated Fuzzy Inference System Generator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![MDE M2T](https://img.shields.io/badge/MDE-Model_to_Text-orange.svg)]()

> **A Replication Package for the paper:** _(Insert Your Paper Title Here)_

## 📖 Overview

MAFIS-Gen is an end-to-end Automated Model-Driven Engineering (MDE) framework designed to transform natural language domain expertise into a fully executable, White-box Fuzzy Inference System (FIS).

Instead of manually coding complex fuzzy logic rules and membership functions, this pipeline utilizes a Large Language Model (LLM) guided by strict formal metamodels (M2) to parse domain logic, and a Jinja2-based Model-to-Text (M2T) engine to dynamically generate the executable reasoning kernel.

## 📂 Repository Structure

The architecture of this repository mirrors the MDE pipeline described in the paper:

- **`inputs/`**: Contains raw natural language descriptions from domain experts.
- **`metamodels/`**: Defines the formal M2-level constraint (`fis_schema.json`) that strictly regulates the Platform-Independent Model (PIM).
- **`pipeline/`**: The core MDE transformation engine.
    - `m2m_transformer.py`: Model-to-Model transformation (Natural Language -> PIM JSON).
    - `m2t_generator.py`: Model-to-Text code generation (PIM JSON -> Python Kernel).
    - `jinja_templates/`: Contains the master template for generating the mathematical white-box engine.
- **`generated_outputs/`**: The destination for the auto-generated code (e.g., `AirportRevenueFIS.py`).
- **`experiments/`**: Scripts to verify the mathematical precision and interpretability of the generated code (Replicating paper figures).

## 🚀 Getting Started

### 1. Environment Setup

Ensure you have Python 3.8+ installed. Install the required dependencies using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

2. Run the End-to-End Pipeline
   Step 1: Generate the Platform-Independent Model (PIM)
   This script parses the expert's text and formalizes it into a JSON structure guided by the metamodel.

Bash
cd pipeline
python m2m_transformer.py
(Success Output: ✅ [M2M] Successfully generated PIM model...)

Step 2: Generate the Executable FIS Code (M2T)
This script injects the PIM into the Jinja2 template to dynamically compile the Python reasoning kernel.

Bash
python m2t_generator.py
(Success Output: ✅ [M2T] Successfully generated executable FIS reasoning kernel...)

3. Verify White-Box Execution (Experiment Replication)
   Once the code is generated in the generated_outputs/ folder, run the verification script to test the white-box rule activations (e.g., Scenario E from the paper):

Bash
cd ../experiments
python verify_execution.py
Expected Console Output:
The system will output the crisp predicted value (e.g., $77.38) and print the exact activation weight of every internal rule. You will observe precise mathematical behavior, such as R9 taking the dominant weight (0.5000) and the Gaussian tail characteristics for partial activations.

🧠 Core Scientific Contributions Demonstrated
Metamodel-Guided Parsing: The fis_schema.json guarantees that LLM outputs are syntactically and semantically flawless for fuzzy logic operations.

Automated M2T Translation: The Jinja2 engine bridges the gap between static JSON constraints and a dynamic skfuzzy Python implementation.

White-Box Interpretability: The generated code automatically includes a get_rule_activations() method, exposing internal reasoning weights without manual coding.

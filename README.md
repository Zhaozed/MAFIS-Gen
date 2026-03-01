MAFIS-Gen: An LLM-Assisted Model-Driven Framework for Fuzzy Inference System Generation
📖 Project Introduction

MAFIS-Gen (Model-driven Automated Fuzzy Inference System Generator) is a research framework designed to bridge the gap between human domain expertise and executable Explainable AI (XAI).

Traditional Fuzzy Inference System (FIS) development requires both deep domain knowledge and manual programming. MAFIS-Gen automates this by:

Parsing natural language requirements into formal Platform-Independent Models (PIM) using LLMs

Generating ready-to-use Python code (based on scikit-fuzzy) via Jinja2 templates

Ensuring behavioral fidelity through automated validation scripts

🚀 Key Features

Zero-Coding Pipeline: Automatically generates a complete Python FIS class from a JSON configuration

Behavioral Fidelity: Preserves 100% of the expert's logical intent through formal M2M/M2T transformations

White-box Interpretability: Every decision made by the generated system is traceable back to the expert's rules

High Efficiency: Reduces development time from days to minutes by decoupling domain logic from implementation

📂 Repository Structure
MAFIS-Gen/
├── pipeline/                # Core transformation engines
│   ├── m2m_transformer.py   # NL to PIM (LLM-based)
│   ├── m2t_generator.py     # PIM to Python (Jinja2-based)
│   └── jinja_templates/     # Code generation templates (fis_class.jinja2)
├── metaModels/              # System constraints & schemas (fis_schema.json)
├── inputs/                  # Domain-specific scenarios in natural language
├── experiments/             # Evaluation scripts & visualization results
│   ├── run_section_4_2_4.py # Framework capability test
│   ├── run_section_4_3.py   # Extensibility analysis (Extended Model)
│   ├── run_section_4_4.py   # Behavioral fidelity analysis
│   └── *.png                # Generated experimental figures (4.7 - 4.10)
├── generated_outputs/       # Storage for intermediate PIMs and generated Python classes
└── requirements.txt         # Project dependencies
⚙️ Installation & Usage
1. Requirements

Ensure you have Python 3.8+ installed.

pip install -r requirements.txt
⚙️ Core Usage: Generating the FIS Code

Before running any experiments, generate the Python execution code from the JSON configuration (PIM).
The framework uses a Jinja2 template engine to achieve this with zero manual coding.

Command:

python3 pipeline/m2t_generator.py \
  --pim generated_outputs/pim.json \
  --output generated_outputs/AirportRevenueFIS.py
🧪 Experiment 1: Framework Capability (Section 4.2.4)

Validates the basic functionality of the generated system to ensure it correctly parses the 2-input, 9-rule Mamdani inference logic.

Run:

python3 experiments/run_section_4_2_4.py
🧪 Experiment 2: Extensibility Analysis (Section 4.3)

Demonstrates the framework's flexibility by introducing a new input variable (Travel_Purpose) without altering the underlying code generation engine.

Step A — Generate the extended system
python3 pipeline/m2t_generator.py \
  --pim generated_outputs/airport_revenue_extended.json \
  --output generated_outputs/AirportRevenueFIS_Extended.py
Step B — Run the evaluation
python3 experiments/run_section_4_3.py
🧪 Experiment 3: Behavioral Fidelity Analysis (Section 4.4)

Proves that the generated code strictly adheres to the semantic relationships and logical intent encoded by the domain expert.
This script automatically generates the evaluation figures.

Run:

python3 experiments/run_section_4_4.py
📊 Visualized Results from Section 4.4
Rule Activation Analysis (Figure 4.10)

This heatmap demonstrates the precise firing strength of each fuzzy rule across five distinct test scenarios, proving white-box mathematical traceability.

Sensitivity Analysis (Figure 4.9)

Validates the monotonic relationship between input variables (Satisfaction) and the output (Consumption) at different Waiting Time levels, reflecting the interaction effects embedded in the expert knowledge.

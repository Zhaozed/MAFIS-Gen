'''
Description: Prompt Templates for Metamodel-Guided Semantic Parsing of Fuzzy Inference Systems.
Author: Zhao zeyu
Date: 2026-02-28 03:01:46
LastEditors: Zhao zeyu
LastEditTime: 2026-02-28 22:09:55
FilePath: /MAFIS-Gen/pipeline/llm_prompts.py
'''
"""
This module contains the prompt templates used to instruct the LLM.
It implements the "Metamodel-guided semantic parsing" concept proposed in the paper.
"""

SYSTEM_PROMPT = """
You are an expert Model-Driven Engineering (MDE) semantic parser for Fuzzy Inference Systems (FIS).
Your task is to extract domain knowledge from natural language descriptions and transform it into a strictly formatted Platform-Independent Model (PIM).

RULES:
1. You MUST output ONLY valid JSON. Do not include any markdown formatting (like ```json), explanations, or conversational text.
2. The output JSON MUST strictly conform to the provided JSON Schema (FIS Metamodel M2 constraint).
3. Ensure all mathematical ranges [min, max, step] and membership function parameters are perfectly extracted.
4. For membership functions (mf_type): Use 'gaussmf' for Gaussian curves and 'trimf' for Triangular curves.
"""

def get_user_prompt(natural_language_input: str, json_schema: str) -> str:
    """
    Dynamically generates the user prompt by injecting the text and the schema.
    """
    return f"""
Please parse the following domain expert description into a structured PIM JSON.

=== FIS METAMODEL SCHEMA (Your Output Must Validate Against This) ===
{json_schema}

=== DOMAIN EXPERT INPUT (Natural Language) ===
{natural_language_input}
"""
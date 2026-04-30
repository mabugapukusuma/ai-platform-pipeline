import json
from utils.llm import call_llm

def repair_schema(bad_schema: str, error: str):
    prompt = f"""
    The following JSON schema is invalid:

    {bad_schema}

    Error:
    {error}

    Fix ONLY the issues and return valid JSON.
    Do not change correct parts.
    Return ONLY JSON.
    """

    fixed = call_llm(prompt)

    return fixed
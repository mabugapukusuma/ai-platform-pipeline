from utils.llm import call_llm

def design_system(intent_json: str):
    prompt = f"""
    Convert this into system design:

    {intent_json}

    Return ONLY JSON:
    {{
      "entities": [],
      "roles": [],
      "flows": []
    }}
    """
    return call_llm(prompt)
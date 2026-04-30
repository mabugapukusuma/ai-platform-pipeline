from utils.llm import call_llm

def generate_schema(design_json: str):
    prompt = f"""
    Generate a COMPLETE system schema from the following design:

    {design_json}

    STRICT RULES:
    - Return ONLY valid JSON
    - Do NOT include explanations
    - Include ALL required keys
    - Keep structure consistent

    Required format:
    {{
      "ui": {{
        "pages": [],
        "components": []
      }},
      "api": {{
        "endpoints": []
      }},
      "database": {{
        "tables": []
      }},
      "auth": {{
        "roles": [],
        "permissions": []
      }}
    }}
    """

    return call_llm(prompt)
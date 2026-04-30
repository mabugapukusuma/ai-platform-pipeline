from utils.llm import call_llm

def extract_intent(user_input: str):
    prompt = f"""
    Extract structured intent from:
    {user_input}

    Return ONLY JSON:
    {{
      "app_type": "",
      "features": []
    }}
    """
    return call_llm(prompt)
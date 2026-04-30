from pipeline.intent import extract_intent
from pipeline.design import design_system
from pipeline.schema import generate_schema
from pipeline.validate import validate_schema
from pipeline.repair import repair_schema
import json


def safe_parse(data):
    """Convert string JSON to dict safely"""
    if isinstance(data, str):
        try:
            return json.loads(data)
        except Exception:
            return {"ERROR": "Invalid JSON format", "raw_output": data}
    return data


def run_pipeline(user_input):
    try:
        # 🔹 Step 1: Intent
        intent = extract_intent(user_input)
        intent = safe_parse(intent)

        # 🔹 Step 2: Design
        design = design_system(intent)
        design = safe_parse(design)

        # 🔹 Step 3: Schema
        schema = generate_schema(design)
        schema = safe_parse(schema)

        # 🔹 Step 4: Validation
        valid, result = validate_schema(schema)

        # 🔹 Step 5: Repair (if needed)
        if not valid:
            schema = repair_schema(schema, result)
            schema = safe_parse(schema)
            valid, result = validate_schema(schema)

        # 🔹 Final safety check
        if schema is None:
            return {"ERROR": "Pipeline returned None"}

        return schema

    except Exception as e:
        return {
            "ERROR": {
                "message": str(e)
            }
        }


if __name__ == "__main__":
    user_input = input("Enter your app idea: ")
    output = run_pipeline(user_input)
    print(json.dumps(output, indent=2))
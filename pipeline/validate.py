import json
from models.schema_models import AppSchema

def validate_schema(schema_str: str):
    try:
        data = json.loads(schema_str)
        AppSchema(**data)
        return True, data
    except Exception as e:
        return False, str(e)
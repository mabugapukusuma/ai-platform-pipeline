from pydantic import BaseModel
from typing import List, Dict, Any

# UI Schema
class UISchema(BaseModel):
    pages: List[Any]
    components: List[Any]

# API Schema
class APISchema(BaseModel):
    endpoints: List[Any]

# Database Schema
class DatabaseSchema(BaseModel):
    tables: List[Any]

# Auth Schema
class AuthSchema(BaseModel):
    roles: List[Any]
    permissions: List[Any]

# Full App Schema
class AppSchema(BaseModel):
    ui: UISchema
    api: APISchema
    database: DatabaseSchema
    auth: AuthSchema
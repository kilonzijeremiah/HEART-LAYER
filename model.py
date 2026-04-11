from pydantic import BaseModel
from typing import Dict, Any

class ExecuteRequest(BaseModel):
    project_id: str
    task_type: str
    payload: Dict[str, Any]
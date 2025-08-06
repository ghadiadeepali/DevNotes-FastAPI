from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CreateWorkspace(BaseModel):
    name: str
    description: str
    
    
class Workspace(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    # class Config:
    #     orm_mode = True  # So you can return SQLAlchemy instances directly


class WorkspaceResponse(BaseModel):
    msg: str
    status_code: int
    object: Workspace
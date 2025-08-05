from backend.core.db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from backend.models.workspaces import Workspace

router = APIRouter(prefix="/workspaces")

@router.get("/all")
def list_all_workspaces(db: Session = Depends(get_db)):
    workspaces = db.query(Workspace).all()
    return workspaces
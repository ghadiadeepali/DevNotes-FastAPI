from backend.core.db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, status
from backend.models.workspaces import Workspace
from backend.schemas import workspace_schemas

router = APIRouter(prefix="/workspaces")

@router.get("/all")
def list_all_workspaces(db: Session = Depends(get_db)):
    workspaces = db.query(Workspace).all()
    return workspaces

@router.post("/create")
def create_workspace(workspace: workspace_schemas.CreateWorkspace, db: Session = Depends(get_db)):
    new_workspace = Workspace (name=workspace.name, description=workspace.description)
    db.add(new_workspace)
    db.commit()
    db.refresh(new_workspace)
    return {
        "msg": "Workspace created successfully",
        "status_code": status.HTTP_201_CREATED,
        "object": new_workspace  # Pydantic will handle SQLAlchemy object if orm_mode=True
    }
    
    
@router.put("/update/{id}")
def update_workspace(id: int, workspace: workspace_schemas.CreateWorkspace, db: Session = Depends(get_db)):
    workspace_object = db.query(Workspace).filter(Workspace.id==id).first()
    workspace_object.name=workspace.name
    workspace_object.description=workspace.description
    db.commit()
    db.refresh(workspace_object)
    return {
        "msg": "Workspace created successfully",
        "status_code": status.HTTP_200_OK,
        "object": workspace_object  # Pydantic will handle SQLAlchemy object if orm_mode=True
    }
    
    
@router.delete("/delete/{id}")
def delete_a_workspace(id:int, db:Session = Depends(get_db)):
    workspace_object = db.query(Workspace).filter(Workspace.id==id).first()
    db.delete(workspace_object)
    db.commit()
    
    return {"msg": "Workspace deleted Successfully"}
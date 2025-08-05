from fastapi import FastAPI, APIRouter
from backend.services import workspaces

app = FastAPI()

app.include_router(workspaces.router)


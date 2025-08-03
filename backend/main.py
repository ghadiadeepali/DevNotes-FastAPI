from fastapi import FastAPI
from backend.core.db import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

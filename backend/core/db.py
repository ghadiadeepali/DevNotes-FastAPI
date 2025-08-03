from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Base = declarative_base()

def init_db():
    from backend.models import user  # Import all models here to ensure table creation
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created.")

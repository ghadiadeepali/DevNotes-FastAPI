from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)

# Base is the foundation for creating all your ORM models. We inherit this in our models
Base = declarative_base()


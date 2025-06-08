import os
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlmodel import create_engine, SQLModel
DATABASE_URL = "postgresql+psycopg2://postgres:example@localhost:1234/postgres"

engine = create_engine(
    DATABASE_URL,
    pool_size=int(os.getenv("DATABASE_POOL_SIZE", 10))
)

def create_db_and_tables():
    """
    Create the database and tables if they do not exist.
    """
    SQLModel.metadata.create_all(engine)

def check_availability() -> bool:
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print (e)
        return False
from sqlalchemy import create_engine
"""
Creates a configured "Session" class bound to the provided engine.
Parameters:
    autocommit (bool): If True, each operation is committed automatically. Default is False.
    autoflush (bool): If True, the Session will automatically flush pending changes to the database. Default is False.
    bind (Engine or Connection): A SQLAlchemy Engine or Connection instance to which the session is bound.
Returns:
    sessionmaker: A configured session class.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

print("Connecting to PostgreSQL database...", psycopg2)
# PostgreSQL connection URL format: postgresql://user:password@host:port/dbname
DATABASE_URL = "postgresql://username:password@localhost:5432/kanban_db"

# Create the engine
engine = create_engine(DATABASE_URL)

# Define session and base
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

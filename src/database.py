from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from src.config import DATABASE_URL, logger

def get_db_engine() -> Engine:
    """
    Creates and returns a SQLAlchemy engine for PostgreSQL database operations.
    """
    engine = create_engine(
        DATABASE_URL,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True
    )
    return engine

def check_connection() -> bool:
    """
    Validates database connectivity. Returns True if connected, False otherwise.
    """
    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1")).scalar()
            return result == 1
    except Exception as e:
        logger.warning(f"Database connection attempt failed: {e}")
        return False

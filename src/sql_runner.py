from pathlib import Path
from sqlalchemy import text
from src.config import SQL_DIR, logger
from src.database import get_db_engine

def run_sql_script(script_path: Path) -> None:
    """
    Executes a single SQL script file against the PostgreSQL database.
    """
    if not script_path.exists():
        raise FileNotFoundError(f"SQL script not found at: {script_path}")

    logger.info(f"Executing SQL script: {script_path.name}")
    
    with script_path.open("r", encoding="utf-8") as f:
        sql_content = f.read()

    engine = get_db_engine()
    with engine.begin() as conn:
        conn.execute(text(sql_content))
    
    logger.info(f"Successfully executed: {script_path.name}")

def execute_all_sql_scripts() -> None:
    """
    Executes all SQL scripts in the sql/ directory in numerical order.
    """
    if not SQL_DIR.exists():
        raise FileNotFoundError(f"SQL directory not found at: {SQL_DIR}")

    sql_files = sorted(list(SQL_DIR.glob("*.sql")))
    logger.info(f"Found {len(sql_files)} SQL script files to execute.")

    for sql_file in sql_files:
        run_sql_script(sql_file)

if __name__ == "__main__":
    execute_all_sql_scripts()

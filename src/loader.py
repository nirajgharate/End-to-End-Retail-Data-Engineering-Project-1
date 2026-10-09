import pandas as pd
from pathlib import Path
from src.config import PROCESSED_CSV_FILE, DB_SCHEMA, logger
from src.database import get_db_engine

def load_staging_table(input_path: Path = None, table_name: str = "sales_raw", schema: str = DB_SCHEMA) -> int:
    """
    Loads processed dataset from CSV into PostgreSQL staging table.
    """
    input_file = input_path or PROCESSED_CSV_FILE

    logger.info(f"Loading processed dataset into staging table '{schema}.{table_name}'...")

    if not input_file.exists():
        raise FileNotFoundError(f"Processed CSV file not found at: {input_file}")

    # Read processed CSV file
    df = pd.read_csv(input_file)
    record_count = len(df)

    engine = get_db_engine()

    # Load dataframe into database staging table
    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema,
        if_exists="replace",
        index=False,
        chunksize=10000
    )

    logger.info(f"Successfully loaded {record_count:,} records into '{schema}.{table_name}'.")
    return record_count

if __name__ == "__main__":
    load_staging_table()

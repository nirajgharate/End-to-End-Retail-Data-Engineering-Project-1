import pandas as pd
from pathlib import Path
from src.config import RAW_CSV_FILE, PROCESSED_CSV_FILE, logger

def transform_retail_data(input_path: Path = None, output_path: Path = None) -> pd.DataFrame:
    """
    Cleans and standardizes raw retail transaction dataset for warehouse staging.
    
    Operations:
    1. Standardize column headers (lowercase, stripped, snake_case).
    2. Remove records with missing customer identifiers.
    3. Filter out cancelled transactions (quantity <= 0).
    4. Remove invalid unit prices (unitprice <= 0).
    5. Standardize invoice timestamp parsing.
    6. Derive computed metric: revenue (quantity * unitprice).
    """
    input_file = input_path or RAW_CSV_FILE
    output_file = output_path or PROCESSED_CSV_FILE

    logger.info(f"Starting data transformation on: {input_file}")
    
    if not input_file.exists():
        raise FileNotFoundError(f"Raw CSV file not found at: {input_file}")

    # Read raw dataset
    df = pd.read_csv(input_file)
    logger.info(f"Loaded raw dataset with shape: {df.shape[0]:,} rows x {df.shape[1]} columns")

    # Standardize column headers
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Data Quality & Business Logic Cleaning Rules
    # 1. Drop records lacking customer identifier
    df = df.dropna(subset=["customerid"])

    # 2. Keep valid completed sales (positive quantity and unit price)
    df = df[(df["quantity"] > 0) & (df["unitprice"] > 0)]

    # 3. Parse invoice timestamp
    df["invoicedate"] = pd.to_datetime(df["invoicedate"])

    # 4. Compute line-item revenue metric
    df["revenue"] = (df["quantity"] * df["unitprice"]).round(2)

    logger.info(f"Cleaned dataset shape: {df.shape[0]:,} rows x {df.shape[1]} columns")

    # Write processed data to Data Lake processed tier
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    logger.info(f"Processed dataset saved to: {output_file}")

    return df

if __name__ == "__main__":
    transform_retail_data()

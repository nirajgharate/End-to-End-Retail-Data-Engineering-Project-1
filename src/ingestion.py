import pandas as pd
from pathlib import Path
from src.config import RAW_EXCEL_FILE, RAW_CSV_FILE, RAW_DATA_DIR, logger

def ingest_raw_excel(input_path: Path = None, output_path: Path = None) -> Path:
    """
    Ingests the raw Online Retail Excel dataset and converts it to a raw CSV format
    in the Data Lake raw tier.
    """
    input_file = input_path or RAW_EXCEL_FILE
    output_file = output_path or RAW_CSV_FILE

    logger.info(f"Starting raw data ingestion from: {input_file}")
    
    if not input_file.exists():
        if output_file.exists():
            logger.info(f"Excel source file missing, but raw CSV already exists at: {output_file}")
            return output_file
        raise FileNotFoundError(f"Source file not found at: {input_file}")

    # Ensure target output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Read Excel dataset
    df = pd.read_excel(input_file)
    logger.info(f"Successfully loaded {len(df):,} records from Excel.")

    # Save to raw CSV tier
    df.to_csv(output_file, index=False)
    logger.info(f"Raw CSV successfully written to: {output_file}")

    return output_file

if __name__ == "__main__":
    ingest_raw_excel()

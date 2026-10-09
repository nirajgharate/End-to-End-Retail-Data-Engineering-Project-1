import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Base Directory: root of the repository
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env if present
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

# Data Lake Directory Paths
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# File Paths
RAW_EXCEL_FILE = RAW_DATA_DIR / "Online Retail.xlsx"
RAW_CSV_FILE = RAW_DATA_DIR / "retail_raw.csv"
PROCESSED_CSV_FILE = PROCESSED_DATA_DIR / "retail_clean.csv"

# SQL Directory
SQL_DIR = BASE_DIR / "sql"

# Database Configuration
DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_DATABASE = os.getenv("DB_DATABASE", "retail_dw")
DB_SCHEMA = os.getenv("DB_SCHEMA", "retail")

# Construct SQLAlchemy database connection URI
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# Logging Setup
def setup_logging(level=logging.INFO):
    """Configures project-wide logging standard format."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger("RetailDataPipeline")

logger = setup_logging()

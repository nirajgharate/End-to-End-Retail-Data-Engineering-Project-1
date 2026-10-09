# Modern Enterprise Retail Data Platform & Analytics Engineering Pipeline

A modular, production-ready Data Engineering and Analytics pipeline designed to process raw transactional data, curate a multi-tiered Data Lake, populate a **Kimball Dimensional Data Warehouse** in PostgreSQL, and expose curated reporting views for **Power BI**.

---

## Key Highlights & Architecture

The solution follows a modern **Medallion Data Lakehouse Architecture** coupled with a traditional relational Star Schema warehouse layer.

```
[ Raw Excel / CSV ] ──> Data Lake (Raw Tier)
                             │
                             ▼
                    Python ETL Pipeline (Pandas / Cleaning)
                             │
                             ▼
                    Data Lake (Processed Tier)
                             │
                             ▼
                    PostgreSQL Staging (`retail.sales_raw`)
                             │
                             ▼
                    Kimball Star Schema Warehouse DDL/ELT
                    ├── dim_customer
                    ├── dim_product
                    ├── dim_country
                    └── dim_date
                    └── fact_sales
                             │
                             ▼
                    Reporting Layer (`retail.vw_sales_analytics`)
                             │
                             ▼
                    Power BI Interactive Dashboard
```

---

## Repository Structure

```
End-to-End-Retail-Data-Engineering-Project-1/
├── data/
│   ├── raw/                  # Raw landed transaction files (Online Retail.xlsx, retail_raw.csv)
│   └── processed/            # Standardized & cleaned datasets (retail_clean.csv)
├── src/                      # Core Python ETL Package
│   ├── __init__.py
│   ├── config.py             # Dynamic path resolution & environment configurations
│   ├── ingestion.py          # Data Lake ingestion module
│   ├── transformation.py     # Schema standardization & metric calculation
│   ├── database.py           # SQLAlchemy database connection pool manager
│   ├── loader.py             # Database staging batch loader
│   └── sql_runner.py         # Automated SQL DDL/ELT executor
├── sql/                      # Modular DDL, Dimensional Modeling & Analytics SQL
│   ├── 01_schema.sql         # Target schema creation
│   ├── 02_staging.sql        # Staging table definition
│   ├── 03_dimensions.sql     # Kimball dimension tables (customer, product, country, date)
│   ├── 04_facts.sql          # Sales Fact Table definition & foreign key constraints
│   ├── 05_load_dimensions.sql# ELT scripts populating dimension tables
│   ├── 06_load_facts.sql     # ELT scripts populating sales fact table
│   ├── 07_indexes.sql        # B-tree performance indexing on foreign & business keys
│   ├── 08_analytics_views.sql# Curated reporting view for BI consumption
│   └── 09_data_quality_checks.sql # Automated data quality & referential integrity audits
├── dashboards/               # Power BI project file (Retail_Dashboard_Visualization.pbix)
├── main.py                   # Unified CLI pipeline orchestrator
├── requirements.txt          # Python dependencies specification
├── .env.example              # Database credentials template
└── .gitignore                # Production git rules
```

---

## Data Warehouse Star Schema Design

The dimensional warehouse adopts the **Kimball methodology**:

### Fact Table: `fact_sales`
- **Primary Key**: `sales_key` (SERIAL)
- **Degenerate Dimension**: `invoice_no`
- **Foreign Keys**: `customer_key`, `product_key`, `country_key`, `date_key`
- **Measures**: `quantity`, `unit_price`, `revenue`

### Dimension Tables:
1. `dim_customer`: Customer ID uniqueness and surrogate key mapping.
2. `dim_product`: Stock code granularity and product metadata descriptions.
3. `dim_country`: Geographic dimensions for global revenue breakdown.
4. `dim_date`: Time-intelligence grain (Invoice Date, Year, Month, Day).

---

## Quick Start & Execution Guide

### 1. Prerequisites & Environment Setup

Clone or place the codebase in your workspace, navigate to the root folder, and set up a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your PostgreSQL credentials:

```ini
DB_USERNAME=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=retail_dw
DB_SCHEMA=retail
```

---

### 2. Running the Pipeline

You can orchestrate the entire end-to-end pipeline with a single command:

```bash
python main.py run-all
```

Or execute individual pipeline stages modularly:

```bash
# Verify database connectivity
python main.py check-db

# Stage 1: Ingest raw Excel file to raw CSV
python main.py ingest

# Stage 2: Perform data cleaning, normalization, and metric generation
python main.py transform

# Stage 3: Load cleaned data into PostgreSQL staging
python main.py load

# Stage 4: Run SQL scripts for Star Schema DDL, ELT loading, and Reporting Views
python main.py sql
```

---

## Data Quality Controls

Data integrity is guaranteed via automated assertions in `sql/09_data_quality_checks.sql`:
- **Referential Integrity**: Verifies zero orphaned foreign keys in `fact_sales`.
- **Primary Key & Business Key Uniqueness**: Enforces unique customer keys, country keys, and date keys.
- **Financial Reconciliation**: Validates that staging revenue totals match fact table revenue metrics exactly.

---

## Analytics & Power BI Integration

Power BI dashboard connections interface strictly through `retail.vw_sales_analytics`. This decoupled abstraction layer prevents direct querying of underlying warehouse tables, maintaining performance governance and security controls.

-- =============================================================================
-- 03_dimensions.sql
-- Description: Dimensional tables (Kimball Star Schema)
-- =============================================================================

-- Customer Dimension
CREATE TABLE IF NOT EXISTS retail.dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id INTEGER UNIQUE NOT NULL
);

-- Product Dimension
CREATE TABLE IF NOT EXISTS retail.dim_product (
    product_key SERIAL PRIMARY KEY,
    stockcode VARCHAR(50) NOT NULL,
    description TEXT
);

-- Country / Geographic Dimension
CREATE TABLE IF NOT EXISTS retail.dim_country (
    country_key SERIAL PRIMARY KEY,
    country VARCHAR(100) UNIQUE NOT NULL
);

-- Date Dimension
CREATE TABLE IF NOT EXISTS retail.dim_date (
    date_key SERIAL PRIMARY KEY,
    invoice_date DATE UNIQUE NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
);

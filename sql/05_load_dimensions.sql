-- =============================================================================
-- 05_load_dimensions.sql
-- Description: Population scripts for Kimball Dimension tables
-- =============================================================================

-- Populate Customer Dimension
INSERT INTO retail.dim_customer (customer_id)
SELECT DISTINCT CAST(customerid AS INTEGER)
FROM retail.sales_raw
WHERE customerid IS NOT NULL
ON CONFLICT (customer_id) DO NOTHING;

-- Populate Product Dimension
INSERT INTO retail.dim_product (stockcode, description)
SELECT
    stockcode,
    MIN(description) AS description
FROM retail.sales_raw
WHERE stockcode IS NOT NULL
GROUP BY stockcode;

-- Populate Country Dimension
INSERT INTO retail.dim_country (country)
SELECT DISTINCT country
FROM retail.sales_raw
WHERE country IS NOT NULL
ON CONFLICT (country) DO NOTHING;

-- Populate Date Dimension
INSERT INTO retail.dim_date (invoice_date, year, month, day)
SELECT DISTINCT
    DATE(invoicedate) AS invoice_date,
    EXTRACT(YEAR FROM invoicedate)::INTEGER AS year,
    EXTRACT(MONTH FROM invoicedate)::INTEGER AS month,
    EXTRACT(DAY FROM invoicedate)::INTEGER AS day
FROM retail.sales_raw
WHERE invoicedate IS NOT NULL
ON CONFLICT (invoice_date) DO NOTHING;

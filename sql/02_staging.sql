-- =============================================================================
-- 02_staging.sql
-- Description: Staging table definition for ingested raw transactions
-- =============================================================================

CREATE TABLE IF NOT EXISTS retail.sales_raw (
    invoiceno VARCHAR(50),
    stockcode VARCHAR(50),
    description TEXT,
    quantity INTEGER,
    invoicedate TIMESTAMP,
    unitprice NUMERIC(12, 2),
    customerid INTEGER,
    country VARCHAR(100),
    revenue NUMERIC(12, 2)
);

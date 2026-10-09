-- =============================================================================
-- 04_facts.sql
-- Description: Central Sales Fact Table definition with Foreign Keys
-- =============================================================================

CREATE TABLE IF NOT EXISTS retail.fact_sales (
    sales_key SERIAL PRIMARY KEY,
    
    -- Degenerate dimension (transaction identifier)
    invoice_no VARCHAR(50) NOT NULL,

    -- Foreign keys referencing dimensions
    customer_key INTEGER NOT NULL,
    product_key INTEGER NOT NULL,
    country_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,

    -- Quantitative Measures
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL,
    revenue NUMERIC(12, 2) NOT NULL,

    -- Foreign key constraints
    CONSTRAINT fk_sales_customer FOREIGN KEY (customer_key) REFERENCES retail.dim_customer(customer_key),
    CONSTRAINT fk_sales_product FOREIGN KEY (product_key) REFERENCES retail.dim_product(product_key),
    CONSTRAINT fk_sales_country FOREIGN KEY (country_key) REFERENCES retail.dim_country(country_key),
    CONSTRAINT fk_sales_date FOREIGN KEY (date_key) REFERENCES retail.dim_date(date_key)
);

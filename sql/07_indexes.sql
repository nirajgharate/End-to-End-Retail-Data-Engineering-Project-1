-- =============================================================================
-- 07_indexes.sql
-- Description: Performance indexes on Fact table foreign keys & business keys
-- =============================================================================

CREATE INDEX IF NOT EXISTS idx_fact_sales_customer ON retail.fact_sales(customer_key);
CREATE INDEX IF NOT EXISTS idx_fact_sales_product ON retail.fact_sales(product_key);
CREATE INDEX IF NOT EXISTS idx_fact_sales_country ON retail.fact_sales(country_key);
CREATE INDEX IF NOT EXISTS idx_fact_sales_date ON retail.fact_sales(date_key);
CREATE INDEX IF NOT EXISTS idx_fact_sales_invoice ON retail.fact_sales(invoice_no);

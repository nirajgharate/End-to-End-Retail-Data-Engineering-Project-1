-- =============================================================================
-- 09_data_quality_checks.sql
-- Description: Automated Data Quality Audits & Referential Integrity Assertions
-- =============================================================================

-- 1. Verify Raw Staging Record Count
SELECT 'Staging Record Count' AS check_name, COUNT(*) AS metric_value FROM retail.sales_raw;

-- 2. Verify Fact Table Record Count
SELECT 'Fact Sales Record Count' AS check_name, COUNT(*) AS metric_value FROM retail.fact_sales;

-- 3. Check for Orphaned Customer Foreign Keys (Must return 0)
SELECT 'Orphaned Customer FK Count' AS check_name, COUNT(*) AS metric_value
FROM retail.fact_sales fs
LEFT JOIN retail.dim_customer dc ON fs.customer_key = dc.customer_key
WHERE dc.customer_key IS NULL;

-- 4. Check for Orphaned Product Foreign Keys (Must return 0)
SELECT 'Orphaned Product FK Count' AS check_name, COUNT(*) AS metric_value
FROM retail.fact_sales fs
LEFT JOIN retail.dim_product dp ON fs.product_key = dp.product_key
WHERE dp.product_key IS NULL;

-- 5. Check for Orphaned Country Foreign Keys (Must return 0)
SELECT 'Orphaned Country FK Count' AS check_name, COUNT(*) AS metric_value
FROM retail.fact_sales fs
LEFT JOIN retail.dim_country dco ON fs.country_key = dco.country_key
WHERE dco.country_key IS NULL;

-- 6. Check for Orphaned Date Foreign Keys (Must return 0)
SELECT 'Orphaned Date FK Count' AS check_name, COUNT(*) AS metric_value
FROM retail.fact_sales fs
LEFT JOIN retail.dim_date dd ON fs.date_key = dd.date_key
WHERE dd.date_key IS NULL;

-- 7. Validate Total Revenue Reconciliation
SELECT 
    'Staging Total Revenue' AS check_name, SUM(revenue)::NUMERIC(14,2) AS metric_value FROM retail.sales_raw
UNION ALL
SELECT 
    'Fact Table Total Revenue' AS check_name, SUM(revenue)::NUMERIC(14,2) AS metric_value FROM retail.fact_sales;

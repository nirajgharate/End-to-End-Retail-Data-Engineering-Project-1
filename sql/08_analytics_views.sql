-- =============================================================================
-- 08_analytics_views.sql
-- Description: Denormalized Reporting View for Power BI & Business Intelligence
-- =============================================================================

CREATE OR REPLACE VIEW retail.vw_sales_analytics AS
SELECT
    -- Transaction Identifiers
    fs.sales_key,
    fs.invoice_no,

    -- Dimensional Attributes
    dc.customer_id,
    dp.stockcode,
    dp.description AS product_description,
    dco.country,
    
    -- Date & Time Intelligence Attributes
    dd.invoice_date,
    dd.year,
    dd.month,
    dd.day,

    -- Quantitative Measures
    fs.quantity,
    fs.unit_price,
    fs.revenue
FROM retail.fact_sales fs
INNER JOIN retail.dim_customer dc ON fs.customer_key = dc.customer_key
INNER JOIN retail.dim_product dp ON fs.product_key = dp.product_key
INNER JOIN retail.dim_country dco ON fs.country_key = dco.country_key
INNER JOIN retail.dim_date dd ON fs.date_key = dd.date_key;

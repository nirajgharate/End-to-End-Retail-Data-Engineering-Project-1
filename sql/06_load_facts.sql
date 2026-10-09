-- =============================================================================
-- 06_load_facts.sql
-- Description: Population scripts for Fact Sales Table
-- =============================================================================

INSERT INTO retail.fact_sales (
    invoice_no,
    customer_key,
    product_key,
    country_key,
    date_key,
    quantity,
    unit_price,
    revenue
)
SELECT
    sr.invoiceno,
    dc.customer_key,
    dp.product_key,
    dco.country_key,
    dd.date_key,
    sr.quantity,
    sr.unitprice,
    sr.revenue
FROM retail.sales_raw sr
JOIN retail.dim_customer dc ON CAST(sr.customerid AS INTEGER) = dc.customer_id
JOIN retail.dim_product dp ON sr.stockcode = dp.stockcode
JOIN retail.dim_country dco ON sr.country = dco.country
JOIN retail.dim_date dd ON DATE(sr.invoicedate) = dd.invoice_date;

-- CREATE DATABASE telco_project_db;

-- USE telco_project_db;

-- SELECT * FROM raw_telco_data LIMIT 10;

-- 1. Create the CUSTOMERS table (Demographics)
-- CREATE TABLE customers AS
-- SELECT 
--     customer_id, 
--     gender, 
--     senior_citizen, 
--     partner, 
--     dependents
-- FROM raw_telco_data;

-- -- 2. Create the SERVICES table (Product details)
-- CREATE TABLE services AS
-- SELECT 
--     customer_id, 
--     phone_service, 
--     multiplelines, 
--     internet_service, 
--     online_security, 
--     device_protection, 
--     tech_support, 
--     streaming_tv, 
--     streaming_movies
-- FROM raw_telco_data;

-- -- 3. Create the BILLING table (Money & Churn)
-- CREATE TABLE billing AS
-- SELECT 
--     customer_id, 
--     contract, 
--     paperless_billing, 
--     payment_method, 
--     monthly_charges, 
--     total_charges, 
--     churn
-- FROM raw_telco_data;

-- -- 4. Set Primary Keys (Crucial for Power BI relationships)
-- 1. Fix the CUSTOMERS table
-- ALTER TABLE customers 
-- MODIFY customer_id VARCHAR(50) NOT NULL;

-- ALTER TABLE customers 
-- ADD PRIMARY KEY (customer_id);

-- -- 2. Fix the SERVICES table
-- ALTER TABLE services 
-- MODIFY customer_id VARCHAR(50) NOT NULL;

-- ALTER TABLE services 
-- ADD PRIMARY KEY (customer_id);

-- -- 3. Fix the BILLING table
-- ALTER TABLE billing 
-- MODIFY customer_id VARCHAR(50) NOT NULL;

-- ALTER TABLE billing 
-- ADD PRIMARY KEY (customer_id);billingraw_telco_dataraw_telco_databillingcustomers
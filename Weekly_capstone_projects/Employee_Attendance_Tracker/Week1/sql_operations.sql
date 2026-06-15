-- Database

CREATE DATABASE RetailSalesDB;
USE RetailSalesDB;

-- Create Tables

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    cost DECIMAL(10,2),
    selling_price DECIMAL(10,2)
);

CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    city VARCHAR(50),
    region VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    designation VARCHAR(50),
    salary DECIMAL(10,2),
    store_id INT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    store_id INT,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert Sample Data

-- Products
INSERT INTO products VALUES
(201,'Tablet','Electronics',18000,25000),
(202,'Bluetooth Speaker','Accessories',1200,2200),
(203,'Office Chair','Furniture',3500,5500),
(204,'Monitor','Electronics',9000,14000);

-- Stores
INSERT INTO stores VALUES
(11,'Delhi Outlet','Delhi','North'),
(12,'Pune Outlet','Pune','West'),
(13,'Kochi Outlet','Kochi','South');

-- Employees
INSERT INTO employees VALUES
(501,'Suresh','Manager',70000,11),
(502,'Divya','Sales Executive',45000,12),
(503,'Naveen','Cashier',30000,13);

-- Sales
INSERT INTO sales VALUES
(9001,11,201,4,'2026-07-01'),
(9002,12,202,10,'2026-07-01'),
(9003,13,203,6,'2026-07-02'),
(9004,11,204,8,'2026-07-03');

-- Create Operations

INSERT INTO products VALUES
(205,'Printer','Electronics',7000,10000);

INSERT INTO stores VALUES
(14,'Jaipur Outlet','Jaipur','North');

INSERT INTO employees VALUES
(504,'Megha','Sales Associate',35000,14);

INSERT INTO sales VALUES
(9005,14,205,5,'2026-07-04');

INSERT INTO sales VALUES
(9006,12,201,7,'2026-07-05');

INSERT INTO sales VALUES
(9007,13,202,9,'2026-07-05');

-- Read Operations

SELECT * FROM products;

SELECT * FROM sales;

SELECT product_name, selling_price
FROM products
WHERE selling_price > 10000;

SELECT region, COUNT(*) AS total_stores
FROM stores
GROUP BY region;

SELECT
    p.product_name,
    SUM(s.quantity) AS units_sold
FROM sales s
JOIN products p
ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY units_sold DESC;

SELECT
    st.store_name,
    SUM(s.quantity * p.selling_price) AS revenue
FROM sales s
JOIN stores st
ON s.store_id = st.store_id
JOIN products p
ON s.product_id = p.product_id
GROUP BY st.store_name;

-- Update Operations

UPDATE products
SET selling_price = 26000
WHERE product_id = 201;

UPDATE employees
SET designation = 'Senior Manager'
WHERE employee_id = 501;

UPDATE stores
SET region = 'Central'
WHERE store_id = 12;

UPDATE sales
SET quantity = 12
WHERE sale_id = 9005;

UPDATE products
SET selling_price = selling_price + 1000
WHERE category = 'Electronics';

UPDATE employees
SET salary = salary * 1.10
WHERE designation LIKE '%Sales%';

-- Delete Operations

DELETE FROM sales
WHERE sale_id = 9007;

DELETE FROM employees
WHERE employee_id = 504;

DELETE FROM stores
WHERE store_id = 14;

DELETE FROM products
WHERE product_id = 205;

DELETE FROM sales
WHERE quantity < 5;

DELETE FROM products
WHERE product_id NOT IN
(
    SELECT DISTINCT product_id
    FROM sales
);

-- Stored Procedures

DELIMITER //

CREATE PROCEDURE GetStoreRevenue(IN p_store INT)
BEGIN
    SELECT
        st.store_name,
        SUM(s.quantity * p.selling_price) AS total_revenue
    FROM sales s
    JOIN stores st
        ON s.store_id = st.store_id
    JOIN products p
        ON s.product_id = p.product_id
    WHERE st.store_id = p_store
    GROUP BY st.store_name;
END //

CREATE PROCEDURE GetProductSales(IN p_product INT)
BEGIN
    SELECT
        p.product_name,
        SUM(s.quantity) AS total_quantity
    FROM sales s
    JOIN products p
        ON s.product_id = p.product_id
    WHERE p.product_id = p_product
    GROUP BY p.product_name;
END //

CREATE PROCEDURE GetRegionRevenue(IN p_region VARCHAR(50))
BEGIN
    SELECT
        st.region,
        SUM(s.quantity * p.selling_price) AS revenue
    FROM sales s
    JOIN stores st
        ON s.store_id = st.store_id
    JOIN products p
        ON s.product_id = p.product_id
    WHERE st.region = p_region
    GROUP BY st.region;
END //

DELIMITER ;

-- Execute Procedures

CALL GetStoreRevenue(11);
CALL GetProductSales(201);
CALL GetRegionRevenue('North');

-- Indexes

CREATE INDEX idx_product_name
ON products(product_name);

CREATE INDEX idx_product_category
ON products(category);

CREATE INDEX idx_store_region
ON stores(region);

CREATE INDEX idx_sales_product
ON sales(product_id);

CREATE INDEX idx_sales_date
ON sales(sale_date);

CREATE INDEX idx_employee_store
ON employees(store_id);

-- Show Indexes

SHOW INDEX FROM products;
SHOW INDEX FROM stores;
SHOW INDEX FROM sales;
SHOW INDEX FROM employees;

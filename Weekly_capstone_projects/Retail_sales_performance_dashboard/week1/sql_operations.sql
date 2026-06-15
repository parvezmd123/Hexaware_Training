-- ==========================================
-- DATABASE
-- ==========================================
CREATE DATABASE RetailSalesDB;
USE RetailSalesDB;

-- ==========================================
-- TABLES
-- ==========================================

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    cost DECIMAL(10,2),
    price DECIMAL(10,2)
);

CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    designation VARCHAR(50),
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

-- ==========================================
-- INSERT SAMPLE DATA
-- ==========================================

INSERT INTO products VALUES
(101,'Laptop','Electronics',45000,60000),
(102,'Mobile','Electronics',18000,25000),
(103,'Chair','Furniture',3000,5000),
(104,'Table','Furniture',5000,8000);

INSERT INTO stores VALUES
(1,'Chennai Store','South'),
(2,'Bangalore Store','South'),
(3,'Mumbai Store','West');

INSERT INTO employees VALUES
(1,'Rahul','Manager',1),
(2,'Priya','Sales Executive',2),
(3,'Amit','Cashier',3);

INSERT INTO sales VALUES
(1001,1,101,5,'2026-06-01'),
(1002,2,102,8,'2026-06-01'),
(1003,3,103,10,'2026-06-02'),
(1004,1,104,6,'2026-06-03');

-- ==========================================
-- CREATE OPERATIONS
-- ==========================================

INSERT INTO sales VALUES (1005,2,101,7,'2026-06-04');

INSERT INTO sales VALUES (1006,3,102,12,'2026-06-04');

INSERT INTO products VALUES
(105,'Smart Watch','Electronics',4000,6500);

INSERT INTO stores VALUES
(4,'Hyderabad Store','South');

INSERT INTO employees VALUES
(4,'Kiran','Sales Executive',4);

INSERT INTO sales VALUES
(1007,4,105,15,'2026-06-05');

-- ==========================================
-- READ OPERATIONS
-- ==========================================

SELECT * FROM sales;

SELECT * FROM products
WHERE price > 10000;

SELECT * FROM stores
WHERE region='South';

SELECT p.product_name,
       SUM(s.quantity) AS units_sold
FROM sales s
JOIN products p
ON s.product_id=p.product_id
GROUP BY p.product_name;

SELECT st.store_name,
       SUM(s.quantity*p.price) AS revenue
FROM sales s
JOIN stores st ON s.store_id=st.store_id
JOIN products p ON s.product_id=p.product_id
GROUP BY st.store_name;

SELECT e.employee_name,
       st.store_name
FROM employees e
JOIN stores st
ON e.store_id=st.store_id;

-- ==========================================
-- UPDATE OPERATIONS
-- ==========================================

UPDATE products
SET price=62000
WHERE product_id=101;

UPDATE stores
SET region='South-East'
WHERE store_id=4;

UPDATE employees
SET designation='Senior Executive'
WHERE employee_id=4;

UPDATE sales
SET quantity=20
WHERE sale_id=1007;

UPDATE products
SET price=price*1.05
WHERE category='Electronics';

UPDATE sales
SET quantity=quantity+2
WHERE quantity<10;

-- ==========================================
-- DELETE OPERATIONS
-- ==========================================

DELETE FROM sales
WHERE sale_id=1007;

DELETE FROM employees
WHERE employee_id=4;

DELETE FROM stores
WHERE store_id=4;

DELETE FROM products
WHERE product_id=105;

DELETE FROM sales
WHERE quantity<6;

DELETE FROM products
WHERE product_id NOT IN
(SELECT DISTINCT product_id FROM sales);

-- ==========================================
-- STORED PROCEDURES
-- ==========================================

DELIMITER //

CREATE PROCEDURE DailySales(
IN p_store INT,
IN p_date DATE
)
BEGIN
SELECT st.store_name,
       SUM(s.quantity*p.price) AS total_sales
FROM sales s
JOIN stores st ON s.store_id=st.store_id
JOIN products p ON s.product_id=p.product_id
WHERE s.store_id=p_store
AND s.sale_date=p_date
GROUP BY st.store_name;
END//

CREATE PROCEDURE ProductRevenue(
IN pid INT
)
BEGIN
SELECT p.product_name,
       SUM(s.quantity*p.price) AS revenue
FROM sales s
JOIN products p
ON s.product_id=p.product_id
WHERE p.product_id=pid
GROUP BY p.product_name;
END//

CREATE PROCEDURE StorePerformance()
BEGIN
SELECT st.store_name,
       SUM(s.quantity*p.price) total_sales
FROM stores st
LEFT JOIN sales s
ON st.store_id=s.store_id
LEFT JOIN products p
ON s.product_id=p.product_id
GROUP BY st.store_name;
END//

CREATE PROCEDURE TopProducts()
BEGIN
SELECT p.product_name,
       SUM(s.quantity) units
FROM sales s
JOIN products p
ON s.product_id=p.product_id
GROUP BY p.product_name
ORDER BY units DESC
LIMIT 5;
END//

CREATE PROCEDURE UnderPerforming(
IN min_units INT
)
BEGIN
SELECT p.product_name,
       SUM(s.quantity) total_units
FROM sales s
JOIN products p
ON s.product_id=p.product_id
GROUP BY p.product_name
HAVING total_units<min_units;
END//

CREATE PROCEDURE RegionSales(
IN reg VARCHAR(50)
)
BEGIN
SELECT st.region,
       SUM(s.quantity*p.price) revenue
FROM sales s
JOIN stores st
ON s.store_id=st.store_id
JOIN products p
ON s.product_id=p.product_id
WHERE st.region=reg
GROUP BY st.region;
END//

DELIMITER ;

-- Execute Procedures

CALL DailySales(1,'2026-06-01');

CALL ProductRevenue(101);

CALL StorePerformance();

CALL TopProducts();

CALL UnderPerforming(20);

CALL RegionSales('South');

-- ==========================================
-- INDEXES
-- ==========================================

CREATE INDEX idx_product
ON sales(product_id);

CREATE INDEX idx_store
ON sales(store_id);

CREATE INDEX idx_sale_date
ON sales(sale_date);

CREATE INDEX idx_region
ON stores(region);

CREATE INDEX idx_employee_store
ON employees(store_id);

CREATE INDEX idx_product_store
ON sales(product_id,store_id);

SHOW INDEX FROM sales;
SHOW INDEX FROM stores;
SHOW INDEX FROM employees;
```

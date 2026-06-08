-- CREATE TABLE
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(30)
);

-- INSERT VALUES
INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,10,'Hyderabad'),
(2,'Mobile','Electronics',25000,25,'Bangalore'),
(3,'Printer','Electronics',18000,8,'Pune'),
(4,'Office Chair','Furniture',7500,15,'Mumbai'),
(5,'Desk','Furniture',12000,5,'Chennai'),
(6,'Notebook','Stationery',80,200,'Hyderabad'),
(7,'Pen','Stationery',20,500,'Delhi'),
(8,'Water Bottle','Accessories',500,50,'Bangalore');

SELECT * FROM products;

SELECT product_name, price FROM products;

--filter exercises

SELECT * 
FROM products
WHERE category = 'Electronics';

SELECT *
FROM products
WHERE NOT category = 'Electronics';

SELECT *
FROM products
WHERE category = 'Electronics'
AND price > 20000;

SELECT *
FROM products
WHERE supplier_city = 'Hyderabad'
OR supplier_city = 'Delhi';

SELECT *
FROM products
WHERE price BETWEEN 500 AND 20000;

SELECT *
FROM products
WHERE supplier_city IN ('Hyderabad', 'Delhi');

-- Starts with P
SELECT *
FROM products
WHERE product_name LIKE 'P%';

-- Ends with r
SELECT *
FROM products
WHERE product_name LIKE '%r';

-- Contains top
SELECT *
FROM products
WHERE product_name LIKE '%top%';

--groupby exercises

SELECT category,
COUNT(*) AS product_count
FROM products
GROUP BY category;

SELECT category,
SUM(price) AS total_price
FROM products
GROUP BY category;

SELECT category,
COUNT(*) AS total_products
FROM products
GROUP BY category
HAVING COUNT(*) > 1;

-- Ascending
SELECT *
FROM products
ORDER BY price ASC;

-- Descending
SELECT *
FROM products
ORDER BY price DESC;

-- Top 3 cheapest products
-- SELECT *
-- FROM products
-- ORDER BY price ASC 
-- LIMIT 3;

--update and delete exercises
UPDATE products
SET price = 60000
WHERE product_id = 1;

DELETE FROM products
WHERE product_id = 8;

--alias and distinct exercises
SELECT DISTINCT category
FROM products;

SELECT product_name AS Name,
price AS Cost
FROM products;

--aggregate functions exercises

SELECT COUNT(*) AS total_products
FROM products;

SELECT MAX(price) AS highest_price
FROM products;

SELECT MIN(price) AS lowest_price
FROM products;

SELECT AVG(price) AS average_price
FROM products;

SELECT SUM(stock_quantity) AS total_stock
FROM products;

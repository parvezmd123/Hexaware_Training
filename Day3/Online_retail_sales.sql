#MYSQL Capstone Project
#PART1-DATABASE DESIGN

CREATE DATABASE retail_capstone_db;

USE retail_capstone_db;
#CREATING TABLES
-- 1.Customers Table
CREATE TABLE customers
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
state VARCHAR(50),
gender VARCHAR(10),
membership_type VARCHAR(30)
);

-- 2.Products Table 
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10 , 2 )
);

-- 3.Orders Table 
CREATE TABLE orders
(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
order_status VARCHAR(30)
);

-- 4.Order_items Table
CREATE TABLE order_items
(
item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT
);

-- 5.Payments Table
CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
order_id INT,

payment_mode VARCHAR(30),
payment_status VARCHAR(30),
amount DECIMAL(10,2)
);

-- 6.Deliveries Table 
CREATE TABLE deliveries
(
delivery_id INT PRIMARY KEY,
order_id INT,
delivery_partner VARCHAR(50),
delivery_status VARCHAR(30),
delivery_city VARCHAR(50)
);

#PART-2 DATA CREATION
-- Insert Customers (11 records - multi-city, varying tiers)
INSERT INTO customers VALUES 
(101, 'Aarav Sharma', 'Hyderabad', 'Telangana', 'Male', 'Gold'),
(102, 'Aditi Rao', 'Hyderabad', 'Telangana', 'Female', 'Silver'),
(103, 'Rocky Bhai', 'Mumbai', 'Maharashtra', 'Male', 'Gold'),
(104, 'Priya Patel', 'Mumbai', 'Maharashtra', 'Female', 'Regular'),
(105, 'Ananya Iyer', 'Bengaluru', 'Karnataka', 'Female', 'Gold'),
(106, 'Vikram king', 'Delhi', 'Delhi', 'Male', 'Regular'),
(107, 'Kavita Reddy', 'Hyderabad', 'Telangana', 'Female', 'Regular'),
(108, 'Arjun Mehta', 'Bengaluru', 'Karnataka', 'Male', 'Silver'),
(109, 'Sneha Gupta', 'Kolkata', 'West Bengal', 'Female', 'Silver'),
(110, 'Rahul dravid', 'Delhi', 'Delhi', 'Male', 'Gold'),
(111, 'Amit Mishra', 'Pune', 'Maharashtra', 'Male', 'Regular'); 

-- Insert Products (10 records - Electronics, Fashion, Home Decor)
INSERT INTO products VALUES 
(201, 'Wireless Earbuds', 'Electronics', 2499.00),
(202, 'Smart Watch', 'Electronics', 4999.00),
(203, 'Running Shoes', 'Fashion', 3200.00),
(204, 'Denim Jacket', 'Fashion', 1800.00),
(205, 'Cotton Bedshirt', 'Fashion', 850.00),
(206, 'LED Desk Lamp', 'Electronics', 1200.00),
(207, 'Ceramic Flower Vase', 'Home Decor', 650.00),
(208, 'Bluetooth Speaker', 'Electronics', 3500.00),
(209, 'Leather Wallet', 'Fashion', 1100.00),
(210, 'Coffee Mug Set', 'Home Decor', 450.00);

-- Insert Orders (16 records - Includes edge cases for data quality)
INSERT INTO orders VALUES 
(501, 101, '2026-01-05', 'Delivered'),
(502, 101, '2026-02-10', 'Delivered'),
(503, 102, '2026-01-15', 'Delivered'),
(504, 103, '2026-02-20', 'Shipped'),
(505, 104, '2026-03-01', 'Cancelled'),
(506, 105, '2026-03-05', 'Delivered'),
(507, 106, '2026-03-12', 'Pending'),
(508, 107, '2026-03-15', 'Delivered'),
(509, 108, '2026-03-18', 'Delivered'),
(510, 109, '2026-03-22', 'Cancelled'),
(511, 110, '2026-03-25', 'Delivered'),
(512, 102, '2026-03-28', 'Delivered'),
(513, 103, '2026-04-01', 'Delivered'),
(514, 105, '2026-04-03', 'Delivered'),
(515, 106, '2026-04-05', 'Delivered'),
(516, 104, '2026-04-06', 'Delivered');

-- Insert Order Items (22 records - handles multiple items per order)
INSERT INTO order_items VALUES 
(1, 501, 201, 1), (2, 501, 204, 2),
(3, 502, 202, 1),
(4, 503, 203, 1), (5, 503, 205, 2),
(6, 504, 208, 1),
(7, 505, 202, 1),
(8, 506, 201, 1), (9, 506, 206, 1),
(10, 507, 203, 1),
(11, 508, 204, 1),
(12, 509, 209, 2),
(13, 510, 202, 1),
(14, 511, 201, 2), (15, 511, 208, 1),
(16, 512, 206, 1),
(17, 513, 203, 2),
(18, 514, 202, 1), (19, 514, 204, 1),
(20, 515, 205, 3),
(21, 516, 201, 1),
(22, 501, 205, 1);

-- Insert Payments (16 records - tracking success, failure, and modes)
INSERT INTO payments VALUES 
(901, 501, 'UPI', 'Success', 6999.00),
(902, 502, 'Credit Card', 'Success', 4999.00),
(903, 503, 'Net Banking', 'Success', 4900.00),
(904, 504, 'UPI', 'Success', 3500.00),
(905, 505, 'Credit Card', 'Failed', 4999.00),
(906, 506, 'UPI', 'Success', 3699.00),
(907, 507, 'COD', 'Pending', 3200.00),
(908, 508, 'UPI', 'Success', 1800.00),
(909, 509, 'Debit Card', 'Success', 2200.00),
(910, 510, 'UPI', 'Success', 4999.00), 
(911, 511, 'Credit Card', 'Success', 8498.00),
(912, 512, 'UPI', 'Success', 1200.00),
(913, 513, 'Net Banking', 'Success', 6400.00),
(914, 514, 'UPI', 'Success', 6799.00),
(915, 515, 'COD', 'Success', 2550.00),
(916, 516, 'Debit Card', 'Failed', 2499.00); 

-- Insert Deliveries (15 records - mapping tracking statuses)
INSERT INTO deliveries VALUES 
(701, 501, 'Delhivery', 'Delivered', 'Hyderabad'),
(702, 502, 'BlueDart', 'Delivered', 'Hyderabad'),
(703, 503, 'Xpressbees', 'Delivered', 'Hyderabad'),
(704, 504, 'Delhivery', 'In Transit', 'Mumbai'),
(705, 506, 'BlueDart', 'Delivered', 'Bengaluru'),
(706, 507, 'Shadowfax', 'Pending', 'Delhi'),
(707, 508, 'Delhivery', 'Delivered', 'Hyderabad'),
(708, 509, 'Xpressbees', 'Delivered', 'Bengaluru'),
(709, 511, 'BlueDart', 'Delivered', 'Delhi'),
(710, 512, 'Delhivery', 'Delivered', 'Hyderabad'),
(711, 513, 'Shadowfax', 'Delivered', 'Mumbai'),
(712, 514, 'BlueDart', 'Delivered', 'Bengaluru'),
(713, 515, 'Xpressbees', 'Delivered', 'Delhi'),
(714, 516, 'Delhivery', 'Delivered', 'Mumbai');

-- PART-3 BASIC QUERIES

-- 1. Display all customers
SELECT * FROM customers;

-- 2. Display customer name, city, and membership type
SELECT customer_name, city, membership_type FROM customers;

-- 3. Display all products sorted by price descending
SELECT * FROM products ORDER BY price DESC;

-- 4. Find customers from Hyderabad
SELECT * FROM customers WHERE city = 'Hyderabad';

-- 5. Find Gold membership customers
SELECT * FROM customers WHERE membership_type = 'Gold';

-- 6. Find products priced between ₹500 and ₹5000
SELECT * FROM products WHERE price BETWEEN 500 AND 5000;

-- 7. Find products from categories Electronics and Fashion
SELECT * FROM products WHERE category IN ('Electronics', 'Fashion');

-- 8. Find orders placed after 2026-01-01
SELECT * FROM orders WHERE order_date > '2026-01-01';

-- 9. Find payments made using UPI
SELECT * FROM payments WHERE payment_mode = 'UPI';

-- 10. Find deliveries that are still pending
SELECT * FROM deliveries WHERE delivery_status = 'Pending';

-- Part4: Aggregrate Queries

-- 11. Count total customers
SELECT COUNT(*) AS total_customers FROM customers;

-- 12. Count total orders
SELECT COUNT(*) AS total_orders FROM orders;

-- 13. Count total products
SELECT COUNT(*) AS total_products FROM products;

-- 14. Find total revenue from successful payments
SELECT SUM(amount) AS total_revenue FROM payments WHERE payment_status = 'Success';

-- 15. Find average order payment amount
SELECT AVG(amount) AS average_payment_amount FROM payments;

-- 16. Find highest payment amount
SELECT MAX(amount) AS highest_payment_amount FROM payments;

-- 17. Find lowest payment amount
SELECT MIN(amount) AS lowest_payment_amount FROM payments;

-- 18. Count customers by city
SELECT city, COUNT(*) AS customer_count FROM customers GROUP BY city;

-- 19. Count products by category
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

-- 20. Count orders by order status
SELECT order_status, COUNT(*) AS order_count FROM orders GROUP BY order_status;

-- Part-5 Joins

-- 21. Display customer name with order ID and order date
SELECT c.customer_name, o.order_id, o.order_date 
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- 22. Display order ID, product name, quantity, and price
SELECT oi.order_id, p.product_name, oi.quantity, p.price 
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

-- 23. Display customer name, product name, quantity, and order date
SELECT c.customer_name, p.product_name, oi.quantity, o.order_date
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;

-- 24. Display order ID with payment mode, payment status, and amount
SELECT order_id, payment_mode, payment_status, amount 
FROM payments;

-- 25. Display order ID with delivery partner and delivery status
SELECT order_id, delivery_partner, delivery_status 
FROM deliveries;

-- 26. Display full order report
SELECT 
    c.customer_name, c.city, o.order_id, o.order_date,
    p.product_name, p.category, oi.quantity, p.price,
    pay.payment_status, d.delivery_status
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN payments pay ON o.order_id = pay.order_id
LEFT JOIN deliveries d ON o.order_id = d.order_id;

-- PART6:GROUPBY AND HAVING

-- 27. Total revenue by city 
SELECT c.city, SUM(pay.amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments pay ON o.order_id = pay.order_id
WHERE pay.payment_status = 'Success'
GROUP BY c.city;

-- 28. Total revenue by customer
SELECT c.customer_name, SUM(pay.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments pay ON o.order_id = pay.order_id
WHERE pay.payment_status = 'Success'
GROUP BY c.customer_id, c.customer_name;

-- 29. Total quantity sold by product
SELECT p.product_name, SUM(oi.quantity) AS total_quantity_sold
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name;

-- 30. Revenue by product category
SELECT p.category, SUM(pay.amount) AS category_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN payments pay ON oi.order_id = pay.order_id
WHERE pay.payment_status = 'Success'
GROUP BY p.category;

-- 31. Number of orders by customer
SELECT c.customer_name, COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name;

-- 32. Customers having more than 1 order
SELECT c.customer_name, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 1;

-- 33. Product categories having revenue greater than ₹10,000
SELECT p.category, SUM(pay.amount) AS category_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN payments pay ON oi.order_id = pay.order_id
WHERE pay.payment_status = 'Success'
GROUP BY p.category
HAVING SUM(pay.amount) > 10000;

-- 34. Cities having more than 2 customers
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
HAVING COUNT(*) > 2;

-- 35. Products sold more than 3 times (Total quantity sold > 3)
SELECT p.product_name, SUM(oi.quantity) AS total_units_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
HAVING SUM(oi.quantity) > 3;

-- PART-7 SUBQUERIES

-- 36. Find customers who placed orders
SELECT * FROM customers 
WHERE customer_id IN (SELECT DISTINCT customer_id FROM orders);

-- 37. Find customers who never placed orders
SELECT * FROM customers 
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);

-- 38. Find products that were never ordered
SELECT * FROM products 
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM order_items);

-- 39. Find orders with payment amount greater than average payment amount
SELECT * FROM payments 
WHERE amount > (SELECT AVG(amount) FROM payments);

-- 40. Find customer who made the highest payment
SELECT * FROM customers 
WHERE customer_id = (
    SELECT o.customer_id 
    FROM orders o 
    JOIN payments p ON o.order_id = p.order_id 
    ORDER BY p.amount DESC 
    LIMIT 1
);

-- 41. Find products priced above the average product price
SELECT * FROM products 
WHERE price > (SELECT AVG(price) FROM products);

-- 42. Find customers who ordered Electronics products
SELECT * FROM customers 
WHERE customer_id IN (
    SELECT DISTINCT o.customer_id 
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    WHERE p.category = 'Electronics'
);

-- 43. Find orders that have successful payments
SELECT * FROM orders 
WHERE order_id IN (SELECT order_id FROM payments WHERE payment_status = 'Success');

-- 44. Find orders that are not delivered yet
SELECT * FROM orders 
WHERE order_id NOT IN (SELECT order_id FROM deliveries WHERE delivery_status = 'Delivered');

-- 45. Find customers whose total spending is above average customer spending
SELECT c.customer_id, c.customer_name, SUM(p.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
WHERE p.payment_status = 'Success'
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) > (
    SELECT AVG(customer_total) FROM (
        SELECT SUM(amount) AS customer_total 
        FROM payments pay
        JOIN orders ord ON pay.order_id = ord.order_id
        WHERE pay.payment_status = 'Success'
        GROUP BY ord.customer_id
    ) AS avg_spend_subquery
);

-- PART8.DATA QUALITY CHECKS 

-- 46. Find orders without payment records
SELECT * FROM orders 
WHERE order_id NOT IN (SELECT order_id FROM payments);

-- 47. Find orders without delivery records
SELECT * FROM orders 
WHERE order_id NOT IN (SELECT order_id FROM deliveries);

-- 48. Find payments where amount is NULL or 0
SELECT * FROM payments WHERE amount IS NULL OR amount <= 0;

-- 49. Find cancelled orders with successful payment
SELECT o.order_id, o.order_status, p.payment_status 
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'Cancelled' AND p.payment_status = 'Success';

-- 50. Find delivered orders with failed payment
SELECT o.order_id, o.order_status, p.payment_status 
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'Delivered' AND p.payment_status = 'Failed';

-- 51. Find order items with invalid product IDs (Orphan rows check)
SELECT * FROM order_items 
WHERE product_id NOT IN (SELECT product_id FROM products);

-- 52. Find orders with invalid customer IDs (Orphan rows check)
SELECT * FROM orders 
WHERE customer_id NOT IN (SELECT customer_id FROM customers);
 








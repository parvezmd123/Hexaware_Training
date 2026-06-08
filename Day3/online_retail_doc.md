Retail Capstone Project Documentatnion

Database Design

The Retail Capstone Project was developed using MySQL to manage and analyze the operations of an online retail business. The database consists of six core tables: customers, products, orders, order_items, payments, and deliveries. Primary key and foreign key constraints were implemented to establish relationships between tables and ensure data consistency, integrity, and efficient data management.

Table Relationships

The database follows a relational structure where a customer can place multiple orders, and each order can include multiple products. The order_items** table serves as a bridge between orders and products, enabling the management of product quantities and order details. Each order is associated with corresponding payment and delivery records. The main relationships are: customers → orders, orders → order_items, products → order_items, orders → payments, and orders → deliveries**.

Key Insights from Reports

Various SQL queries were used to generate business insights from the retail data. Analysis revealed that the Electronics category contributed significantly to overall revenue, while cities such as Hyderabad had a strong customer presence. Customer purchasing behavior was examined to identify repeat buyers and frequent orders. The reports also highlighted pending deliveries and unsuccessful payment transactions. Additionally, data quality checks were performed to detect missing values and invalid records. The project demonstrated practical usage of SQL concepts including joins, aggregate functions, GROUP BY, HAVING clauses, subqueries, and data quality analysis techniques.

Hospital Management System – Short Documentation

Database Design

The Hospital Management System is developed using a relational database model to efficiently manage hospital operations. The database consists of seven main tables: patients, doctors, departments, appointments, treatments, bills, and payments. Each table is designed using normalization principles to reduce data redundancy, improve consistency, and maintain data integrity.

Table Relationships

The database follows a structured relational architecture. A department can have multiple doctors, and a doctor can handle multiple appointments. A patient may have multiple appointments over time. Each appointment is associated with a treatment record, and every appointment generates a bill. A bill can be linked to one or more payment transactions. Foreign key constraints are used throughout the database to ensure referential integrity and maintain accurate relationships between records.

Key Insights from Reports

SQL queries are used to generate valuable insights from the system, including the total number of patients, doctors, and appointments, overall hospital revenue, patients with the highest billing amounts, doctors with the highest workload, and departments generating the most revenue. The reports also help identify unpaid or partially paid bills, missing treatment records, and other data quality issues. These insights support better decision-making, efficient resource allocation, and improved financial management within the hospital.

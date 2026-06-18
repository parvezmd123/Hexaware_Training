# Overview of Three-Level Namespace and Creating Unity Catalog Objects

## What is the Three-Level Namespace?

In Unity Catalog, every object is identified using a **three-level namespace**:

```text
catalog.schema.object
```

- **Catalog** – The top-level container used to organize data.
- **Schema (Database)** – Groups related objects within a catalog.
- **Object** – A table, view, function, volume, or model.

### Example

```text
sales_catalog.retail.orders
```

Where:
- `sales_catalog` → Catalog
- `retail` → Schema
- `orders` → Table

---

# Unity Catalog Hierarchy

```text
Metastore
│
└── Catalog
    │
    └── Schema
        │
        ├── Tables
        ├── Views
        ├── Functions
        └── Volumes
```

Example:

```text
Metastore
│
└── sales_catalog
    │
    └── retail
        │
        ├── customers
        ├── orders
        ├── products
        └── sales_view
```

---

# Benefits of Three-Level Namespace

- Better organization of data.
- Prevents naming conflicts.
- Supports fine-grained access control.
- Simplifies data governance.
- Enables sharing across multiple workspaces.
- Improves data discovery and management.

---

# Creating Unity Catalog Objects

## 1. Create a Catalog

```sql
CREATE CATALOG sales_catalog;
```

Verify:

```sql
SHOW CATALOGS;
```

---

## 2. Create a Schema

```sql
CREATE SCHEMA sales_catalog.retail;
```

Verify:

```sql
SHOW SCHEMAS IN sales_catalog;
```

---

## 3. Create a Table

```sql
CREATE TABLE sales_catalog.retail.customers (
    customer_id INT,
    customer_name STRING,
    city STRING
);
```

---

## 4. Insert Data

```sql
INSERT INTO sales_catalog.retail.customers
VALUES
(101, 'Rahul', 'Chennai'),
(102, 'Priya', 'Bengaluru'),
(103, 'Ahmed', 'Hyderabad');
```

---

## 5. Query the Table

```sql
SELECT * FROM sales_catalog.retail.customers;
```

---

## 6. Create a View

```sql
CREATE VIEW sales_catalog.retail.chennai_customers AS
SELECT *
FROM sales_catalog.retail.customers
WHERE city = 'Chennai';
```

Query the view:

```sql
SELECT * FROM sales_catalog.retail.chennai_customers;
```

---

## 7. Create a Function

```sql
CREATE FUNCTION sales_catalog.retail.add_tax(amount DOUBLE)
RETURNS DOUBLE
RETURN amount * 1.18;
```

Use the function:

```sql
SELECT sales_catalog.retail.add_tax(1000);
```

---

# Create and Enable Unity Catalog

## Step 1: Create a Metastore

1. Open the Databricks Account Console.
2. Navigate to **Data → Metastores**.
3. Click **Create Metastore**.
4. Provide:
   - Metastore Name
   - Cloud Region
   - Storage Location
5. Click **Create**.

---

## Step 2: Assign Metastore to Workspace

1. Open the created metastore.
2. Go to **Workspaces**.
3. Click **Assign to Workspace**.
4. Select your Databricks workspace.
5. Save the changes.

---

## Step 3: Verify Unity Catalog

```sql
SHOW CATALOGS;
```

Expected output:

```text
main
samples
system
```

---

## Step 4: Create a Catalog

```sql
CREATE CATALOG sales_catalog;
```

---

## Step 5: Create a Schema

```sql
CREATE SCHEMA sales_catalog.retail;
```

---

## Step 6: Create a Table

```sql
CREATE TABLE sales_catalog.retail.orders (
    order_id INT,
    customer_name STRING,
    amount DOUBLE
);
```

---

## Step 7: Grant Permissions

```sql
GRANT SELECT ON TABLE sales_catalog.retail.orders TO analysts;
```

---

# Overview of Data Governance

Data Governance is the framework for managing data securely, accurately, and consistently across an organization.

## Objectives

- Ensure data quality.
- Protect sensitive information.
- Maintain compliance.
- Control user access.
- Track data usage and ownership.

## Components

- Data Security
- Data Quality
- Data Privacy
- Access Control
- Auditing
- Metadata Management

---

# What is Unity Catalog?

Unity Catalog is Databricks' unified governance solution for data and AI assets.

It provides centralized management for:

- Tables
- Views
- Functions
- Volumes
- Machine Learning Models

## Features

- Centralized governance
- Fine-grained permissions
- Role-based access control
- Data lineage
- Audit logging
- Metadata management
- Cross-workspace sharing

---

# Three-Level Namespace Summary

| Level | Description | Example |
|--------|-------------|----------|
| Catalog | Top-level container | `sales_catalog` |
| Schema | Groups related objects | `retail` |
| Object | Table/View/Function | `customers` |

Reference format:

```text
catalog.schema.object
```

Example:

```text
sales_catalog.retail.customers
```

---

# Key Takeaways

- Unity Catalog organizes objects using `catalog.schema.object`.
- A Metastore is the top-level governance layer.
- Catalogs contain schemas.
- Schemas contain tables, views, and functions.
- Unity Catalog simplifies security, governance, and collaboration.
- Fine-grained permissions can be granted at the catalog, schema, or table level.
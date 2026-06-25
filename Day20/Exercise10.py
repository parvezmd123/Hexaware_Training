from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv

# -----------------------------------
# Task 1: Create Orders CSV
# -----------------------------------
def create_orders():
    with open("/tmp/orders.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["product", "quantity", "price"])
        writer.writerow(["Laptop", 1, 70000])
        writer.writerow(["Mouse", 4, 500])
        writer.writerow(["Monitor", 2, 12000])
        writer.writerow(["Keyboard", 3, 1500])

    print("orders.csv created successfully.")


# -----------------------------------
# Task 2: Calculate Revenue
# -----------------------------------
def calculate_order_value():
    revenues = []
    total_revenue = 0
    highest_product = ""
    highest_revenue = 0

    with open("/tmp/orders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            product = row["product"]
            quantity = int(row["quantity"])
            price = int(row["price"])

            revenue = quantity * price
            total_revenue += revenue

            if revenue > highest_revenue:
                highest_revenue = revenue
                highest_product = product

            revenues.append((product, revenue))

    with open("/tmp/revenue.txt", "w") as file:
        for product, revenue in revenues:
            file.write(f"{product},{revenue}\n")

        file.write(f"TOTAL,{total_revenue}\n")
        file.write(f"HIGHEST,{highest_product}\n")

    print("Revenue calculated successfully.")


# -----------------------------------
# Task 3: Generate Sales Report
# -----------------------------------
def generate_sales_report():
    with open("/tmp/revenue.txt", "r") as file:
        lines = file.readlines()

    with open("/tmp/sales_report.txt", "w") as report:
        report.write("Sales Report\n")
        report.write("====================\n")

        for line in lines[:-2]:
            product, revenue = line.strip().split(",")
            report.write(f"{product} = {revenue}\n")

        total = lines[-2].strip().split(",")[1]
        highest = lines[-1].strip().split(",")[1]

        report.write("\n")
        report.write(f"Total Revenue = {total}\n")
        report.write(f"Highest Selling Product = {highest}\n")

    print("Sales report generated successfully.")

    with open("/tmp/sales_report.txt", "r") as report:
        print(report.read())


# -----------------------------------
# DAG Definition
# -----------------------------------
with DAG(
    dag_id="exercise10_online_orders",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Online Orders Revenue Report",
) as dag:

    create_orders_task = PythonOperator(
        task_id="create_orders",
        python_callable=create_orders,
    )

    calculate_order_value_task = PythonOperator(
        task_id="calculate_order_value",
        python_callable=calculate_order_value,
    )

    generate_sales_report_task = PythonOperator(
        task_id="generate_sales_report",
        python_callable=generate_sales_report,
    )

    # Task Dependencies
    create_orders_task >> calculate_order_value_task >> generate_sales_report_task

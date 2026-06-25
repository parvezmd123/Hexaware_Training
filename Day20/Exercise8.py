from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# -----------------------------
# Task 1: Create Electricity File
# -----------------------------
def create_bill_file():
    data = """Rahul,210
Priya,180
Amit,300
Sneha,150
Kiran,260
"""
    with open("/tmp/electricity.txt", "w") as f:
        f.write(data)

    print("electricity.txt created successfully.")


# ------------------------------------
# Task 2: Calculate Total and Average
# ------------------------------------
def calculate_total_units():
    total_units = 0
    customer_count = 0

    with open("/tmp/electricity.txt", "r") as f:
        for line in f:
            _, units = line.strip().split(",")
            total_units += int(units)
            customer_count += 1

    average_units = total_units / customer_count

    with open("/tmp/bill_data.txt", "w") as f:
        f.write(f"{customer_count},{total_units},{average_units}")

    print(f"Customers = {customer_count}")
    print(f"Total Units = {total_units}")
    print(f"Average Units = {average_units}")


# -----------------------------
# Task 3: Generate Summary
# -----------------------------
def generate_bill_summary():
    with open("/tmp/bill_data.txt", "r") as f:
        customers, total, average = f.read().split(",")

    with open("/tmp/bill_summary.txt", "w") as f:
        f.write("Electricity Bill Summary\n")
        f.write("========================\n")
        f.write(f"Customers = {customers}\n")
        f.write(f"Total Units = {total}\n")
        f.write(f"Average Units = {float(average):.2f}\n")

    print("Bill summary generated successfully.")

    with open("/tmp/bill_summary.txt", "r") as f:
        print(f.read())


# -----------------------------
# DAG Definition
# -----------------------------
with DAG(
    dag_id="exercise8_electricity_bill",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Electricity Bill Summary using Apache Airflow",
) as dag:

    create_bill_file_task = PythonOperator(
        task_id="create_bill_file",
        python_callable=create_bill_file,
    )

    calculate_total_units_task = PythonOperator(
        task_id="calculate_total_units",
        python_callable=calculate_total_units,
    )

    generate_bill_summary_task = PythonOperator(
        task_id="generate_bill_summary",
        python_callable=generate_bill_summary,
    )

    # Task Dependencies
    create_bill_file_task >> calculate_total_units_task >> generate_bill_summary_task

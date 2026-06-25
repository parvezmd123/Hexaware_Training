from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# -----------------------------------
# Task 1: Create Employee File
# -----------------------------------
def create_employee_file():
    data = """Rahul,28
Priya,31
Amit,42
Sneha,26
Kiran,38
"""

    with open("/tmp/employees.txt", "w") as f:
        f.write(data)

    print("employees.txt created successfully.")


# -----------------------------------
# Task 2: Calculate Employee Ages
# -----------------------------------
def calculate_average_age():
    ages = []

    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            name, age = line.strip().split(",")
            ages.append(int(age))

    youngest = min(ages)
    oldest = max(ages)
    average = sum(ages) / len(ages)

    with open("/tmp/age_data.txt", "w") as f:
        f.write(f"{youngest},{oldest},{average}")

    print(f"Youngest Age = {youngest}")
    print(f"Oldest Age = {oldest}")
    print(f"Average Age = {average:.2f}")


# -----------------------------------
# Task 3: Generate Age Report
# -----------------------------------
def generate_age_report():
    with open("/tmp/age_data.txt", "r") as f:
        youngest, oldest, average = f.read().split(",")

    with open("/tmp/age_report.txt", "w") as f:
        f.write("Employee Age Report\n")
        f.write("=====================\n")
        f.write(f"Youngest Age = {youngest}\n")
        f.write(f"Oldest Age = {oldest}\n")
        f.write(f"Average Age = {float(average):.2f}\n")

    print("Age report generated successfully.")

    with open("/tmp/age_report.txt", "r") as f:
        print(f.read())


# -----------------------------------
# DAG Definition
# -----------------------------------
with DAG(
    dag_id="exercise13_employee_age_report",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Employee Age Report using Apache Airflow",
) as dag:

    create_employee_file_task = PythonOperator(
        task_id="create_employee_file",
        python_callable=create_employee_file,
    )

    calculate_average_age_task = PythonOperator(
        task_id="calculate_average_age",
        python_callable=calculate_average_age,
    )

    generate_age_report_task = PythonOperator(
        task_id="generate_age_report",
        python_callable=generate_age_report,
    )

    # Task Dependencies
    create_employee_file_task >> calculate_average_age_task >> generate_age_report_task

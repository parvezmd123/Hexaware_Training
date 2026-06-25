from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# -----------------------------
# Task 1: Create Department File
# -----------------------------
def create_department_file():
    data = """IT,45000
HR,35000
Finance,50000
IT,55000
Finance,40000
HR,30000
"""
    with open("/tmp/departments.txt", "w") as f:
        f.write(data)

    print("departments.txt created successfully.")


# --------------------------------------
# Task 2: Calculate Department Salaries
# --------------------------------------
def calculate_department_salary():
    department_totals = {}

    with open("/tmp/departments.txt", "r") as f:
        for line in f:
            dept, salary = line.strip().split(",")
            salary = int(salary)

            if dept not in department_totals:
                department_totals[dept] = 0

            department_totals[dept] += salary

    with open("/tmp/department_totals.txt", "w") as f:
        for dept, total in department_totals.items():
            f.write(f"{dept},{total}\n")

    print("Department Salary Totals:")
    for dept, total in department_totals.items():
        print(f"{dept} = {total}")


# ---------------------------------
# Task 3: Generate Final Report
# ---------------------------------
def generate_department_report():
    with open("/tmp/department_totals.txt", "r") as infile, \
         open("/tmp/department_report.txt", "w") as outfile:

        outfile.write("Department Salary Report\n")
        outfile.write("========================\n")

        for line in infile:
            dept, total = line.strip().split(",")
            outfile.write(f"{dept} = {total}\n")

    print("Department report generated successfully.")

    with open("/tmp/department_report.txt", "r") as f:
        print(f.read())


# -----------------------------
# DAG Definition
# -----------------------------
with DAG(
    dag_id="exercise7_department_salary",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Department Salary Report using Apache Airflow",
) as dag:

    create_department_file_task = PythonOperator(
        task_id="create_department_file",
        python_callable=create_department_file,
    )

    calculate_department_salary_task = PythonOperator(
        task_id="calculate_department_salary",
        python_callable=calculate_department_salary,
    )

    generate_department_report_task = PythonOperator(
        task_id="generate_department_report",
        python_callable=generate_department_report,
    )

    # Task Dependencies
    create_department_file_task >> calculate_department_salary_task >> generate_department_report_task

from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="exercise2_salary_report",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
):

    @task
    def create_salary_file():
        with open("/tmp/employees.txt", "w") as f:
            f.write("""Rahul,45000
Priya,52000
Amit,61000
Sneha,48000""")

    @task
    def calculate_total_salary():
        total = 0

        with open("/tmp/employees.txt", "r") as f:
            for line in f:
                name, salary = line.strip().split(",")
                total += int(salary)

        print(f"Total Salary = {total}")
        return total

    @task
    def generate_report(total_salary):
        with open("/tmp/report.txt", "w") as f:
            f.write(
                f"""Salary Report
Employees = 4
Total Salary = {total_salary}"""
            )

        print("Report Generated Successfully")

    # Create Tasks
    create_file_task = create_salary_file()
    total_salary = calculate_total_salary()
    report_task = generate_report(total_salary)

    # Set Dependencies
    create_file_task >> total_salary >> report_task
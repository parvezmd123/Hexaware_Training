from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# -----------------------------------
# Task 1: Create Results File
# -----------------------------------
def create_result_file():
    data = """Rahul,Pass
Priya,Fail
Amit,Pass
Sneha,Pass
Kiran,Fail
Megha,Pass
"""

    with open("/tmp/results.txt", "w") as f:
        f.write(data)

    print("results.txt created successfully.")


# -----------------------------------
# Task 2: Count Pass and Fail
# -----------------------------------
def count_pass_fail():
    pass_count = 0
    fail_count = 0

    with open("/tmp/results.txt", "r") as f:
        for line in f:
            _, result = line.strip().split(",")

            if result == "Pass":
                pass_count += 1
            else:
                fail_count += 1

    with open("/tmp/result_counts.txt", "w") as f:
        f.write(f"{pass_count},{fail_count}")

    print(f"Total Pass = {pass_count}")
    print(f"Total Fail = {fail_count}")


# -----------------------------------
# Task 3: Generate Result Summary
# -----------------------------------
def generate_result_summary():
    with open("/tmp/result_counts.txt", "r") as f:
        pass_count, fail_count = f.read().split(",")

    with open("/tmp/result_summary.txt", "w") as f:
        f.write("Exam Result Summary\n")
        f.write("===================\n")
        f.write(f"Total Pass = {pass_count}\n")
        f.write(f"Total Fail = {fail_count}\n")

    print("Result summary generated successfully.")

    with open("/tmp/result_summary.txt", "r") as f:
        print(f.read())


# -----------------------------------
# DAG Definition
# -----------------------------------
with DAG(
    dag_id="exercise9_exam_result",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Exam Result Report using Apache Airflow",
) as dag:

    create_result_file_task = PythonOperator(
        task_id="create_result_file",
        python_callable=create_result_file,
    )

    count_pass_fail_task = PythonOperator(
        task_id="count_pass_fail",
        python_callable=count_pass_fail,
    )

    generate_result_summary_task = PythonOperator(
        task_id="generate_result_summary",
        python_callable=generate_result_summary,
    )

    # Task Dependencies
    create_result_file_task >> count_pass_fail_task >> generate_result_summary_task

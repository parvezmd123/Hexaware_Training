from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# -----------------------------------
# Task 1: Create Enrollment File
# -----------------------------------
def create_enrollment_file():
    data = """Python,Rahul
Python,Priya
SQL,Amit
Python,Sneha
Power BI,Kiran
SQL,Megha
Power BI,Arjun
"""

    with open("/tmp/enrollments.txt", "w") as f:
        f.write(data)

    print("enrollments.txt created successfully.")


# -----------------------------------
# Task 2: Count Students by Course
# -----------------------------------
def count_students():
    course_count = {}

    with open("/tmp/enrollments.txt", "r") as f:
        for line in f:
            course, student = line.strip().split(",")

            if course not in course_count:
                course_count[course] = 0

            course_count[course] += 1

    with open("/tmp/course_counts.txt", "w") as f:
        for course, count in course_count.items():
            f.write(f"{course},{count}\n")

    print("Course Enrollment Counts:")
    for course, count in course_count.items():
        print(f"{course} = {count}")


# -----------------------------------
# Task 3: Generate Course Report
# -----------------------------------
def generate_course_report():
    with open("/tmp/course_counts.txt", "r") as infile, \
         open("/tmp/course_report.txt", "w") as outfile:

        outfile.write("Course Enrollment Report\n")
        outfile.write("========================\n")

        for line in infile:
            course, count = line.strip().split(",")
            outfile.write(f"{course} = {count}\n")

    print("Course report generated successfully.")

    with open("/tmp/course_report.txt", "r") as f:
        print(f.read())


# -----------------------------------
# DAG Definition
# -----------------------------------
with DAG(
    dag_id="exercise14_course_enrollment_report",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Course Enrollment Report using Apache Airflow",
) as dag:

    create_enrollment_file_task = PythonOperator(
        task_id="create_enrollment_file",
        python_callable=create_enrollment_file,
    )

    count_students_task = PythonOperator(
        task_id="count_students",
        python_callable=count_students,
    )

    generate_course_report_task = PythonOperator(
        task_id="generate_course_report",
        python_callable=generate_course_report,
    )

    # Task Dependencies
    create_enrollment_file_task >> count_students_task >> generate_course_report_task

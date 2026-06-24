from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="exercise3_student_marks",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
):

    @task
    def create_marks_file():
        with open("/tmp/marks.txt", "w") as f:
            f.write("""Math,80
Science,75
English,90
Python,95""")

    @task
    def calculate_average():
        total = 0
        count = 0

        with open("/tmp/marks.txt", "r") as f:
            for line in f:
                subject, marks = line.strip().split(",")
                total += int(marks)
                count += 1

        average = total / count

        print(f"Average Marks = {average}")
        return average

    @task
    def generate_result(average):
        result = "PASS" if average >= 50 else "FAIL"

        with open("/tmp/result.txt", "w") as f:
            f.write(
                f"""Average Marks = {average}
Result = {result}"""
            )

        print(f"Result = {result}")

    # Create Tasks
    create_file_task = create_marks_file()
    average_task = calculate_average()
    result_task = generate_result(average_task)

    # Dependencies
    create_file_task >> average_task >> result_task
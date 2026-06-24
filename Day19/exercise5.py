from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="exercise5_attendance_report",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
):

    @task
    def create_attendance():
        with open("/tmp/attendance.txt", "w") as f:
            f.write("""Rahul,Present
Priya,Present
Amit,Absent
Sneha,Present
Kiran,Absent""")

    @task
    def count_present():
        present = 0

        with open("/tmp/attendance.txt", "r") as f:
            for line in f:
                name, status = line.strip().split(",")

                if status == "Present":
                    present += 1

        print(f"Present = {present}")
        return present

    @task
    def count_absent():
        absent = 0

        with open("/tmp/attendance.txt", "r") as f:
            for line in f:
                name, status = line.strip().split(",")

                if status == "Absent":
                    absent += 1

        print(f"Absent = {absent}")
        return absent

    @task
    def generate_summary(present, absent):
        total = present + absent

        with open("/tmp/attendance_report.txt", "w") as f:
            f.write(
                f"""Total Students = {total}
Present = {present}
Absent = {absent}"""
            )

    create_task = create_attendance()
    present_task = count_present()
    absent_task = count_absent()

    report_task = generate_summary(
        present_task,
        absent_task
    )

    create_task >> [present_task, absent_task]
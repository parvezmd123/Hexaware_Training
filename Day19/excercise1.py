from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="exercise1_file_read",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
):

    @task
    def create_file():
        with open("/tmp/message.txt", "w") as f:
            f.write("""Welcome to Apache Airflow
Learning DAGs
Learning Task Dependencies""")

    @task
    def read_file():
        with open("/tmp/message.txt", "r") as f:
            print(f.read())

    create_file() >> read_file()
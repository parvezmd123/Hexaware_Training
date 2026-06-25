from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# -----------------------------------
# Task 1: Create Temperature File
# -----------------------------------
def create_temperature_file():
    data = """Monday,34
Tuesday,36
Wednesday,31
Thursday,38
Friday,35
Saturday,33
Sunday,32
"""

    with open("/tmp/temperature.txt", "w") as f:
        f.write(data)

    print("temperature.txt created successfully.")


# -----------------------------------
# Task 2: Find Highest and Average Temperature
# -----------------------------------
def find_highest_temperature():
    temperatures = []

    with open("/tmp/temperature.txt", "r") as f:
        for line in f:
            day, temp = line.strip().split(",")
            temperatures.append(int(temp))

    highest = max(temperatures)
    average = sum(temperatures) / len(temperatures)

    with open("/tmp/weather_data.txt", "w") as f:
        f.write(f"{highest},{average}")

    print(f"Highest Temperature = {highest}")
    print(f"Average Temperature = {average:.2f}")


# -----------------------------------
# Task 3: Generate Weather Report
# -----------------------------------
def generate_weather_report():
    with open("/tmp/weather_data.txt", "r") as f:
        highest, average = f.read().split(",")

    with open("/tmp/weather_report.txt", "w") as f:
        f.write("Weather Report\n")
        f.write("====================\n")
        f.write(f"Highest Temperature = {highest}\n")
        f.write(f"Average Temperature = {float(average):.2f}\n")

    print("Weather report generated successfully.")

    with open("/tmp/weather_report.txt", "r") as f:
        print(f.read())


# -----------------------------------
# DAG Definition
# -----------------------------------
with DAG(
    dag_id="exercise11_temperature_analysis",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Temperature Analysis using Apache Airflow",
) as dag:

    create_temperature_file_task = PythonOperator(
        task_id="create_temperature_file",
        python_callable=create_temperature_file,
    )

    find_highest_temperature_task = PythonOperator(
        task_id="find_highest_temperature",
        python_callable=find_highest_temperature,
    )

    generate_weather_report_task = PythonOperator(
        task_id="generate_weather_report",
        python_callable=generate_weather_report,
    )

    # Task Dependencies
    create_temperature_file_task >> find_highest_temperature_task >> generate_weather_report_task

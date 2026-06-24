from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import csv

with DAG(
    dag_id="exercise6_csv_processing",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
):

    @task
    def create_csv():
        with open("/tmp/sales.csv", "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow(["product", "quantity", "price"])
            writer.writerow(["Laptop", 2, 70000])
            writer.writerow(["Mouse", 5, 500])
            writer.writerow(["Keyboard", 3, 1200])

    @task
    def read_csv():
        data = []

        with open("/tmp/sales.csv", "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                data.append(row)

        return data

    @task
    def calculate_revenue(data):
        revenue_data = []
        total_revenue = 0

        for row in data:
            revenue = int(row["quantity"]) * int(row["price"])

            revenue_data.append(
                {
                    "product": row["product"],
                    "revenue": revenue
                }
            )

            total_revenue += revenue

        return {
            "revenues": revenue_data,
            "total": total_revenue
        }

    @task
    def create_summary(result):
        with open("/tmp/sales_summary.txt", "w") as f:

            for item in result["revenues"]:
                f.write(
                    f"{item['product']} = {item['revenue']}\n"
                )

            f.write(
                f"\nTotal Revenue = {result['total']}"
            )

    csv_task = create_csv()
    data_task = read_csv()
    revenue_task = calculate_revenue(data_task)

    summary_task = create_summary(revenue_task)

    csv_task >> data_task >> revenue_task >> summary_task
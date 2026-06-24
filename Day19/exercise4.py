from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="exercise4_stock_alert",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
):

    @task
    def create_inventory():
        with open("/tmp/inventory.txt", "w") as f:
            f.write("""Rice,50
Oil,7
Soap,35
Sugar,10
Tea,5""")

    @task
    def find_low_stock():
        low_stock = []

        with open("/tmp/inventory.txt", "r") as f:
            for line in f:
                product, qty = line.strip().split(",")

                if int(qty) < 15:
                    low_stock.append(product)

        print(low_stock)
        return low_stock

    @task
    def generate_alert(products):
        with open("/tmp/alerts.txt", "w") as f:
            for item in products:
                f.write(item + "\n")

    create_task = create_inventory()
    stock_task = find_low_stock()
    alert_task = generate_alert(stock_task)

    create_task >> stock_task >> alert_task
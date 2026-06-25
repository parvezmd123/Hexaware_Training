from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# -----------------------------------
# Task 1: Create Transactions File
# -----------------------------------
def create_transactions():
    data = """Deposit,10000
Withdraw,2500
Deposit,4000
Withdraw,1500
Deposit,2000
"""

    with open("/tmp/transactions.txt", "w") as f:
        f.write(data)

    print("transactions.txt created successfully.")


# -----------------------------------
# Task 2: Calculate Balance
# -----------------------------------
def calculate_balance():
    total_deposit = 0
    total_withdrawal = 0

    with open("/tmp/transactions.txt", "r") as f:
        for line in f:
            transaction_type, amount = line.strip().split(",")
            amount = int(amount)

            if transaction_type == "Deposit":
                total_deposit += amount
            elif transaction_type == "Withdraw":
                total_withdrawal += amount

    final_balance = total_deposit - total_withdrawal

    with open("/tmp/account_data.txt", "w") as f:
        f.write(f"{total_deposit},{total_withdrawal},{final_balance}")

    print(f"Total Deposit = {total_deposit}")
    print(f"Total Withdrawal = {total_withdrawal}")
    print(f"Final Balance = {final_balance}")


# -----------------------------------
# Task 3: Generate Account Report
# -----------------------------------
def generate_account_report():
    with open("/tmp/account_data.txt", "r") as f:
        deposit, withdrawal, balance = f.read().split(",")

    with open("/tmp/account_report.txt", "w") as f:
        f.write("Bank Transaction Summary\n")
        f.write("========================\n")
        f.write(f"Total Deposit = {deposit}\n")
        f.write(f"Total Withdrawal = {withdrawal}\n")
        f.write(f"Final Balance = {balance}\n")

    print("Account report generated successfully.")

    with open("/tmp/account_report.txt", "r") as f:
        print(f.read())


# -----------------------------------
# DAG Definition
# -----------------------------------
with DAG(
    dag_id="exercise12_bank_transaction_summary",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Bank Transaction Summary using Apache Airflow",
) as dag:

    create_transactions_task = PythonOperator(
        task_id="create_transactions",
        python_callable=create_transactions,
    )

    calculate_balance_task = PythonOperator(
        task_id="calculate_balance",
        python_callable=calculate_balance,
    )

    generate_account_report_task = PythonOperator(
        task_id="generate_account_report",
        python_callable=generate_account_report,
    )

    # Task Dependencies
    create_transactions_task >> calculate_balance_task >> generate_account_report_task

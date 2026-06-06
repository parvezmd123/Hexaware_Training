import csv
import numpy as np
import pandas as pd
from collections import defaultdict,Counter

FILE_NAME="orders.csv"
orders=[]
try:
    with open("orders.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            try:
                row["quantity"] = int(row["quantity"])
                row["price"] = float(row["price"])

                row["revenue"] = row["quantity"] * row["price"]

                orders.append(row)

            except ValueError:
                print("Invalid quantity or price:", row)

except FileNotFoundError:
    print("orders.csv file not found!")

print("\nAll Orders")

for order in orders:
    print(order)

#Task 2
print("\nAll Records")
for order in orders:
    print(order)

#Task 3
print("\nTotal Orders:",len(orders))

#Task 4
total_revenue=sum(order["revenue"]for order in orders)
print("\nTotal Revenue:",total_revenue)

#Task 5
highest_order=max(order["revenue"] for order in orders)
print("\nhighest_order:",highest_order)

#Task 6
lowest_order=min(order["revenue"] for order in orders)
print("\nlowest_order:",lowest_order)

#Task 7
average_order=total_revenue / len(orders)
print("\nAverage Revenue:",average_order)

#Task 8
customers= set(order["customer_name"] for order in orders)

print("\nUnique Customers")
for customer in customers:
    print(customer)

#Task 9
print("\nUnique Customer Count:",len(customers))

#Task 10
customer_purchase=defaultdict(float)

for order in orders:
    customer_purchase[order["customer_name"]] += order["revenue"]

top_customer=max(customer_purchase, key=customer_purchase.get)

print("\nCustomer with highest purchase amount")
print(top_customer,customer_purchase[top_customer])

#Task 11
product_orders = Counter(order["product"] for order in orders)

print("\nOrders By Product")
print(dict(product_orders))

#Task 12
product_revenue = defaultdict(float)

for order in orders:
    product_revenue[order["product"]] += order["revenue"]

print("\nRevenue By Product")
print(dict(product_revenue))

#Task 13

product_quantity = defaultdict(int)

for order in orders:
    product_quantity[order["product"]] += order["quantity"]

most_sold = max(product_quantity, key=product_quantity.get)

print("\nMost Sold Product:")
print(most_sold, product_quantity[most_sold])

#Task 14
least_sold=min(product_quantity,key=product_quantity.get)

print("\nLeast Sold Product:")
print(least_sold, product_quantity[least_sold])

#Task 15
category_revenue = defaultdict(float)

for order in orders:
    category_revenue[order["category"]] += order["revenue"]

print("\nRevenue By Category")
print(dict(category_revenue))

#Task 16
city_orders = Counter(order["city"] for order in orders)

print("\nOrders By City")
print(dict(city_orders))

#Task 17
city_revenue = defaultdict(float)

for order in orders:
    city_revenue[order["city"]] += order["revenue"]

print("\nRevenue By City")
print(dict(city_revenue))

#Task 18
top_city = max(city_revenue, key=city_revenue.get)

print("\nHighest Revenue City")
print(top_city, city_revenue[top_city])

#Task 19
products = sorted([order["product"] for order in orders])

print("\nSorted Product List")
print(products)

#Task 20
cities = set(order["city"] for order in orders)

print("\nUnique Cities")
print(cities)

#Task 21
city_revenue_dict = dict(city_revenue)

print("\nCity Revenue Dictionary")
print(city_revenue_dict)

#Task 22
product_quantity_dict = dict(product_quantity)

print("\nProduct Quantity Dictionary")
print(product_quantity_dict)

#Task 23
def calculate_total_revenue():
    return sum(order["revenue"] for order in orders)

#Task 24
def find_top_product():
    return max(product_quantity, key=product_quantity.get)

#Task 25
def find_top_city():
    return max(city_revenue, key=city_revenue.get)

#Task 26
def find_average_order_value():
    return calculate_total_revenue() / len(orders)

print("\nFunction Outputs")
print(calculate_total_revenue())
print(find_top_product())
print(find_top_city())
print(find_average_order_value())

#Task 30
order_values = np.array([order["revenue"] for order in orders])

print("\nNumPy Analysis")
print("Total Revenue:", np.sum(order_values))
print("Average Revenue:", np.mean(order_values))
print("Maximum Revenue:", np.max(order_values))
print("Minimum Revenue:", np.min(order_values))
print("Standard Deviation:", np.std(order_values))

#Task 31
df = pd.read_csv(FILE_NAME)

#Task 32
df["Revenue"] = df["quantity"] * df["price"]

#Task 33
print("\nTop 5 Highest Value Orders")
print(df.nlargest(5, "Revenue"))

#Task 34
print("\nRevenue By City")
print(df.groupby("city")["Revenue"].sum())

#Task 35
print("\nRevenue By Product")
print(df.groupby("product")["Revenue"].sum())

#Task 36
print("\nTop Selling Products")
print(df.groupby("product")["quantity"].sum().sort_values(ascending=False))

#Task 37
print("\nCity Wise Order Count")
print(df.groupby("city")["order_id"].count())

#Report Generation
with open("sales_summary_report.txt", "w") as report:

    report.write("SALES SUMMARY REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Total Orders : {len(orders)}\n")
    report.write(f"Total Revenue : {total_revenue}\n")
    report.write(f"Average Order Value : {average_order}\n")
    report.write(f"Highest Order Value : {highest_order}\n")
    report.write(f"Lowest Order Value : {lowest_order}\n\n")

    report.write("Revenue By City\n")
    report.write(str(dict(city_revenue)) + "\n\n")

    report.write("Revenue By Category\n")
    report.write(str(dict(category_revenue)) + "\n\n")

    report.write(f"Top Selling Product : {most_sold}\n")
    report.write(f"Top Revenue City : {top_city}\n")

print("\nReport Generated Successfully")

#Task 38
high_value = df[df["Revenue"] > 50000]
high_value.to_csv("high_value_orders.csv", index=False)

# Task 39
electronics = df[df["category"] == "Electronics"]
electronics.to_csv("electronics_orders.csv", index=False)

print("CSV Files Exported Successfully")

# Task 40
def menu():
    while True:

        print("\n===== SALES ANALYSIS MENU =====")
        print("1. View Orders")
        print("2. Revenue Analysis")
        print("3. Product Analysis")
        print("4. City Analysis")
        print("5. Export Reports")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            print(df)

        elif choice == "2":
            print("Total Revenue:", total_revenue)

        elif choice == "3":
            print(dict(product_revenue))

        elif choice == "4":
            print(dict(city_revenue))

        elif choice == "5":
            print("Reports Already Generated")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid Choice")

menu()

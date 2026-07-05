import pandas as pd

print("Loading Products Dataset...")
products = pd.read_csv("products.csv")

print("Loading Sales Dataset...")
sales = pd.read_csv("sales.csv")

print("Joining Datasets...")
df = pd.merge(sales, products, on="product_id")

print("Calculating Summary...")

summary = df.groupby("store_name").agg(
    Total_Revenue=("revenue", "sum"),
    Total_Profit=("profit", "sum")
).reset_index()

summary.to_csv("final_metrics.csv", index=False)

print("Finding Lowest Performing Stores...")

lowest = summary.sort_values("Total_Profit").head(5)

lowest.to_csv("lowest_performing_stores.csv", index=False)

print("\n===== Store Performance =====")
print(summary)

print("\n===== Lowest Performing Stores =====")
print(lowest)

print("\nPipeline Completed Successfully.")

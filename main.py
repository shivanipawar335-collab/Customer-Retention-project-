import pandas as pd
import matplotlib.pyplot as plt

# Load data
orders = pd.read_csv("olist_orders_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")

# Merge data
df = orders.merge(customers, on="customer_id", how="left")

# Count orders for each customer
customer_orders = df.groupby("customer_unique_id")["order_id"].count()

# Calculate customer numbers
repeat_customers = (customer_orders > 1).sum()
one_time_customers = (customer_orders == 1).sum()
total_customers = len(customer_orders)

# Calculate retention rate
retention_rate = (
    repeat_customers / total_customers * 100
    if total_customers > 0 else 0
)

# Show results
print("CUSTOMER RETENTION ANALYSIS")
print("Total Customers:", total_customers)
print("Repeat Customers:", repeat_customers)
print("One-Time Customers:", one_time_customers)
print("Retention Rate:", round(retention_rate, 2), "%")

# Pie Chart
labels = ["Repeat Customers", "One-Time Customers"]
values = [repeat_customers, one_time_customers]

plt.figure()
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Customer Retention Analysis")
plt.savefig("customer_retention_pie.png")
plt.show()

# Bar Chart
plt.figure()
plt.bar(labels, values)
plt.title("Repeat vs One-Time Customers")
plt.xlabel("Customer Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customer_retention_bar.png")
plt.show()

# Final result
print("\nProject Completed Successfully!")
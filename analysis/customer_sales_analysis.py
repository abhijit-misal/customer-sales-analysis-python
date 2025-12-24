import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/customer_sales.csv')

# Basic data cleaning
df.drop_duplicates(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

# Create revenue column
df['Revenue'] = df['Quantity'] * df['Price']

# 1. Total revenue
print("Total Revenue:", df['Revenue'].sum())

# 2. Revenue by product
product_revenue = df.groupby('Product')['Revenue'].sum()
print("\nRevenue by Product:")
print(product_revenue)

# 3. Revenue by region
region_revenue = df.groupby('Region')['Revenue'].sum()
print("\nRevenue by Region:")
print(region_revenue)

# 4. Top customers
top_customers = df.groupby('Customer')['Revenue'].sum().sort_values(ascending=False)
print("\nTop Customers:")
print(top_customers)

# Visualization
product_revenue.plot(kind='bar', title='Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

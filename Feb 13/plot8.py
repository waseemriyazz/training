import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
file = pd.read_csv("Feb 13/company_sales_data.csv")

# Calculating the total units for each product
total_units_per_product = file.iloc[:, 1:7].sum()

# Calculating the percentage of total units for each product
percentage_per_product = (total_units_per_product / total_units_per_product.sum()) * 100

# Plotting the Pie chart
plt.figure(figsize=(10, 8))
plt.pie(percentage_per_product, labels=percentage_per_product.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Percentage of Total Units Sold for Each Product Over One Year')

# Show the plot
plt.show()
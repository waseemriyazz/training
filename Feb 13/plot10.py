import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
file = pd.read_csv("Feb 13/company_sales_data.csv")

# Extracting data for all products
months = file['month_number']
facecream_sales = file['facecream']
facewash_sales = file['facewash']
toothpaste_sales = file['toothpaste']
bathingsoap_sales = file['bathingsoap']
shampoo_sales = file['shampoo']
moisturizer_sales = file['moisturizer']

# Creating a stack plot
plt.figure(figsize=(10, 6))
plt.stackplot(months, facecream_sales, facewash_sales, toothpaste_sales, bathingsoap_sales, shampoo_sales, moisturizer_sales, labels=['Facecream', 'Facewash', 'Toothpaste', 'Bathingsoap', 'Shampoo', 'Moisturizer'])
plt.title('Product Sales Over the Months')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.legend(loc='upper left')

# Show the stack plot
plt.show()
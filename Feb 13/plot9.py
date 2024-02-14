import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
file = pd.read_csv("Feb 13/company_sales_data.csv")

# Extracting data for Bathing soap and Facewash
bathing_soap_data = file['bathingsoap']
facewash_data = file['facewash']

# Creating subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plotting Bathing soap data
axs[0].plot(file['month_number'], bathing_soap_data, marker='o', color='b', label='Bathing Soap')
axs[0].set_title('Bathing Soap Sales Over the Year')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Units Sold')
axs[0].legend()

# Plotting Facewash data
axs[1].plot(file['month_number'], facewash_data, marker='o', color='r', label='Facewash')
axs[1].set_title('Facewash Sales Over the Year')
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Units Sold')
axs[1].legend()

# Adjusting layout for better visualization
plt.tight_layout()

# Show the subplots
plt.show()
import pandas as pd 

import matplotlib.pyplot as plt


file = pd.read_csv("Feb 13/company_sales_data.csv")

plt.scatter(
    file['month_number'],
    file['toothpaste'],
    label = 'toothpaste sales data',
    
)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
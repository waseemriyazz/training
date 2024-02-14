import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("Feb 13/company_sales_data.csv")

plt.hist(
    file['total_profit'],
    bins=10,
    label='Total profit'
    
)


plt.legend()
plt.show()
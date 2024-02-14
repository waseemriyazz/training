import pandas as pd 

import matplotlib.pyplot as plt


file = pd.read_csv("Feb 13/company_sales_data.csv")

plt.plot(file['month_number'], file['total_profit'])
plt.title('Company profit per month')
plt.xlabel('Month number')
plt.ylabel('Total profit in dollars')
plt.legend()
plt.show()
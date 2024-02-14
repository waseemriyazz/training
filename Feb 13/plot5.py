import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv("Feb 13/company_sales_data.csv")


bar_width = 0.35

bar_positions1 = file['month_number']
bar_positions2 = bar_positions1 + bar_width


plt.bar(
    bar_positions1,
    file['facecream'], 
    width=bar_width, 
    label='Face Cream Sales'
    )


plt.bar(
    bar_positions2, 
    file['facewash'], 
    width=bar_width, 
    label='Face Wash Sales'
    )

plt.grid(True, linestyle='--', linewidth=0.5)

plt.title('Monthly Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Quantity')
plt.xticks(bar_positions1 + bar_width / 2, file['month_number'])  # Center x-ticks between the bars
plt.legend()


plt.show()

import pandas as pd 

import matplotlib.pyplot as plt


file = pd.read_csv("Feb 13/company_sales_data.csv")
plt.plot(
    file['month_number'],
    file['facecream'], 
    label = 'face cream sales data',
    marker = 'o',
    linewidth=3
    
)
plt.plot(
    file['month_number'],
    file['facewash'],
    label = 'face wash sales data',
    marker = 'o',
    linewidth=3
    
)
plt.plot(
    file['month_number'],
    file['toothpaste'],
    label = 'toothpaste sales data',
    marker = 'o',
    linewidth=3
    
)
plt.plot(
    file['month_number'],
    file['bathingsoap'],
    label = 'bathing soap sales data',
    marker = 'o',
    linewidth=3
    
)
plt.plot(
    file['month_number'],
    file['shampoo'],
    label = 'shampoo sales data',
    marker = 'o',
    linewidth=3
    
)
plt.plot(
    file['month_number'],
    file['moisturizer'],
    label = 'moisturizer sales data',
    marker = 'o',
    linewidth=3
    
)









plt.title('Sales data')
plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.legend()
plt.show()
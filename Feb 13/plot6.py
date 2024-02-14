import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file = pd.read_csv("Feb 13/company_sales_data.csv")

plt.bar(
    file['month_number'],
    file['bathingsoap'], 
    label='Face Cream Sales'
    )

plt.grid( linestyle = '--')
# Set x-ticks to start from 1 and continue sequentially up to 12
plt.xticks(np.arange(1, 13))

plt.show()

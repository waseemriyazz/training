# Import statements go here

import pandas as pd
import statsmodels.api as sm
import numpy as np

anes96 = sm.datasets.anes96


dataset_anes96 = anes96.load_pandas()
df = dataset_anes96.data
if __name__ =="__main__":
    print("Script run")
    print(anes96.NOTE)
    print(df)
    print(df.head(8))
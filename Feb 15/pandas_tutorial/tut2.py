import pandas as pd 
titanic = pd.read_csv("Feb 15/pandas_tutorial/titanic.csv")
print(titanic) #prints data in the csv file
print(titanic.head(8)) #prints 1st 8 rows of the csv file
print(titanic.dtypes) #prints data types of each coloumn
print(titanic.info()) #prints technical summary of the dataframe
"""
REMEMBER
Getting data in to pandas from many different file formats or data sources is supported by read_* functions.

Exporting data out of pandas is provided by different to_*methods.

The head/tail/info methods and the dtypes attribute are convenient for a first check.

"""
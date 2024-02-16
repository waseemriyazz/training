import pandas as pd 
titanic = pd.read_csv("Feb 15/pandas_tutorial/titanic.csv")
ages = titanic["Age"]

# print(f"printing the head of ages \n{ages.head()}")
# print(f"printing the type of ages {type(ages)}")
# print(f"printing the shape of ages {ages.shape}")

# age_sex = titanic[["Age", "Sex"]]
# print(age_sex.head())
# # How do I filter specific rows from a DataFrame?
# above_35 = titanic[titanic["Age"] > 35]

# print(above_35.head())

# print(titanic ["Age"] > 35)

# class_23 = titanic [ titanic["Pclass"].isin([2,3]) ]
# print(class_23)
# age_no_na = titanic[titanic["Age"].notna()]
# print(age_no_na)

# adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
# print(adult_names)
"""In this case, a subset of both rows and columns is made in one go and just using
 selection brackets [] is not sufficient anymore. The loc/iloc operators are required in 
 front of the selection brackets []. When using loc/iloc, the part before the comma is the 
 rows you want, and the part after the comma is the columns you want to select."""

print(titanic.head())
titanic.iloc[0:3, 3] = "anonymous"
print(titanic["Name"])

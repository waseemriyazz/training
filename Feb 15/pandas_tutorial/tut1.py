import pandas as pd 
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)


print(df)
print(df["Age"])
ages = pd.Series([12, 15, 50], name="Ages")

print(ages)
print(df["Age"].max())
print(ages.max())

print(df.describe())

"""
REMEMBER
Import the package, aka import pandas as pd

A table of data is stored as a pandas DataFrame

Each column in a DataFrame is a Series

You can do things by applying a method to a DataFrame or Series
"""
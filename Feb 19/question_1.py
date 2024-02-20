
# Q1DataFrame Basic Properties Exercise
# Our DataFrame (df) contains data on registered voters in the United States, including demographic information and political preference.
# Using pandas, print the first 5 rows of the DataFrame to get a sense of what the data looks like. Next, answer the following questions:






from data_frame import df
import numpy as np
# How many observations are in the DataFrame?
# How many variables are measured (how many columns)?

print(df.head(16)) # 944 observations(rows) and 12 columns

# What is the age of the youngest person in the data? The oldest?

sorted= df.sort_values(by="age")
print(sorted)
print(f"oldest {sorted.iloc[-1:, ]["age"]}")
print("  \n")
print(f"youngest {sorted.iloc[0:1, ]["age"]}")

# How many days a week does the average respondent watch TV news (round to the nearest tenth)?
tv = np.array(df["TVnews"])
print(np.median(tv))

# Check for missing values. Are there any?

print(df.isnull().any().any())





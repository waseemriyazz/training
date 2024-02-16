import pandas as pd

# Load the dataset
file_path = 'Feb 15/la_jobs.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Find all values from the first cell of rows where 'EXPERIENCE_LENGTH' is '-'
values_to_return = df.loc[df['EXPERIENCE_LENGTH'] == '-', :].iloc[:, 0]

# Display the values to return
print(values_to_return)
answer = df[df["JOB_CLASS_NO"] > 9205]
answer.head()


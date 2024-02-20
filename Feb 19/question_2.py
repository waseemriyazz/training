# Q2Data Processing Exercise
# We want to adjust the dataset for our use. Do the following:





# Rename the educ column education.
from data_frame import df
# print(df.head(1))
# df = df.rename(columns={"educ":"education"})
# print(df.head(1))

# Create a new column called party based on each respondent's answer to PID. party should equal Democrat if the respondent selected either Strong Democrat or Weak Democrat. party will equal Republican if the respondent selected Strong or Weak Republican for PID and Independent if they selected anything else.

def get_party(df):
  """
    returns respondent's political party based on PID
  """

  if df['PID'] < 2:
    return "Democrat"
  elif df['PID'] > 4:
    return "Republican"
  else:
    return "Independent"

# Apply the function to the df and save to a new column 'party.'
df['party'] = df.apply(get_party, axis = 1)

print(df)

# Create a new column called age_group that buckets respondents into the following categories based on their age: 18-24, 25-34, 35-44, 45-54, 55-64, and 65 and over.

def get_agegroup(df):
  """
    returns age bracket string dependent on respondent's exact age (integer)
  """

  if df['age'] < 25:
    return "18-24"
  elif df['age'] < 35:
    return "25-34"
  elif df['age'] < 45:
    return "35-44"
  elif df['age'] < 55:
    return "45-54"
  elif df['age'] < 65:
    return "55-64"
  else:
    return "65 and over"
  
df["age_group"] = df.apply(get_agegroup, axis=1)
print(df)
from question_2 import df
avg_by_age = df.groupby(["age_group"]).mean()

# print mean values of each age group for selected columns and sort accordingly
print(avg_by_age['selfLR'].sort_values(ascending = False))
print(avg_by_age['TVnews'].sort_values(ascending = True))
income_quants = list(df['income'].quantile(q=[0.2, 0.4, 0.6, 0.8, 1]))

def get_income_quant(df):
  """
    Return quantile group based on respondent income.
  """

  if df['income'] <= income_quants[0]:
    return "Q1"
  elif df['income'] <= income_quants[1]:
    return "Q2"
  elif df['income'] <= income_quants[2]:
    return "Q3"
  elif df["income"] <= income_quants[3]:
    return "Q4"
  else:
    return "Q5"

# Apply it to the df and make a new column
df['income_quant'] = df.apply(get_income_quant, axis=1)
print(df)

# avg_by_incomequant = df.groupby(["income_quant"]).mean()
# print(avg_by_incomequant)
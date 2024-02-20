# 4. Calculating From Data Exercise
# For each of the below match-ups, choose the group that is more likely to vote for Bill Clinton. You can calculate this using the percentage of each group that intends to vote for Clinton (vote).

# Another way to think about this: Given that a respondent is a Democrat, there is a ____ percent chance they will vote for Clinton. How does this value change if the respondent is a Republican?

# Which match-up was the closest? Which had the biggest difference?

# Democrats or Republicans
# People younger than 44 or People 44 and older
# People who watch TV news at least 6 days a week or People who watch TV news less than 3 days a week
# People who live somewhere with a population greater than the average respondent or People who live in a place with a population equal to or less than the average respondent
from question_3 import df
import numpy as np
df['younger44'] = np.where(df['age'] < 44, True, False)

# TV news at least 6 days a week vs. TV news less than 3 days a week
def get_TVnews(df):
  """
    returns categorical value based on how much respondent watches TV news weekly
  """

  if df['TVnews'] > 5:
    return ">5"
  if df['TVnews'] < 3:
    return "<3"
  else:
    return "3-5"

df['TVnews_category'] = df.apply(get_TVnews, axis = 1)

# Live somewhere with population larger than the average respondent vs Population <= average
avg_population = df.popul.mean()
df['popul_greater'] = np.where(df['popul'] > avg_population, True, False)
def match_ups(Column, ConditionA, ConditionB):
  """
    Evaluates two groups and determines which one has a higher proportion of Clinton voters.

    Column: column in 'df' to reference
    ConditionA: group 1 to filter on
    ConditionB: group 2 to filter on
  """

  all_A = df[(df[Column] == ConditionA)]
  clinton_A = all_A[(all_A['vote'] == 0)]
  percent_A = (len(clinton_A) / len(all_A)) * 100

  all_B = df[(df[Column] == ConditionB)]
  clinton_B = all_B[(all_B['vote'] == 0)]
  percent_B = (len(clinton_B) / len(all_B)) * 100

  print(f"{ConditionA} = {percent_A:.2f}%")
  print(f"{ConditionB} = {percent_B:.2f}%")
  print(f"Difference ({ConditionA} minus {ConditionB}) = {percent_A - percent_B:.2f} percent points.")

  print("Democrats vs Republicans")
match_ups("party", "Democrat", "Republican")

print("\nYounger than 44 (True) vs 44 and Older (False)")
match_ups("younger44", True, False)

print("\nWatch TV news 6+ days a week (>5) vs Watch TV news less than 3 days a week (<3)")
match_ups("TVnews_category", ">5", "<3")

print("\nLive somewhere more populous than the average respondent (True) vs Live somewhere less populous (False")
match_ups("popul_greater", True, False)
from question_4 import df
def make_sway(df):
  """
    return difference between respondent's Left/Right leaning and their impression of their \
    intended candidate's Left/Right leaning.
  """

  # If the respondent plans to vote for Clinton
  if df['vote'] == 0:
    # Calculate the difference between respondent's view and their impression of Clinton's views.
    return df['selfLR'] - df['ClinLR']
  
  # If the respondent plans to vote for Dole
  else:
    # Calculate difference between respondent's view and their impression of Dole's views.
    return df['selfLR'] - df['DoleLR']

# In the resulting column, a negative value means the respondent views their chosen candidate as more "Left" than them.
# A positive value inidicates the respondent sees their candidate as more "Right" than them.
df['sway_diff'] = df.apply(make_sway, axis=1)

# Sort by absolute value to see the largest difference in either direction
df.sort_values(by='sway_diff', ascending=False, key=abs)

sway = df[df['sway_diff'].abs() >= 3]

# We could look at the averages to interpret this df.
print(sway.describe())

# Or we could count how many people fall in each category.
print("\nAmong the people with the largest `sway_diff`:")
print(f"{len(sway[sway['sway_diff'] > 0])} respondents perceive their candidate as more conservative than them.")
print(f"{len(sway[sway['sway_diff'] < 0])} respondents perceive their candidate as more liberal than them.")
print(f"{len(sway[sway['vote'] == 0])} respondents are voting for Clinton.")
print(f"{len(sway[sway['vote'] == 1])} respondents are voting for Dole.")


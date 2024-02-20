# Q3. Filtering Data Exercise
# Use the filtering method to find all the respondents who have the impression that Bill Clinton is moderate or conservative (ClinLR equals 4 or higher). How many respondents are in this subset?

# # Among these respondents, how many have a household income less than $50,000 and attended at least some college?
from question_2 import df
ClModRep = df[df['ClinLR'] >= 4]

print(f"{len(ClModRep)} respondents have the impression that Bill Clinton is moderate or conservative.")

ClModRep_filtered = ClModRep[(ClModRep['income'] < 20) & (ClModRep['educ'] > 3)]
print(f"Among the {len(ClModRep)} respondents have the impression that Bill Clinton is moderate or conservative, {len(ClModRep_filtered)} ({len(ClModRep_filtered)/len(ClModRep):.2f}%) earn less than $50,000 and attended at least some college.")
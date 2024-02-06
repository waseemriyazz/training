# 10.[stocks.csv]contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file
# with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# ```
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# ```


# Your input format (stocks.csv) is,

# |Company Name|Price|Earnings Per Share|Book Value|
# |-------|----------|-------|----------|
# |Reliance|1467|66|653|
# |Tata Steel|391|89|572|

# Output.csv should look like this,

# |Company Name|PE Ratio|PB Ratio|
# |-------|----------|-------|
# |Reliance|22.23|2.25|
# |Tata Steel|4.39|0.68|

import pandas as pd
csv_file_name='Feb 5/assigment 2/stocks.csv'
df=pd.read_csv(csv_file_name)
df['PE Ratio']=df['Price']/df['Earnings Per Share']
df['Price to Book Ratio']=df['Price']/df['Book Value']
output_df = df[['Company Name', 'PE Ratio', 'Price to Book Ratio']]
file_name='Output.csv'
output_df.to_csv(file_name,index=False)
output_df=output_df.drop_duplicates()
output_df=output_df.dropna
print(output_df)
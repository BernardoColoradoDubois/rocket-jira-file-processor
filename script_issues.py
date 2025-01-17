import json
import pandas as pd
from src.lib.parsers.issues import issue_parser

file = open('./files/issues/2024_11_15_1731635738755_202411320', 'r')

table = []

for line in file:
  # Procesa cada línea aquí

  data = json.loads(line)
  
  cleaned_data = issue_parser(data)
  
  print(cleaned_data)
  table.append(cleaned_data)

file.close()

df = pd.DataFrame.from_dict(table)

print(df.dtypes)

df.to_csv('./csv/issues_sample.csv', index=False)
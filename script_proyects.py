import json
import pandas as pd
from src.lib.parsers.projects import project_parser

file = open('./files/projects/2024_11_15_1731635738755_202411320', 'r')

table = []

for line in file:
  # Procesa cada línea aquí

  data = json.loads(line)
  
  cleaned_data = project_parser(data)
  
  print(cleaned_data)
  table.append(cleaned_data)

file.close()

df = pd.DataFrame.from_dict(table)

df.to_csv('./csv/projects_sample.csv', index=False)
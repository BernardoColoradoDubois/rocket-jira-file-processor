import json
import pandas as pd
from src.lib.parsers.issues import issue_parser

file = open('./files/issues/issues_sample', 'r')

table = []

for line in file:
  # Procesa cada línea aquí

  data = json.loads(line)
  
  cleaned_data = issue_parser(data)
  
  print(cleaned_data)
  table.append(cleaned_data)
  

  
file.close()

df = pd.DataFrame(table)

df.to_csv('issues_sample.csv', index=False)
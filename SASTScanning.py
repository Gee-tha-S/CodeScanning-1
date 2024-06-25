
import pandas as pd
from pandas import json_normalize
import json
 
# Load the JSON file
json_file_path = 'code_scanning_alerts.json'
with open(json_file_path, 'r') as f:
    data = json.load(f)
 
# Normalize the nested JSON
df = json_normalize(data)

# Define new data for additional columns


#print(df)
##############################################################################
# Convert the DataFrame to a CSV file
csv_file_path = 'code-scanning.csv'
df.to_csv(csv_file_path, index=False)
 
print(f"Nested JSON file has been converted to CSV file at: {csv_file_path}")

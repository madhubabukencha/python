# Pandas is a 3rd party library so,
# To install: pip install pandas
import pandas as pd
import json

# Lets assume data present in sample.json file
# Loading json data data into python
with open("sample.json", "r") as json_data:
    python_data = json.load(json_data)

indicators = python_data['indicators']
ind_dataframe = pd.DataFrame(indicators)
# Sorting all rows with type as "URL"
# and then fetching all values data
print(ind_dataframe[ind_dataframe['type'].str.contains("URL")]['value'])



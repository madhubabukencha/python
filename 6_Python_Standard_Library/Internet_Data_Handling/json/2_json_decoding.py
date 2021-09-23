"""
Author      : Madhu Babu Kencha
created on  : 15-Nov-2018

Decoding from json object to python object changes the
data types like below
 ------------------------
|JSON	     |   Python  |
|------------------------|
|object	     |   dict    |
|------------------------|
|array	     |   list    |
|------------------------|
|string	     |   str     |
|------------------------|
|number(int) |   int     |
|------------------------|
|number(real)|	 float   |
|------------------------|
|true        |	 True    |
|------------------------|
|false	     |   False   |
|------------------------|
|null	     |   None    |
 ------------------------
"""

import json

data = {}
data["Mark"] = {
    "name": "Mark",
    "age": 22,
    "height": 5.7,
    "grades": [2, 4, 7],
    "marks": (2, 1, 6),
    "Address": None
}
print("DATA:\n", data)

# Encoding python object data to Json before decoding
# TypeError: the JSON object must be str, bytes or byte array, not dict
data_string = json.dumps(data)
print("ENCODING:\n", data_string)

# Decoding json data into python object
decode = json.loads(data_string)
print ("Python object(DECODING):\n", decode)

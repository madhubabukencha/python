"""
Author      : Madhu Babu Kencha
created on  : 15-Nov-2018

In the process encoding python object to json object changes
the data types like below
 ----------------------------
|Python         |	JSON     |
 ----------------------------|
| dict	        |  object    |
| list, tuple	|  array     |
| str	        |  string    |
| int, long     |  number    |
| float	        |  number    |
| True	        |  true      |
| False	        |  false     |
| None	        |  null      |
 ----------------------------
"""

import json

data = [{"name": "Bob", "phone": "893488",
         "email": "example@gmail.com",
         "has_licence": True,
         "Address": None}]

# print(type(data))
# Accessing dictionary value inside python dictionary
# print(data[0]["name"])
print("DATA:", repr(data))


# The dumps method used to convert python object to json object
# Here encoding means converting python obj to json obj(also called serialization)
data_string = json.dumps(data, indent=2)

# print(type(data_string))
print("JSON:", data_string)
with open("storing_data.json", "w") as f:
    f.write(data_string)

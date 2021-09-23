"""
This program shows basic usage of urllib
"""
import urllib.request

data = urllib.request.urlopen("https://www.boredapi.com/api/activity")
print(type(data))
# Data is in the strig format
data_dict = data.read().decode('utf-8')
# Converting to python dictionary
data_dict = eval(data_dict)
print(data_dict["activity"])

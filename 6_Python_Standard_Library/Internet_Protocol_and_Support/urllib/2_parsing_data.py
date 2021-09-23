import urllib.request
import urllib.parse

url = "https://pythonprogramming.net/search/"
values = {'q': 'basic'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
response_data = response.read()
print(response_data)

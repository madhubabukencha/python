import requests

# Get an web page
response = requests.get("https://www.xkcd.com/353/")

# Content of response in unicode
print(response.text)

# Printing requested url
print("URL :", response.url)

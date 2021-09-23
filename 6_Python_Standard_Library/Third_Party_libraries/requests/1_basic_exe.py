import requests

# Get an web page
response = requests.get("https://www.xkcd.com/353/")

# Printing response of website
# print("Response: ", response)
print("Response:", response.status_code)  # 200 is SUCCESS
print("Response:", response.ok)

print(response.headers)

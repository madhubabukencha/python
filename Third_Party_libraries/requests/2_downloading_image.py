import requests

response = requests.get('https://images.unsplash.com/photo-1541781286675-7b70223358d1?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=1296&amp;q=60')
with open("comic.png", "wb") as f:
    # Content of the response, in bytes
    f.write(response.content)

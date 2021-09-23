from bs4 import BeautifulSoup
import requests

with open("cities.html") as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# The prettify function helps in giving nice format to html
# print(soup.prettify())

# To get body of html
body_of_cities = soup.body()
# print(body_of_cities)

# To get first div of body
first_div = soup.body.div
# print(first_div)

# Another way to get first div
# Type: class 'bs4.element.Tag'
my_div = soup.find('div')
# print(my_div)

# To find all div tags
all_div_tags = soup.find_all('div')
# print(all_div_tags)

# To fetch all class attributes
all_class = soup.find_all(class_="cities")
# print(all_class)

# To fetch particular attribute
all_attributes = soup.find(attrs={"data-example": "yes"})
print(all_attributes)

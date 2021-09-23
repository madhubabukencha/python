from bs4 import BeautifulSoup

my_file = open("cities.html", "r")
soup = BeautifulSoup(my_file, "html.parser")
my_file.close()


text = soup.select("#special")[0]

# Getting text from specific tag
print(text.get_text())

# To get the html tag
print(text.name)

# To get all attributes
print(text.attrs)

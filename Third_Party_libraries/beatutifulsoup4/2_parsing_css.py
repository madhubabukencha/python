from bs4 import BeautifulSoup

with open("cities.html", "r") as css_file:
    my_soup = BeautifulSoup(css_file, "html.parser")

# all elements of h2 tag
selecting_h2_tag = my_soup.select("h2")
# print(selecting_h2_tag)

# picking all cities from style class
all_cities = my_soup.select(".cities")
# print(all_cities)

# Picking all attributes
all_attributes = my_soup.select("[data-example]")
print(all_attributes)

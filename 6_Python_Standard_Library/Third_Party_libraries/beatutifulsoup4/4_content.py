from bs4 import BeautifulSoup


with open("cities.html", "r") as content_file:
    soup = BeautifulSoup(content_file, "html.parser")


body_content = soup.body.contents[1].contents
# print(body_content)

next_sibling = soup.body.contents[1].next_sibling.next_sibling
# print(next_sibling)

parent = soup.find(class_="madhu").parent.parent
# print(parent)

data = soup.find(class_="cities").find_next_sibling()
print(data)

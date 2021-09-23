"""
Name    :Madhu Babu Kencha
Date    : 04-jun-2020

The re.compile() function is used to compile a pattern into pattern object.
"""
import re

text = "Madhu is a very silent person. madhu only talks regarding programs"
pattern = re.compile("madhu", re.IGNORECASE)

find_all = re.findall(pattern, text)
print(find_all)

new_text = re.sub(pattern, "Madhu Babu Kencha", text)
print(new_text)

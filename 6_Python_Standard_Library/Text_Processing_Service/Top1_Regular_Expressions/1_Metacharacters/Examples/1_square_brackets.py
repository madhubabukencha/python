# See the square brackets documentation in README.md file
import re

pattern = "[0-9]"
invert_pattern = "[^0-9]"
text_string = "The police contact number in india is 100 and ambulance service 108"
result = re.findall(pattern, text_string)
invert_result = re.findall(invert_pattern, text_string)
print(result)
print(invert_result)

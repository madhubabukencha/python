"""
Name             : Madhu Babu Kencha
Created on       : 01-12-2018

This program provides basic understanding of escape characters

Python uses back slash to indicate special characters
'\n'   Denotes newline
'\t'   Denotes a tab
'\r'   Denotes a raw string
"""
import re

# re.search(pattern, string, flags)
# Here \n is a escape character(single char "\n")
# return None
print(re.search("n", "\n"))

# Here \n in string is a two diff characters("\" and "n")
print(re.search("n", r"\n"))

# Here \n is single character('n')
# returns the match
print(re.search("n", "\\n"))

# Regex with '\n' and r'\n' both looks for newline
# Here pattern is newline and string is new line
# returns the match
print(re.search("\n", "\n\n\n\n"))

# Here pattern in raw format(newline), it doesn't effect the pattern
# returns the match
print(re.search(r"\n", "\n\n\n\n"))

# Here pattern in raw format(newline), it doesn't effect the pattern
# returns the None since it doesn't find new line
print(re.search(r"\n", r"\n\n\n\n"))




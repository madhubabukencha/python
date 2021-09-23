"""
Name         : Madhu Babu Kencha
Created on   : 03-03-2019

The fill() function takes text as input and produces formatted text as
output. The text is now left justified.
"""
import textwrap
from sample_text import sample_text

print(textwrap.fill(sample_text, width=70))

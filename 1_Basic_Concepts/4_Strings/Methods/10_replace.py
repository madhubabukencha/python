"""
The replace method will return a copy of string by replacing
words with specified substring.

syntax:
------
str.replace(word, substring, count)

word            : This is going to be replace with substring \n
substring       : This is the word that we want to replace \n
count(optional) : The number of times you want replace word with substring\n
"""

# Example : 1
present_tense = "Ramu is reading a book"
past_tense = present_tense.replace('is', 'was')
print(past_tense)

# Example : 2
text = """ Coding is a good way to express yourself.
don't try to learn it in a single day. Feel
free to experiment with code. just code code and code
"""
code_to_hard_code = text.replace('code', 'hardcode', 2)
print(code_to_hard_code)

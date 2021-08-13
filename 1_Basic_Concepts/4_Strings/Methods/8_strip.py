'''
The "strip()" method removes the specified char from
start and end of the string and returns a copy of
strings

Syntax
------
str.string('char')

Returns
-------
A copy of stripped string.
'''
web_address = "oooo/www.madhubabu.comooo"
k = web_address.strip('o').strip('/')
print("This is original Web address:{}".format(web_address))
print("This is stripped Web address:{}".format(k))

# Example 2
print(f"\nRemoving white spaces:")
string_with_whitespace = r"Madhu Babu\n"
print("Original string : {}".format(string_with_whitespace))
print("Original string : {}".format(string_with_whitespace.strip(r"\n")))


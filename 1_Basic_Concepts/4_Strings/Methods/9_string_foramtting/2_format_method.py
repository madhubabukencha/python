"""
Name         : Madhu Babu Kencha
Created on   : 27-Nov-2018

The format method is used to format the output
"""

x = 20
y = 45

print("The values are {} and {}".format(x, y))
print("The values are {1} and {0}".format(x, y))

# Assigning values to some variable
print("The values are {aa} and {bb}".format(aa=x, bb=y))

# We can also swap the variable and we can repeat them
print("The values are {bb} and {aa}, {bb}".format(aa=x, bb=y))

# We can also add spaces using slice
print("The values are {0:<5} {1:>05}".format(x, y))

# We can also add sing
# '<' - Forces the field to be left-aligned within the available
# space (This is the default.)
# '>' - Forces the field to be right-aligned within the
#  available space.
print("The values are {0:<5} {1:>+5}".format(x, y))

z = 20 * 4544 * 10000
print("The values are {:,}".format(z))

# We can also specify fixed number of decimal points
print("The values are default: {0:f} and fixed decimals: {0:.3f}".format(z))

# We can also specify different bases
print("The values are hexadecimal: {0:X}, octal: {0:o}, binary: {0:b}".format(1000))

# we can also use short cut f instead of format method
print(f"The values are hexadecimal: {x:x}, octal: {x:o}, binary: {x:b}")

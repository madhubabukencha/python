"""
This program will takes a Python Unicode character,
looks up its name, and looks up the character again
from the name(it should match the original character)
"""
import unicodedata


def unicode_test(value):
    name = unicodedata.name(value)
    value_2 = unicodedata.lookup(name)
    print("Value : {0}, Name : {1},Verifying_Value : {2}".
          format(value, name, value_2))


unicode_test("A")
unicode_test("*")
unicode_test('^')
unicode_test("\\")
unicode_test("/")

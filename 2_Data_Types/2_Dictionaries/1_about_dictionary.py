"""
Creator         : "Madhu Babu Kencha"
Created on      : 27-10-2018

Dictionary is an unordered collection of data values, While other
compound data types have only value as an element. a dictionary has
a 'key: value' pair and each 'key' and 'value' separated by colon(:),
and 'key:value' pair separated by comma (,) from other 'key:value' pair.
Key of a  dictionary must be unique and of immutable data type
such as strings , Integers and tuples. But values can be repeated
and be of any
"""

# Creating an empty dictionary
# empty_dictionary = dict()
empty_dictionary = {}
print("Empty dictionary:{0:>22}".format(str(empty_dictionary)))

# Dictionary with Integer keys
dict_integers = {1: "apple", 2: "Mango", 3: "Orange", 4: "Pineapple"}
print("Dictionary with Integer key values :", dict_integers)

# Mixed key values
dict_mixed = {'name': "Madhu", 1: 'king', 'number': 1, 'date': '27-10-2018'}
print("Mixed keys and values              :", dict_mixed)

# Creating a dictionary with dict() method
dictionary = dict(name="Madhu", age=22, salary=300000)
print("Dictionary from tuple              :", dictionary)

# Creating a dictionary Item  as a pair
dictionary = dict([(1, "Madhu"), (2, "Kiran")])
print("Dictionary from Item as a pair     :", dictionary)

# Creating nested dictionary
nested_dictionary = {1: {'a': "A", 'b': "B", 'c': "C"},
                     2: {'d': "D", 'e': "E", 'f': "F"}}
print("Nested dictionary                  :", nested_dictionary)

"""
Name           : Madhu Babu Kencha
Created on     : 19-08-2020

The items method return a view object that contains a list of dictionaries
key and value pair tuple

syntax
------
dictionary.items()

* items method doesn't take any thing as input
* Returns a view object

what is view object?
https://stackoverflow.com/questions/8957750/what-are-dictionary-view-objects
the keys view is not a copy of the keys at a given point in time, but rather
a simple window that shows you the keys; if they are changed, then what you
see through the window does change as well
"""

grades = {'Balu': 43, 'Martin': 56, 'Madhu': 100}

# view object is simply a window. Whenever grades dictionary changes
# view object also changes
view_object = grades.items()
print(f"View Object: {view_object}")

# Now I am going to change grades
grades['Venkat'] = 48

# You can notice, view_object changed
view_object = grades.items()
print(f"View Object: {view_object} \n")

# Looping over an view object
for key, value in view_object:
    print(f"Name: {key:<10} Grade: {value}")

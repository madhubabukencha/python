# We can use tuple as a key in the dictionary.
# We are not able to use list as a key of dictionary

marks = {(45, 25): "James",  (58, 96): "Robert"}
print(marks[(45, 25)])

# The items() function in of dictionary returns the dictionary
name_and_age = {"madhu": 23, "Varun": 24}
print(name_and_age.items())

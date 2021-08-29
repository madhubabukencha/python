"""
Name : Madhu Babu Kencha

This program will explain about keyword arguments
keyword arguments have two asterisks as their prefix
"""


def function1():
    # Creating a dictionary
    x = {'name1': "Madhu", "name2": "Krisha", "name3": "Hari"}
    # Unpacking key-word arguments
    function2(**x)


def function2(**kwargs):
    for i in kwargs:
        print(i, '=', kwargs[i])

        
if __name__ == "__main__":
    function1()

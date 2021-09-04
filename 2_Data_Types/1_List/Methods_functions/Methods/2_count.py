# The count() method returns the number of occurrence of an element in a list

ages = input("Please enter input with some space:").split()

on_border_ages = ages.count('18')
if on_border_ages >= 0:
    print("Total number of people having exactly 18 years old:", on_border_ages)

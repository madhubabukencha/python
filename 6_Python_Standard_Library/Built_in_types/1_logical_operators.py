# Defining boolean variables
isRaining = True
isSunny = False

# Logical operators

"""
1)and
True and True   --> True
True and False  --> False
False and False --> False
False and True  --> False
"""
# Make isSunny true to make statement execute
if isRaining and isSunny:
    print("It is raining and it is sunny")

"""
2)or
True or True   --> True
True or False  --> True
False or False --> False
False or True  --> True
"""
if isRaining or isSunny:
    print("It may be it raining or sunny")

"""
3)not
not True --> False
not False --> True
"""
# Make isRaining false
if not isSunny:
    print("It is not raining")

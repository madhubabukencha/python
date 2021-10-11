"""
Name    :Madhu Babu Kencha
Date    :04-April-2020

In a single word absolute means non negative value
"""
# pylint: disable=C0103

# Absolute value of an Integer
temperature = -20
print(f"Absolute value of int {temperature}: {abs(temperature)}")

# Absolute value of a Float
y_axis = 54.3321
print(f"Absolute value of float {y_axis}: {abs(y_axis)}")

# Absolute value of a complex number
# In case complex numbers, abs() returns it's magnitude
# magnitude of 3-4j ==> |3-4j|^2
#                   ==> 3^2 + 4^2
#                   ==> sqrt(9+16)
#                   ==> 5.0

complex_number = 3-4j
print(f"Absolute value of complex number {complex_number}: {abs(complex_number)}")

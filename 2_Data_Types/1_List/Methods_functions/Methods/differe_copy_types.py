#!/usr/bin/env python
# coding: utf-8

# Different types of copy methods in python
import copy

# Using equal sign operators
print("USING EQUAL(=) SIGN : ")
equal_var = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
temp_equal_var = equal_var
print(F"{'Variable':<20} ID_Value")
print(F"{'equal_var':<20} {id(equal_var)}")
print(F"{'temp_equal_var ':<20} {id(temp_equal_var )}")

print("\nUSING COLON(:) SIGN : ")
colon_var = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
temp_colon_var = colon_var[:]
temp_colon_var = colon_var[:]
print(F"{'Variable':<20} ID_Value")
print(F"{'colon_var':<20} {id(colon_var)}")
print(F"{'temp_colon_var':<20} {id(temp_colon_var)}")
print(F"{'colon_var[1]':<20} {id(colon_var[1])}")
print(F"{'temp_colon_var[1]':<20} {id(temp_colon_var[1])}")

# Using copy method(shallow copy)
print("\nUsing Copy Method : ")
to_copy = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
temp_var = to_copy.copy()
print(F"{'Variable':<20} ID_Value")
print(F"{'to_copy':<20} {id(to_copy)}")
print(F"{'temp_var':<20} {id(temp_var)}")
print(F"{'to_copy[1]':<20} {id(to_copy[1])}")
print(F"{'temp_var[1]':<20} {id(temp_var[1])}")

# Using deepcopy method
print("\nUsing deepcopy Method : ")
to_deepcopy = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
temp_deep_var = copy.deepcopy(to_deepcopy)
print(F"{'Variable':<20} ID_Value")
print(F"{'to_deepcopy':<20} {id(to_deepcopy)}")
print(F"{'temp_deep_var':<20} {id(temp_deep_var)}")
print(F"{'to_deepcopy[1]':<20} {id(to_deepcopy[1])}")
print(F"{'temp_deep_var[1]':<20} {id(temp_deep_var[1])}")
"""
inf - is infinity, a value greater than any other value
-inf - in neg infinity, a value smaller than any other value
nan - Not a number,equal to o
"""
x = float('inf')
print("The float is: {:F}".format(x))

pos_inf = float('inf')
neg_inf = -float('inf')
nan_value = pos_inf + neg_inf
print("The float value is: {:f}".format(nan_value))

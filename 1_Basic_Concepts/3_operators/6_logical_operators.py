"""
Python logical operators are,
1. and --> Returns True if both operands are true
2. or  --> Returns True if anyone of operands is true
3. not --> not True will be False
"""
x = 10
y = 20

print(f"AND: {(x < y)  and (y > x)}")
print(f"AND: {(x > y)  and (y > x)} \n")

print(f"OR: {(x < y)  or (y > x)}")
print(f"OR: {(x > y)  or (y > x)}\n")

print(f"NOT: {not((x < y)  or (y > x))}")
print(f"NOT: {not((x > y) and (y > x))}")

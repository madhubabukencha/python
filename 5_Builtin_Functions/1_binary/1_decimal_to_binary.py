"""
Date : 12-March-2020
This program tells us how to convert a decimal number into
a binary format.

Decimal Number:
Decimal system is base 10 (ten symbols, 0-9, is used to
represent a number)

Binary Number:
Binary system base is 2
A number started with '0b' considered as binary number
"""


def decimal_to_binary(value):
    print(f"Binary value of {value}: {bin(value)}")


decimal_to_binary(67)
decimal_to_binary(89)

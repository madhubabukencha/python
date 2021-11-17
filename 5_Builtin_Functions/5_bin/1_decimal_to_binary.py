"""
Date : 12-March-2020
The bin method takes integer as input and returns binary representation
of a string. If input/parameter is not an integer then its has implement
__index__ method to return the integer

Decimal Number:
Decimal system is base 10 (ten symbols, 0-9, is used to represent a number)

Binary Number:
Binary system base is 2
A number started with '0b' considered as binary number
"""


def decimal_to_binary(value):
    print(f"Binary value of {value}: {bin(value)}")


decimal_to_binary(67)
decimal_to_binary(89)


class BinaryConverted:
    m = 1
    n = 2
    o = 3

    def __index__(self):
        return self.m + self.n + self.o


print(bin(BinaryConverted()))




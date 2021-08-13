"""
Name       : Madhu Babu Kencha
Created on : 25-Nov-2018

To raise an exception forcefully we use "raise" in python
"""


def main(number):
    sum_value = 0
    if number <= 0:
        raise ValueError("This is not Natural number")
    else:
        numbers_list = [int(i) for i in str(number)]
        cubes = list(map(lambda x: x*x*x, numbers_list))
        sum_value = sum(cubes)

    if sum_value == number:
        print("It is an armstrong number")
    else:
        print("It is not a armstrong number")


if __name__ == "__main__":
    try:
        main(0)
    except ValueError as v:
        print(f"Error:{v}")
    main(153)

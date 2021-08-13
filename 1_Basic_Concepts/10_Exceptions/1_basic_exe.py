"""
Name       : Madhu Babu Kencha
Created on : 25-Nov-2018

This is the program about exception handling.
Exception handling help us to catch the run time
errors
"""
import sys


def main(number, divisor):
    try:
        number = (int(number)/divisor)
        print("The number is:", number)
    except ValueError:
        print("Error: The number must be integer")
    except ZeroDivisionError:
        print("Error: Divisor must be greater than zero")
    except Exception as err:
        print(f"Unknown Error:{sys.exc_info()} \nError Message: {err}")
    # If everything goes fine then else part will execute
    else:
        print("Hey! good job")


if __name__ == '__main__':
    main(34, 0)
    main("name", 7)
    main(5, 2)

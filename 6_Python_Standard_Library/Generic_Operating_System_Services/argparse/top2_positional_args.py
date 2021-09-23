#!/usr/bin/env python3
"""
Author      : Madhu Babu Kencha
Created on  : 14-sept-2018

1) Calling a program require us to specify an option
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Performs the arithmetic operations")
    parser.add_argument("number_1", help="First Number")
    parser.add_argument("number_2", help="Second Number")
    parser.add_argument("operation", help="Performs the specified operation")
    args = parser.parse_args()

    # By default the argument value comes in string format
    number_1 = int(args.number_1)
    number_2 = int(args.number_2)
    final_result = None
    if args.operation == "add":
        final_result = number_1 + number_2
    elif args.operation == "sub":
        final_result = number_1 - number_2
    elif args.operation == "mul":
        final_result = number_1 * number_2
    elif args.operation == "div":
        final_result = number_1/number_2
    else:
        raise NotImplementedError(f"We have not implemented '{args.operation}' operation")

    print(final_result)


if __name__ == '__main__':
    main()

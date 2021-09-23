#!/usr/bin/env python3
"""
Author      : Madhu Babu Kencha
Created on  : 14-sept-2018


1) In this program we will see how to combain both positional and
   optional arguments
2) Order of passing arguments does not matter
"""

import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("name", help="Print you the name")
	parser.add_argument("-v", "--verbose", help="Print the verbose output",
		                action="store_true")
	args = parser.parse_args()
	your_name = args.name
	if args.verbose:
		print("The programmer name is {}".format(your_name))
	else:
		print(your_name)


if __name__ == '__main__':
	main()
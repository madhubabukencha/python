#!/usr/bin/env python3
"""
Author      : Madhu Babu Kencha
Created on  : 14-sept-2018


1) The action "count" is used to count the number of occurences of a 
   specific optional arguments
"""

import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("square", help = "Print the square of number", type = int)
	parser.add_argument("-v", "--verbose", help = "Increases the verbosity of the output",
	                    action = "count", default = 0)
	args = parser.parse_args()
	res_square = args.square**2
	if args.verbose >= 2:
		print("The square of {} is {}".format(args.square, res_square))
	elif args.verbose >= 1:
		print("{}**2=={}".format(args.square, res_square))
	else:
		print(res_square)


if __name__ == '__main__':
	main()
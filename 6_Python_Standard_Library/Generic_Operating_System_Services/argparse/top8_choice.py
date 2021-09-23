#!/usr/bin/env python3
"""
Author      : Madhu Babu Kencha
Created on  : 14-sept-2018

1) To understand the program go with help message
   and try to run by passing different options to 
   --verbosity
"""


import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("square", help = "quare the given number", type = int)
	parser.add_argument("-v", "--verbosity", help = "Increase the output verbosity",
		                choices = [0, 1, 2], type = int)
	args = parser.parse_args()
	res_square = (args.square**2)
	if args.verbosity == 2:
		print("The square of {} is {}".format(args.square, res_square))
	elif args.verbosity == 1:
		print("{}**2=={}".format(args.square, res_square))
	else:
		print(res_square)


if __name__ == '__main__':
	main()
#!/usr/bin/env python3
"""
Author      : Madhu Babu Kencha
Created on  : 14-sept-2018
"""

import argparse


def main():
	parser = argparse.ArgumentParser()
	# "argparse" treats options we given it as strings
	# So let's tell "argparse" to treat that input as integer
	parser.add_argument("square", help = "Square the given number", type = int )
	args=parser.parse_args()
	print(args.square**2)


if __name__ == '__main__':
	main()

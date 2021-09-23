#!/usr/bin/env python3
"""
Author      : Madhu Babu Kencha
Created on  : 14-sept-2018


1) This program to demonstrate the optional argument parsing
2) This program is written to display something when --verbosity option is
   specified and display not when nothing
3) To show option is actually optional, there is no error when running the 
   program without it
4) When using the --verbosity option, no need to specify any value
"""

import argparse


def main():
	parser = argparse.ArgumentParser()
	# This means that, if the option is specified, assign the value True to args.verbose
	parser.add_argument( "--verbosity", help = "Increases the verbosity of output", \
		                 action="store_true" )
	args = parser.parse_args()
	if args.verbosity:
		print( "Verbosity is on" )


if __name__ == '__main__':
	main()

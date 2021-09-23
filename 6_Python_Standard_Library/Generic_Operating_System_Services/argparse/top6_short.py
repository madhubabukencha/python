#!/usr/bin/env python3
"""
Author      : Madhu Babu Kencha
Created on  : 14-sept-2018

1) This program demonstrate how to specify short options
"""
import argparse


def main():
	parser = argparse.ArgumentParser()
	# This means that, if the option is specified, assign the value True to args.verbose
	parser.add_argument( "-v", "--verbosity", help = "Increases the verbosity of output", \
		                 action="store_true" )
	args = parser.parse_args()
	if args.verbosity:
		print( "Verbosity is on" )


if __name__ == '__main__':
	main()
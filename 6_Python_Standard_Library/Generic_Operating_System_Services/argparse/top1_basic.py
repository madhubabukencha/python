#!/usr/bin/env python3
"""
Author : Madhu Babu Kencha
DATE   : 14-sept-2018

1) "argparse" is a recommended command line parsing module in python
2) Two other modules also full fill the same task namely getopt and the
   deprecated optparse.
3) usage : top1_basic.py -h or top1_basic.py --help
"""

import argparse


def main():
    """This will tells the basic usage of argparse module"""
    # Initializing parser
    parser = argparse.ArgumentParser()
    # Trying to parse the argument
    parser.parse_args()


if __name__ == '__main__':
    main()

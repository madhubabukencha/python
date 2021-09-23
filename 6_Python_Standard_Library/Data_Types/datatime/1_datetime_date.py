"""
In this program we are going to see usage of datatime module class
called date
"""
from datetime import date


def main():
    # To get today's date
    today = date.today()
    print("Today's date is: {}".format(today))

    # To get date individual components of date
    print("Day: {}, Month: {}, Year: {}".format(today.day, today.month, today.year))

    # To get weekday number(it starts from 0 and ends with 6)
    print("Day Number: {}".format(today.weekday()))

    # To get today in words
    print("Day in words: {}".format(today.ctime().split()[0]))

    # All variables and methods associated with today obj
    print("Variable and Methods: {}".format(dir(today)))


if __name__ == '__main__':
    main()

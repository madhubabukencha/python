"""
In this program we are going to learn how to use datatime class
"""
from datetime import datetime


def main():
    # To get current date and time
    today = datetime.now()
    print("Date and Time: {}".format(today))

    # To get time
    time = datetime.time(today)
    print("Time: {}".format(time))

    # String formatter
    # https://www.w3schools.com/python/python_datetime.asp
    day = today.strftime("%A")
    print("The Day: {}".format(day))

    # Printing time in 12h format
    time = today.strftime("Time in 12h format: %H:%M:%S")
    print(time)

    # Print local version of date
    date = today.strftime("Local date: %x")
    print(date)


if __name__ == '__main__':
    main()

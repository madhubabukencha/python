"""
In this program we are going to learn about timedelta
"""
from datetime import date
from datetime import datetime
from datetime import timedelta


def main():
    # Constructing basic timedelta class
    print(timedelta(days=365, hours=5, minutes=1))

    # what is after 4 weeks 2 days from now
    day = datetime.now() + timedelta(days=2, weeks=1)
    print(f"Day:{day.strftime('%A')}, Date: {day.strftime('%d')}")

    # Creating date
    now = datetime.now()
    birth_day = datetime(1996, 5, 13, hour=11, minute=59, second=59)
    time = now.year-birth_day.year
    print(time)


if __name__ == '__main__':
    main()

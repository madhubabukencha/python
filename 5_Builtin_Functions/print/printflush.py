"""
This program helps in understanding the concept of flush.
Whenever we writing something to the disk or console
flow things will be like below,
data --> Buffer --> writes to the disk

with flush function it would be,
data -------------> writes to the disk

Useful links:
https://www.youtube.com/watch?v=FLdGnbil5M4
https://gist.github.com/santosh/5235922
"""

from time import sleep

text = "Lorem Ipsum is simply dummy text of the printing \
and typesetting industry. Lorem Ipsum has been the\
industry's standard dummy text ever since the 1500s,\
when an unknown printer took a galley of type and\
scrambled it to make a type specimen book"

for character in text:
    # In pycharm automatic flush seems enable
    # Try on python terminal to understand the difference
    # Check by assigning flush True and False
    print(character, end=" ", flush=True)
    sleep(.1)
print("\n")

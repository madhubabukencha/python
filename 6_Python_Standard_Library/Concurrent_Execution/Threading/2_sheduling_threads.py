"""
We can't restrict how thread gives importance to process in processor.
In the output you can notice how it varies
"""
import threading
from time import sleep

STOP_DRINKING = True


def drink_water():
    name = threading.currentThread().getName()
    drink_count = 0
    while STOP_DRINKING:
        drink_count += 1
    print(f"you drank {name}: {drink_count} times\n")


if __name__ == '__main__':
    threading.Thread(target=drink_water, name="normal water").start()
    threading.Thread(target=drink_water, name="Bicelary").start()
    STOP_DRINKING = False

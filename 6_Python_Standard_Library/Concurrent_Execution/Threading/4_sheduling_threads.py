"""
We can't restrict how a thread gives importance to a process in the processor.
In the below example, we can notice, we has spawn 2 similar child threads but
number of times they got executed on the processor is different. From these we
can understand that, we can't district thread execution on the processor.

In the output you can notice how it varies
"""
import threading

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

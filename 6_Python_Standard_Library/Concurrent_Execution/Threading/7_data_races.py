"""
Data Races:
In concepts we can practically see how much multiple threads creates
a problem when they are trying to access same variable, files ect..,

In the output you can notice difference between expected value and
the value we got
"""
import threading


apples_bucket = 0
# apples_to_add = 20
apples_to_add = 20_000_00


def add_to_bucket():
    # In real world, instead of global variable you can expect a file
    global apples_bucket
    for _ in range(apples_to_add):
        apples_bucket += 1


if __name__ == '__main__':
    ram = threading.Thread(target=add_to_bucket)
    shiv = threading.Thread(target=add_to_bucket)
    ram.start()
    shiv.start()
    ram.join()
    shiv.join()
    print(f"Expected apples: {apples_to_add + apples_to_add}")
    print(f"Apples in the bucket: {apples_bucket}")

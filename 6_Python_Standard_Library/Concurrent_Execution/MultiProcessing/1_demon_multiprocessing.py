import os
import multiprocessing


# Function to waste cpu time
def waste_cpu():
    while True:
        pass

print(__name__)
if __name__ == '__main__':
    # Displaying information about thread
    print(f"Process ID: {os.getpid()}")

    print("Creating 10 CPU wasters")
    for i in range(10):
        multiprocessing.Process(target=waste_cpu).start()

    # Displaying information about thread
    print(f"Process ID: {os.getpid()}")

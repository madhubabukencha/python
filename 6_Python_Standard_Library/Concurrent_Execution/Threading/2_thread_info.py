"""
It will demonstrate the basic functionality of threading
"""

import os
import threading


# Function to waste cpu time
def waste_cpu():
    print(threading.current_thread())
    while True:
        "To run a thread forever"
        pass


# Displaying information about thread
print(f"Process ID: {os.getpid()}")
print("Thread Count:", threading.active_count())
print(threading.current_thread().getName())
for thread in threading.enumerate():
    print(thread)

print("Creating 12 CPU wasters")
for i in range(12):
    threading.Thread(target=waste_cpu).start()

# Displaying information about thread
print(f"Process ID: {os.getpid()}")
print("Thread Count:", threading.active_count())

# Not useful, it just our information
# We are looking over on active threads here
# for thread in threading.enumerate():
#     print(threading.current_thread().getName())
#     print(thread)
print("Main thread execution is completed")

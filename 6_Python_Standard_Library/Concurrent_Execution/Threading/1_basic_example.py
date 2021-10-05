"""
This program teaches you how to a create multithreading program.
It would advisable to know the difference between a thread and
a process before starting to understanding this script.
https://www.guru99.com/difference-between-process-and-thread.html
"""

import time
import threading

start = time.perf_counter()


def time_counter():
    print("Sleeping 1 second")
    time.sleep(1)
    # It will give the current thread details
    print(f"Thread: {threading.current_thread()}")
    print("Sleeping is done")


print(f"Thread: {threading.current_thread()}")
# Calling function using threads
t1 = threading.Thread(target=time_counter)
t2 = threading.Thread(target=time_counter)

# start() method is for starting thread execution
t1.start()
t2.start()

# join() method makes waits of main thread until child threads completion
# Comment and see for better understanding
t1.join()
t2.join()
end = time.perf_counter()
print(f"Total time: {end-start:.2f}")

"""
concurrent.futures is just creating another way of creating multiprocessing

Methods Used
------------
1. executor.submit()
   The submit() method schedules each task. This creates a Future object, which
   represents the task to be done. The Future Object encapsulate the execution
   of our function and allows us to check on it after its been schedule so we
   can check that its running or if it's done also checks the result.

2. future_object.result() method print the return value of a function
"""

import concurrent.futures
import time


start = time.perf_counter()


def test_function(seconds, name):
    print(f"Hello {name}!!!")
    print(f"Started {seconds} sleeping")
    time.sleep(seconds)
    return "Sleeping is done"


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_object = executor.submit(test_function, 2, "Madhu Babu Kencha")
        print(future_object.result())
    end = time.perf_counter()
    print(f"Total time: {end-start:.2f}")

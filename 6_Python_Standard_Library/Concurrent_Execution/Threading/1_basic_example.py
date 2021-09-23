import time
import threading

start = time.perf_counter()


def time_counter():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Sleeping is done")


# Calling function using threads
t1 = threading.Thread(target=time_counter)
t2 = threading.Thread(target=time_counter)

# start() method is for starting thread execution
t1.start()
t2.start()

# join() method waits until thread completion
# Comment and see for better understanding
t1.join()
t2.join()
end = time.perf_counter()
print(f"Total time: {end-start:.2f}")

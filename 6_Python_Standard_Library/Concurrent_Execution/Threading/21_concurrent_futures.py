import concurrent.futures
import time


start = time.perf_counter()


def time_counter(seconds, name):
    print(f"Sleep {seconds, name} second(s)")
    time.sleep(seconds)
    return f"Sleeping {seconds} second(s) done"


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    # The executor.submit() method schedule each task
    # This creates a Future object, which represents the task to be done
    
    results = [executor.submit(time_counter, sec, "Madhu") for sec in seconds]
    # Since we used as_completed() method, it will print the results as completed
    for f in concurrent.futures.as_completed(results):
        # result() method returns the return value of a function(i.e here time_counter function's)
        # if result() is called then it will wait until function gets completed
        print(f.result())

end = time.perf_counter()
print(f"Total time: {end-start:.2f}")
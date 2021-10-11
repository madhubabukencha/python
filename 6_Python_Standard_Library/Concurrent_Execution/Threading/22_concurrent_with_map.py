import concurrent.futures
import time

start = time.perf_counter()


def time_counter(seconds, name):
    print(name)
    print(f"Sleep {seconds} second(s)")
    time.sleep(seconds)
    return f"Sleeping {seconds} second(s) done"


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    args = ((sec, "Madhu") for sec in seconds)
    results = executor.map(lambda para: time_counter(*para), args)

    for result in results:
        print(result)


end = time.perf_counter()
print(f"Total time: {end-start:.2f}")
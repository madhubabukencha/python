import concurrent.futures
import time

start = time.perf_counter()


def do_something(sec):
    print("Sleeping {}".format(sec))
    time.sleep(sec)
    return f"Sleeping {sec} done"


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]

        # map method returns the results as they were completed
        results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)
    end = time.perf_counter()
    print(f"Total Time:{end - start}")
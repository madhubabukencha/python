import concurrent.futures
import time

start = time.perf_counter()


def do_count(sec):
    print(f"Sleeping {sec}")
    time.sleep(sec)
    return f"Sleeping {sec} is done"


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_count, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    end = time.perf_counter()
    print(F"Total time: {end-start}")
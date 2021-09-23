import multiprocessing
import time

start = time.perf_counter()


def test_function():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Sleeping is done")


p1 = multiprocessing.Process(target=test_function)
p2 = multiprocessing.Process(target=test_function)

if __name__ == "__main__":
    # Executing functions
    p1.start()
    p2.start()

    # Using join method we can make program to wait until
    # these process getting completed
    p1.join()
    p2.join()

    end = time.perf_counter()
    print(f"Total time took for execution:{end - start:.2f}")

import multiprocessing
import time


start = time.perf_counter()


def test_function(seconds):
    print(f"Sleeping {seconds} second")
    time.sleep(1)
    print("Sleeping is done")


processes = []
if __name__ == '__main__':
    for _ in range(10):
        p = multiprocessing.Process(target=test_function, args=[2])
        p.start()
        # If you add join() method here then it becomes synchronization
        processes.append(p)

    for process in processes:
        process.join()

    end = time.perf_counter()
    print(f"Total time took to complete the execution:{end - start:.2f}")

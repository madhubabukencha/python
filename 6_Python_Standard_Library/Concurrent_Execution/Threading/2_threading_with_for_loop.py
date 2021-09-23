import time
import threading

start = time.perf_counter()


def time_counter(seconds):
    print(f"Sleep {seconds} second(s)")
    time.sleep(seconds)
    print("Sleeping is done")


threads_list = []
for _ in range(10):
    t = threading.Thread(target=time_counter, args=[1.5])
    t.start()
    # If you add join here it will equal to synchronization(it will take 10sec)
    # t.join()
    threads_list.append(t)

for thread in threads_list:
    thread.join()

end = time.perf_counter()
print(f"Total time: {end-start:.2f}")

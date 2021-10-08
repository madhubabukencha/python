"""
Mutual Exclusion(mutex)
-----------------------
In data races, we have seen that, data corrupted while accessing shared
resources. To solve this problem we have something called mutex. Here
in mutex we lock critical resource accessing simultaneously.

Whatever thread uses resources it has some lock so that other threads
wouldn't come and modify the content until it release the lock. If thread
waiting for some input or sleeping then it wouldn't need lock, so it will
released the lock so that other process might use the resources.
"""
import threading
import time

apples_bucket = 0
apples_to_add = 5
resource_lock = threading.Lock()


def add_to_bucket():
    # In real world, instead of global variable you can expect a file
    global apples_bucket

    # Entire for block is not a critical resource
    # Just adding apples is the critical block, so commenting these lines
    # resource_lock.acquire()
    for _ in range(apples_to_add):
        print(threading.current_thread().getName(), "is sleeping")
        time.sleep(0.5)
        # Here we locking the critical resources
        resource_lock.acquire()
        apples_bucket += 1
        resource_lock.release()
    # resource_lock.release()


if __name__ == '__main__':
    ram = threading.Thread(target=add_to_bucket)
    shiv = threading.Thread(target=add_to_bucket)
    ram.start()
    shiv.start()
    ram.join()
    shiv.join()
    print(f"Expected apples: {apples_to_add + apples_to_add}")
    print(f"Apples in the bucket: {apples_bucket}")

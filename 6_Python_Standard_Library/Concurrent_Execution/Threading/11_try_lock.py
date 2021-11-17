"""
In case of standard mutex lock, one thread need to wait until other
thread releases the acquired lock. But in some scenarios, we wanted
to do other tasks if mutex was locked. Too meet this scenario we have
something called "try lock".

If the mutex you're trying to lock is available, it will get locked
and the method will return true. Otherwise, If the mutex is already
possessed by another thread, the Try Lock method will immediately
return False. That return value of true or false lets the thread know
whether or not it was successful in acquiring the lock. So if I try to
lock the mutex that was already locked by other thread,the attempt will
fail, so thread do the other task.
"""
import threading
import time

lock = threading.Lock()
apple_bucket = 0


def add_apples():
    global apple_bucket
    name = threading.currentThread().getName()
    apples_to_add = 0
    while apple_bucket <= 20:
        if apples_to_add and lock.acquire(blocking=False):
            print(f"{name} thread is adding apple")
            apple_bucket += apples_to_add
            apples_to_add = 0
            time.sleep(0.3)
            lock.release()
        else:
            apples_to_add = 1
            time.sleep(0.2)
            print(f'{name} is waiting')


if __name__ == '__main__':
    thread_1 = threading.Thread(target=add_apples)
    thread_2 = threading.Thread(target=add_apples)
    start = time.perf_counter()
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    print(apple_bucket)
    end = time.perf_counter()
    print(f'Time:{end-start}')

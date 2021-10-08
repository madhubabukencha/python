"""
If a thread tries to lock a mutex that it's already locked, it'll enter
into a waiting list for that mutex, which results in something called a
deadlock(already seen the previous program), because no other thread
can unlock that mutex. There may be times when a program needs to lock
a mutex multiple times before unlocking it. In that case, you should use a
reentrant mutex to prevent this type of problem. A reentrant mutex is a
particular type of mutex that can be locked multiple times by the same
process or thread.
"""
import threading

# Creating RLock
lock = threading.RLock()

pens = 0
pencils = 0


def add_pens():
    global pens
    for _ in range(100):
        lock.acquire()
        pens += 1
        lock.release()


def add_pencil():
    global pencils
    for _ in range(100):
        lock.acquire()
        add_pens()
        pencils += 1
        lock.release()


if __name__ == '__main__':
    madhu = threading.Thread(target=add_pencil())
    madhu.start()
    madhu.join()
    print(pencils)
    print(pens)

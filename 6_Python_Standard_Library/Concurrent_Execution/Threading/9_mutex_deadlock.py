"""
In this program we can see how mutex situation occurs.
A dead lock situation occurs when you try to lock already
locked resources

NOTE: It this program never ends so, you can terminate manually
"""
import threading


lock = threading.Lock()

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

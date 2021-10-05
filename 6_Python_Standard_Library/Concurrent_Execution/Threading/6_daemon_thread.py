"""
Sometimes we create some threads that runs periodically. But the
problem is, those threads execute even after main thread completion.
If you want to stop such kind of threads whenever main thread is completed
then you can declare them as a daemon thread.
"""
import threading
import psutil  # pip install psutil
from time import sleep


def check_cpu_ram(seconds):
    while True:
        # To check usage percentage
        cpu = psutil.cpu_percent()
        # To check ram usage percentage
        ram = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu}")
        print(f"RAM Usage: {ram}\n")
        sleep(seconds)


if __name__ == '__main__':
    os_stats = threading.Thread(target=check_cpu_ram, args=[1])
    # We are making a non daemon thread as daemon thread
    # To see the difference, you can comment this line
    os_stats.daemon = True
    os_stats.start()
    print("Starting main thread and sleep 2 sec")
    sleep(2)
    print("sleep 2 more sec")
    sleep(2)
    print("Main thread is done")




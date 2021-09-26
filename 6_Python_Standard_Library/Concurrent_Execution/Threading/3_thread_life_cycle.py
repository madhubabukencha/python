"""
This program helps to understand the thread life cycles
Source: LinkedIn Learning
"""
from time import sleep
import threading


class ChefMadhu(threading.Thread):
    def __init__(self):
        """It's mandatory to call parent thread class init method"""
        super().__init__()

    def run(self):
        """Overriding parent class run method"""
        print("Madhu started and waiting for sausage to thaw...")
        sleep(3)
        print("Cutting sausage is done")


# main thread
if __name__ == '__main__':
    print("Barron started & requesting madhu's help.")
    madhu = ChefMadhu()
    print('  Madhu alive?:', madhu.is_alive())

    print('Barron tells Madhu to start.')
    madhu.start()
    print('  Madhu alive?:', madhu.is_alive())

    print('Barron continues cooking soup.')
    sleep(0.5)
    print('  Madhu alive?:', madhu.is_alive())

    print('Barron patiently waits for madhu to finish and join...')
    madhu.join()
    print('  Madhu alive?:', madhu.is_alive())

    print('Barron and Madhu are both done!')


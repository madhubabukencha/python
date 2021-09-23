from time import sleep


def progress_bar(percent=0, width=40):
    left = (width * percent)//100
    right = width - left
    # print(f'left : {left}, right: {right}')
    print('\r[', "#" * left, " " * right, ']',
          f'{percent:.0f}%', sep="", end="")


for i in range(101):
    progress_bar(i)
    sleep(0.1)

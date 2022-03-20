# This is the program will print fibonacci series
def main():
    a, b = 0, 1
    count = 0
    while a <= 1000:
        print(a, end=",")
        count += 1
        a, b = b, b+a
    print("\n count:%d" % count)


if __name__ == '__main__':
    main()

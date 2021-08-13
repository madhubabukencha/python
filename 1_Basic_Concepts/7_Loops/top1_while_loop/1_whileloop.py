# This is the program will print fibonacci series
def main():
    a, b, d = 0, 1, 0
    count1 = 0
    while d <= 1000:
        d = 0  # To make d value 0 in every iteration
        print(a, end="|")
        count1 += 1
        a, b = b, b+a
        d += a
    print("\ncount:%d" % (count1))


if __name__ == '__main__':
    main()

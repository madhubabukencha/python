def swap_case(string):
    length = len(s)
    p = ""
    if length <= 10 >= 0:
        for i in s:
            if i.isupper():
                k = i.lower()
            else:
                k = i.upper()
            p += k
    return p


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# This program shows the usage of appending mode


def main():
    with open("write_exe.txt", "a", encoding="utf-8") as f:
        f.write("I love Python in coding \n")


if __name__ == '__main__':
    main()

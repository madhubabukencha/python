# This the program which is used to print text along with line number


def my_details():
    file1 = open("story.txt")
    i = 1  # i=1, makes our line numbers starts from one
    for line in file1:
        print("line:%d" % i, line, end="")
        i += 1
    file1.close()


if __name__ == "__main__":
    my_details()

# Enumerate returns the index
def exa_enumerate():
    name = "Kencha Madhu Babu"
    for index, k in enumerate(name):
        if k == 'a':
            print("{} is the index of a".format(index))


if __name__ == "__main__":
    exa_enumerate()
# This program shows how to use read() method
# Syntax : file_object.read(count)
# Syntax : file_object.readline(count)
# Syntax : file_object.readlines(count)
# count : Number of bytes to read


def main():
    # Here we are opening a file with read mode
    # Benefit of opening a file using "with" is, it will automatically
    # close the file, once a block inside "with" is finished.
    # So need to specify close() method explicitly
    with open("sample.txt", "r", encoding="utf-8") as f:
        # See the difference by uncommenting below lines one by on

        # readline() method reads a single line
        # data = f.readline()

        # readlines() method reads all lines if don't specify the count
        #data = f.readlines()

        # If we specify bytes the read() method reads
        # only reads that many bytes. If we don't then
        # it will read entire file
        data = f.read(7)
        print(data)
        count = 1
        for i in data:
            print(str(count) + " : "+i, end=", ")
            count += 1

        # If you want to see how much data left after reading 7 bytes
        # you can simply do like below
        # print("\n")
        # print(f.read())


if __name__ == '__main__':
    main()

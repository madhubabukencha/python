"""
Name       : Madhu Babu Kencha
Created on : 25-Nov-2018

The finally statement executes no matter about the try status
(either it passed or not). After completing or using a file or
network we have to close or disconnect them. In this situation
we use finally method. It will helps to close the file even
though there is any problem in file operation(like reading,
writing etc ..,)
"""


def main():
    try:
        file_object = open("sample.txt", "w+")
        file_object.write("Welcome to python exceptions")
    finally:
        file_object.close()

    print(file_object.closed)


if __name__ == '__main__':
    main()

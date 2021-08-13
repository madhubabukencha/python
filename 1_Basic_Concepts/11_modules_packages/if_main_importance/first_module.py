# print("First module's name : {} ".format(__name__))
import os
file_name = os.path.basename(__file__)


def main():
    print("First module's name : {} ".format(__name__))


if __name__ == "__main__":
    main()
    print(f"Hello, I will print whenever {file_name} executed directly")
else:
    print(f"Hello, I will print whenever {file_name} imported")

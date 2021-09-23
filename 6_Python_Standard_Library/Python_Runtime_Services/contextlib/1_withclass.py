"""
Date: 20-11-2020

Context Manager allows us to allocate and release resources precisely
when we want to. A common use case of context managers is locking and
unlocking resources and closing opened files

At the very least a context manager has an __enter__ and __exit__ method
defined. Let’s make our own file-opening Context Manager and learn the basics
"""


class OpenFile:

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file_object = open(self.file_name, self.mode)
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("Exception was caught")
        return self.file_object.close()


# whenever we call a class with "with" then __enter__() method gets called
# The unintended part is called the __exit__() method
with OpenFile("sample_text.txt", "w") as file:
    file.write("Welcome to Context Manager")
    # file.asdfsdf()

print(file.closed)

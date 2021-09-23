from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    try:
        file_obj = open(file_name, mode)
        # If you use return instead of yield you get below error
        # ValueError: I/O operation on closed file.
        # return file_obj
        yield file_obj
    finally:
        file_obj.close()


with open_file("sample_text.txt", "w") as f:
    print(type(f))
    f.write("Hello World")
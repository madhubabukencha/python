from contextlib import contextmanager
import os

@contextmanager
def change_directory(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

# Change path accordingly for your requirements
with change_directory(r"D:\Programming_Languages\Python\python_3.8.X\4_Advance_Concepts\top5_Property") as dire:
    print(os.listdir())

print(os.getcwd())
"""
Author      : Madhu Babu Kencha
created on  : 21-Nov-2018
"""
#!/usr/bin/env python3

# opening a file called sample with read, write and binary mode
file_object = open("sample.txt", "wb+")
print("Name of the file: ", file_object.name)
print("Mode of the file: ", file_object.mode)
print("Is it closed ?  : ", file_object.closed)
# Closing a file
file_object.close()
print("Is it closed ?  : ", file_object.closed)
"""
seek will set the position of the file Handle(cursor)

syntax
-----
Syntax: f.seek(offset, from_what), where f is file pointer

Parameters:
Offset: Number of positions to move forward
from_what: It defines point of reference(optional, and default is o)

The reference point is selected by the from_what argument. It accepts three values:

0: sets the reference point at the beginning of the file
1: sets the reference point at the current file position
2: sets the reference point at the end of the file

NOTE: for reading in binary format
https://stackoverflow.com/questions/21533391/seeking-from-end-of-file-throwing-unsupported-exception
"""
file_object = open("sample.txt", "rb")
data = file_object.read(5)
print(data)
# current position of file handler
print(F"Current cursor position: {file_object.tell()}")

# Moving back to the starting position
# file_object.seek(file_handler_position, 0-referring to start point)
# file_object.seek(0, 0)
# Moving 15 characters forward
# file_object.seek(15, 0)


# from_what 1 tell that file reference point at the current file
# position(in this case it is 5)
# Here you can see we set file handler set to 0 but still file handler position is 5
# file_object.seek(0, 1)


# from_what 2: sets the reference point at the end of the file
# So positive handler wouldn't have any impact. Need to use negative indexs
file_object.seek(-50, 2)

data = file_object.read()
print(data)


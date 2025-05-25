"""
If you want to last few bytes of a file, make sure you are
reading in binary mode.
"""
with open("read_end.txt", "rb") as file:
    # Move the cursor to the end of the file
    file.seek(-22, 2)
    print(file.read())
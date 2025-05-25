"""
In Python, StringIO is a class from the io module that
allows you to treat a string as a file-like object. This
means you can perform file operations like read(), write(),
seek(), etc., on an in-memory string buffer instead of an
actual file on disk.
"""
import io

# Create a StringIO object
string_io = io.StringIO()

# Write to the StringIO object
string_io.write("Hello, World!\n")
# Move the cursor to the beginning of the StringIO object
string_io.seek(0)
# Read from the StringIO object
content = string_io.read()
print(f"Content: {content}")
# Clear the StringIO object
# If this line is not included, then the next write will
# append to the existing content
string_io.truncate(0)

# Write more content to the StringIO object
string_io.write("Goodbye,\n World!\n")
string_io.seek(0)
content = string_io.read()
print(f"Content after truncation: {content}")

# other methods to get data from StringIO or buffer
string_io.seek(0)
print(f"StringIO content: {string_io.getvalue()}")
print(f"Readline method: {string_io.readline()}")
print(f"Readline method: {string_io.readline()}")

# Close the StringIO object
string_io.close()
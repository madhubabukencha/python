"""
About BytesIO:
BytesIO is a class in the io module of Python's standard
library that provides a convenient way to work with binary
data in memory as if it were a file. It allows you to read 
and write bytes to an in-memory buffer, making it useful for
scenarios where you need file-like behavior without actually
creating a physical file on disk.

Common use cases:
- Reading and writing binary data without disk I/O
- Simulating file operations in memory
- Handling binary data streams, such as images or audio files
"""
from io import BytesIO


bio = BytesIO()
# Write bytes to the BytesIO object
bio.write(b"Hello, World!\n")
bio.seek(0)  # Move the cursor to the beginning of the BytesIO object
data = bio.read()
print(f"Data read from BytesIO: {data}")
bio.close()

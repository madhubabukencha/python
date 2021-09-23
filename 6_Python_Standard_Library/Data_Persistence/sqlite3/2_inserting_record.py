"""
Name : Madhu Babu Kencha
Date : 26-03-2021
"""
import sqlite3


# Establishing connection
connection = sqlite3.connect("TEST.db")
# Preparing cursor
cursor = connection.cursor()
# Values
record = (123456, "Madhu Babu Kencha", 24, "M", 30000.0, "Kurnool")
# Inserting command, you can even use entire command in capitals letters
insert = "insert into EMPLOYEE values(?, ?, ?, ?, ?, ?)"
cursor.execute(insert, record)
connection.commit()
connection.close()



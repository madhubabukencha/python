"""
Name: Madhu Babu Kencha
Date: 28-03-2021

In this program we will learn how to insert multiple records to
"""
import sqlite3


# Establishing connection
connection = sqlite3.connect("TEST.db")
# Preparing cursor
cursor = connection.cursor()
# Records
records = [
    (120001, "Ravi Kiran", 40, "M", 40000.0, "Hyderabad"),
    (120002, "Max Well", 45, "M", 100000, "Africa"),
    (120003, "Sachin", 50, "M", 500050, "India")
]
insert_cmd = "INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_cmd, records)
connection.commit()
connection.close()


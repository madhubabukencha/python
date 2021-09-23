"""
Name: Madhu Babu Kencha
Date: 28-03-2021

In this program, we will learn how to fetch data from database
using multiple methods.
"""
import sqlite3
import pprint


# Establishing connection
connection = sqlite3.connect("TEST.db")
# Preparing cursor
cursor = connection.cursor()
fetch_cmd = "SELECT * FROM EMPLOYEE"
cursor.execute(fetch_cmd)

# Fetching single record
record = cursor.fetchone()
print(record, end="\n")

# If you want specified number of records
print("\nFETCHING 2 RECORDS:")
two_records = cursor.fetchmany(size=2)
pprint.pprint(two_records)

# Fetching all records
print("\nFETCHING ALL RECORDS:")
records = cursor.fetchall()
pprint.pprint(records)

connection.close()

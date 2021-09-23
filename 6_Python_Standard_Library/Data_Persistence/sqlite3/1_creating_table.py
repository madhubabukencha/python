"""
Name : Madhu Babu Kencha
Date : 26-03-2021
"""

import sqlite3


# Establishing database connection
connection = sqlite3.connect("TEST.db")
# Preparing cursor object
# The sqlite3.Cursor class is an instance using which
# you can invoke methods that execute SQLite statements,
# fetch data from the result sets of the queries
cursor = connection.cursor()
# Preparing SQL commands
drop_table = "DROP TABLE IF EXISTS EMPLOYEE"
create_table = """
              CREATE TABLE EMPLOYEE(
              EMPID INT(6) NOT NULL,
              NAME CHAR(20) NOT NULL,
              AGE INT,
              SEX CHAR(1),
              SALARY FLOAT,
              ADDRESS CHAR(60)
              )
"""
cursor.execute(drop_table)
cursor.execute(create_table)

connection.close()




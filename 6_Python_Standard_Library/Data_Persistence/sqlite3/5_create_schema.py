import os
import sqlite3


db_filename = "todo.db"
schema_filename = "todo_schema.sql"

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print("CREATING SCHEMA")
        with open(schema_filename, "rt") as f:
            schema = f.read()
        conn.executescript(schema)
        print("SCHEMA CREATED")
        print("INSERTING INITIAL DATA")
        conn.executescript("""
        insert into project (name, description, deadline)
        values ("TODO", "Application of TODO list", "2021-07-14");
        
        insert into task (details, status, deadline, project)
        values ("Create UI", "Done", "2021-4-13", "TODO");
        
        insert into task (details, status, deadline, project)
        values ("Create database", "Progress", "2021-4-20", "TODO");
        
        insert into task (details, status, deadline, project)
        values ("Fix Bugs", "New", "2021-5-20", "TODO");
        """)


    else:
        print("DATABASE EXITS, ASSUMES SCHEMA DOES TO")
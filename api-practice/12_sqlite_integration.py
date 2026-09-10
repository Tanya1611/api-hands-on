from fastapi import FastAPI
import sqlite3

'''
SQLite Database: A lightweight, file-based database that comes automatically built into Python, requiring no third-party library installation.
'''
conn = sqlite3.connect("test.db",check_same_thread=False)

# Cursor object is responsible for executing SQL queries
cursor = conn.cursor()

#---------------------------DB Connected-----------------------------------------

# Table creation

cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed TEXT
    )
""")

# Save the changes
conn.commit()

#conn -> DB
#cursor -> sql

app = FastAPI()

# Normal Route
@app.get("/")
def home():
    return {
        "message" : "SQLite connected fine!"
    }

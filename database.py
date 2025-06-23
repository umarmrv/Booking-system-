import sqlite3

def connect():
    return sqlite3.connect('office.db')

def init_db():
    with connect() as conn:
        with open('schema.sql') as f:
            conn.executescript(f.read())

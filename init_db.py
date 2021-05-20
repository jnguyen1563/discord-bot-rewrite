import sqlite3
from sqlite3 import Error

def create_connection(db):
    """ Create a connection to SQLite database, create a database if not exists """
    conn = None
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, table_sql):
    """
    Create the user table for SQLite database
    """
    try:
        c = conn.cursor()
        c.execute(table_sql)
    except Error as e:
        print(e)

def main():
    conn = create_connection(r'./databases/balances.db')

    table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        balance integer
    );"""

    if conn:
        create_table(conn, table_sql)
    else:
        print("Cannot create database")

if __name__ == '__main__':
    main()

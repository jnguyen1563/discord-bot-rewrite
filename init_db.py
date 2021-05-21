import sqlite3
from sqlite3 import Error

def create_database(table_name, table_sql):
    """
    Create a SQLite database
    :param table_name: The name used for the database table
    :param table_sql: The SQL commands used to create the table
    """
    conn = None
    try:
        conn = sqlite3.connect(fr'./databases/{table_name}.db')
        c = conn.cursor()
        c.execute(table_sql)
        print(f'Sucessfully created table {table_name}')
    except Error as e:
        print(f'Failed to create table {table_name}')
        print(e)

def main():

    balances_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        balance real,
        crypto real
    );"""

    create_database('balances', balances_sql)

if __name__ == '__main__':
    main()
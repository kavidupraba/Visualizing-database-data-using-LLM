import sqlite3 as sq

def check_db():
    conn = sq.connect("sample_database.db")
    cursor = conn.cursor()

    # Query to get the list of all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if tables:
        print("Tables in the database:")
        for table in tables:
            print(f"- {table[0]}")

            # Optional: Query each table to show its structure
            cursor.execute(f"PRAGMA table_info({table[0]});")
            columns = cursor.fetchall()
            print(f"Columns in {table[0]}: {columns}")
    else:
        print("No tables found in the database.")

    conn.close()

check_db()

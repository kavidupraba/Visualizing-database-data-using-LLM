import sqlite3 as sq
from store_schema import store_file


def handle_data(qry):
    conn=sq.connect("sample_database.db")
    cursor=conn.cursor()

    if qry != "No valid sql query found":
        print("Executing query:", qry)

        if "create table" in qry.lower():
            table_name = qry.lower().split("create table ")[1].split("(")[0].strip()
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            table_exists = cursor.fetchone()

            if table_exists:
                return None
            else:
                cursor.execute(qry)
                conn.commit()
                store_file()

        if qry.strip().lower().startswith("select"):
            cursor.execute(qry)
            result = cursor.fetchall()
            print(f"Query result: {result}")
            return result
        else:
            return None
    else:
        print("FAILED!!!! BOOOOO")

    conn.close()

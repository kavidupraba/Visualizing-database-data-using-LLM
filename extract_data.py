import sqlite3 as sq

def handle_data(qry):
    conn = sq.connect("sample_database.db")
    cursor = conn.cursor()
    if qry!="No valid sql query found":
        cursor.execute(qry)

        if qry.strip().lower().startswith("select"):
            result=cursor.fetchall()
            print(f"{result}")
            return result
        conn.commit()
    else:
        print("FAILD!!!! BOOOOO")
    conn.close()





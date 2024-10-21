import sqlite3 as sq

conn=sq.connect("sample_database.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM PRODUCT_SALES")
row = cursor.fetchall()
for r in row:
    print(r)

conn.close()


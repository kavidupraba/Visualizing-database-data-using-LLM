import sqlite3 as sq

conn=sq.connect("sample_database.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM Product_Sales")
#cursor.execute("DROP TABLE Product_Sales")
conn.commit()
row = cursor.fetchall()

for r in row:
    print(r)

conn.close()


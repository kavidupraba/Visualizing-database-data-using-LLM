import sqlite3 as sq

conn=sq.connect("sample_database.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM TEST")
#cursor.execute("DROP TABLE Sales_Data")
#conn.commit()
row = cursor.fetchall()

for r in row:
    print(r)

conn.close()


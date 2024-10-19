import sqlite3 as sq

conn=sq.connect("sample_database.db")
cursor=conn.cursor()

def get_table():
    cursor.execute("PRAGMA foreign_key=ON;")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables=cursor.fetchall()

    schema={}
    for table in tables:
        #print(table)#this will come as a tuple so we need to get the table name separately
        table_name=table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns=cursor.fetchall()
        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        fkey_list=cursor.fetchall()
        #print(fkey_list)#out put is like this:(0, 'orders', 'products', 'product_id', 'id'),  # (id, from_table, to_table, local_column, foreign_column)(1, 'invoices', 'customers', 'customer_id', 'id')
        fk_column={fk[3]:(fk[2],fk[4]) for fk in fkey_list} if fkey_list else {}
        #print(fk_column)
        #print(columns)
        #schema[table_name]=[(column[1],column[2]) for column in columns]# the output is like this:[(0, 'ID', 'INTEGER', 0, None, 1), so you have to get the column name!
        schema[table_name]=[]
        for column in columns:
            column_name=column[1]
            Data_type=column[2]
            Primary_key="PRIMARY KEY" if column[5]==1 else ''
            Foregin_key=f"FOREIGN KEY:(REFERENCE: ({fk_column[column_name][0]},{fk_column[column_name][1]}))"if column_name in fk_column else ""
            schema[table_name].append((column_name,Data_type,Primary_key,Foregin_key))




    return schema

get_table()
#print(db_schema)
#table_schema="\n".join(f"Table_name: {table} \n"+"\n".join(f"Column_name: {col[0]}, Data_type: {col[1]}, {col[2]} {col[3]}" for col in column) for table,column in db_schema.items() )
#print(table_schema)
#table_detail=get_table()
#print(table_detail)
#conn.close()
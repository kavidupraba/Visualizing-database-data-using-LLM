import json
from turning_table_to_text import get_table

def store_file():
    schema=get_table()
    with open("schema.json","w",encoding='utf-8') as f:
        json.dump(schema,f)

def get_file_data():
    store_file()
    with open("schema.json","r",encoding='utf-8') as f:
        schema_L=json.load(f)
    return schema_L

#Sales_Data
#store_file()
data=get_file_data()
print(data)
import re#re is python expresion that help to search through strings

# handling getting sql code part
def handle_response(response):
    match=re.search(r"```sql(.*?)```",response,re.DOTALL)# in here we get the qry that sarounded by ```sql``` that .*? is for that but
    #this selected group might be like this \nSELECT * FROM\n CUSTOMER\n and re.DOTALL will going to give us the lines i mean the lines tha
    # separate from each other "\n" if you not use this you will not going to get any!
    if match:
        sql_query=match.group(1).strip()#in here we get match.group will get the group of qury example \nSELECT * FROM CUSTOMER\n  do you see that
        #\n is gone now .strip() will remove any white space AND those remaining \n
        return sql_query
    else:
        return "No valid sql query found"

# handling creating chart part
def hadlie_repnse_c(response_c):
    match=re.search(r"```python(.*?)```",response_c,re.DOTALL)
    if match:
        py_code=match.group(1).strip()
        return py_code
    else:
        return "No valid pyton code"

import spacy
npl=spacy.load("en_core_web_sm")

def classify_user_input(user_input):
    doc=npl(user_input.lower())
    keyword_sql=["select", "from", "where", "count", "total", "query", "database","retrieve","create","add","delete","update"]

    #sql_detect=any(key in keyword_sql for key in doc)
    sql_detect=any(token.text in keyword_sql for token in doc)
    if sql_detect:
        return "sql"
    else:
        return "normal"

def classify_ai_response(response):
    doc_r=npl(response.lower())
    keyword_response_s="```sql"
    keyword_response_p="```python"
    if keyword_response_s in response:
        return "```sql"
    if keyword_response_p in response:
        return "```python"


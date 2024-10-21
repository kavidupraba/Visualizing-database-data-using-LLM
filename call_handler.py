from prompt_manager import genarate_prompts,genarate_prompts_c,genarate_prompts_w,genarate_prompt_s
from handling_response import handle_response,hadlie_repnse_c,get_explanation
from checking_user_input_and_response import classify_ai_response
from extract_data import handle_data
from showing_charts import show_ch
from turning_table_to_text import *

#buuilding first prompt
def create_fist_prompt(user_i):
    #schema=get_table()
    f_prompt=genarate_prompts(user_i)
    #conn.close()
    return f_prompt

#sending request to create chart for provided data that we retreved from data_base
def sending_chart_request(response):
    re=classify_ai_response(response)
    if re=="```sql":
       qry=handle_response(response)
       re_data=handle_data(qry)
       if re is not None:
          prompt_c=genarate_prompts_c(re_data)
       else:
          prompt_c=genarate_prompt_s()
       return prompt_c




def getting_information(response_c):
    Explanation = get_explanation(response_c)
    return Explanation


#showing the retreaved data in a chart
def showing_the_charts(response_c):
    re = classify_ai_response(response_c)
    if re=="```python":
        py_c=hadlie_repnse_c(response_c)
        show_ch(py_c)
    elif re=="```sql":
        qry = handle_response(response_c)
        handle_data(qry)


def prompt_without_sql_request(user_i):
    #schema=get_table()
    prompt_w=genarate_prompts_w(user_i)
    return prompt_w





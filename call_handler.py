from prompt_manager import genarate_prompts,genarate_prompts_c
from handling_response import handle_response,hadlie_repnse_c
from extract_data import handle_data
from showing_charts import show_ch
from turning_table_to_text import *

#buuilding first prompt
def create_fist_prompt(user_i):
    schema=get_table()
    f_prompt=genarate_prompts(schema,user_i)
    conn.close()
    return f_prompt

#sending request to create chart for provided data that we retreved from data_base
def sending_chart_request(response):
    qry=handle_response(response)
    re_data=handle_data(qry)
    prompt_c=genarate_prompts_c(re_data)
    return prompt_c

#showing the retreaved data in a chart
def showing_the_charts(respons_c):
    py_c=hadlie_repnse_c(respons_c)
    show_ch(py_c)



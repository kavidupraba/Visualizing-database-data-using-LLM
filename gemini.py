"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from gemi import *
from turning_table_to_text import *
from prompt_manager import genarate_prompts,genarate_prompts_c
from handling_response import handle_response,hadlie_repnse_c
from extract_data import handle_data
from showing_charts import show_ch
import json



#genai.configure(api_key=os.environ["GEMINI_API_KEY"])

genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)
user_i=input("Ask me somthing bro? ")
db_schema=get_table()
table_schema="\n".join(f"Table_name: {table} \n"+"\n".join(f"Column_name: {col[0]}, Data_type: {col[1]}, {col[2]} {col[3]}" for col in column) for table,column in db_schema.items() )
#print(table_schema)

prompt=genarate_prompts(table_schema,user_i)

response = chat_session.send_message(prompt)
qry=handle_response(response.text)
#print(qry)
re_data=handle_data(qry)
prompt_c=genarate_prompts_c(re_data)
response_c=chat_session.send_message(prompt_c)
py_c=hadlie_repnse_c(response_c.text)
show_ch(py_c)
print(response_c.text)
#print(response.text)
#print(response.json())
#qry=response["sql"]
#print(qry)
conn.close()

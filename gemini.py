"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from gemi import *
from turning_table_to_text import *
#from prompt_manager import genarate_prompts



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
print(table_schema)

prompt=f"this table is a Database table that created using sqlite3 in a python environment {table_schema} " \
       f"take a good look at this structure because following questions are base on this and here is the user input: {user_i} your task is to " \
       f"answer the question that user aks according to previously provided {table_schema} example: what is the qury to retreave all the " \
       f"items inside TEST table? answer SELECT * FROM TEST"




response = chat_session.send_message(prompt)
conn.close()
print(response.text)
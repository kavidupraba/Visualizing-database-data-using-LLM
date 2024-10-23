
import os
import google.generativeai as genai
from gemi import *
from call_handler import create_fist_prompt,sending_chart_request,showing_the_charts
from store_schema import get_file_data




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

schema=get_file_data()
print(schema)
chat_session = model.start_chat(
  history=[
    {"role": "user", "parts": "Here is the schema for the database you will be working with:"},
    {"role": "user", "parts": get_file_data()},
    {"role": "user", "parts": "Use this schema when answering questions related to database queries or structure."}
  ]
)
#user_i=input("Ask me somthing bro? ")


#prompt=create_fist_prompt(user_i)
#response = chat_session.send_message(prompt)
#prompt_c=sending_chart_request(response.text)

#response_c=chat_session.send_message(prompt_c)
#showing_the_charts(response_c.text)
cash_memory=[]
def __chat__(prompt):
  if cash_memory==[]:
    response = chat_session.send_message(prompt)
  else:
    fix_prompt="\n".join([f'{{"role":"{entry["role"]}","parts":"{entry["parts"]}"}}'for entry in cash_memory])
    fix_prompt+=prompt
    response=chat_session.send_message(fix_prompt)
    cash_memory.append({"role":"user","parts":f"{prompt}"})
    cash_memory.append({"role": "model", "parts": f"{response.text}"})


  return response.text
#print(response_c.text)



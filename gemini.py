
import os
import google.generativeai as genai
from gemi import *
from call_handler import create_fist_prompt,sending_chart_request,showing_the_charts




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
#user_i=input("Ask me somthing bro? ")


#prompt=create_fist_prompt(user_i)
#response = chat_session.send_message(prompt)
#prompt_c=sending_chart_request(response.text)

#response_c=chat_session.send_message(prompt_c)
#showing_the_charts(response_c.text)

def __chat__(prompt):
  response=chat_session.send_message(prompt)
  return response.text
#print(response_c.text)



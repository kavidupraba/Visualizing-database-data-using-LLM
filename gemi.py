import google.generativeai as genai
import os
import dotenv as dt

#dote_envpath=r"C:\Users\CS0064TX\Desktop\CS50\Perspective_of_data_science\Project\key.env"
dt.load_dotenv(dotenv_path=r"C:\Users\CS0064TX\Desktop\CS50\Perspective_of_data_science\Project\key.env")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

#print(GOOGLE_API_KEY)
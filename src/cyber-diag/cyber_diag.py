import os
from dotenv import load_dotenv, dotenv_values
import google.generativeai as genai

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
gemini_url = os.getenv("GEMINI_API_URL")

genai.configure(api_key=gemini_key)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("")

print(response.text)
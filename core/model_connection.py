import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
API_KEY = os.getenv("API_KEY")

def send_prompt(prompt, SYS_PROMPT):
    client = genai.Client(api_key=API_KEY)

    try:
        res = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=str(prompt),
            config=types.GenerateContentConfig(
                system_instruction=SYS_PROMPT,
                temperature=0.6
                )
            )
            
        return res.text
    except Exception as e:
        print("Deu erro: ", e)

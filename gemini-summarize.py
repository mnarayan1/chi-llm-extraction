import os
from dotenv import load_dotenv
import google.generativeai as genai

def gemini_abstractive():
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(model_name="gemini-pro")

    with open("input_1.txt", "r") as file:
        input_text = file.read()

    prompt = input_text + " In an accessible tone, summarize the above text."

    response = model.generate_content(prompt)

    return response.candidates[0].content.parts[0].text
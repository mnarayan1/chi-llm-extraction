import os
from dotenv import load_dotenv
import google.generativeai as genai
import textwrap

def gemini_abstractive(input_file, sources):
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(model_name="gemini-pro")

    with open(input_file, "r") as file:
        input_text = file.read()

    prompt = input_text + " In an accessible tone, summarize the above text."

    response = model.generate_content(prompt)

    print("generating abstractive summary")

    with open("final_summary.txt", 'w') as f:
        text = f"The following summary was generated from: {sources}" + "\n"
        text += response.candidates[0].content.parts[0].text
        f.write(textwrap.fill(text, width=100))

    print("finished generating abstractive summary")
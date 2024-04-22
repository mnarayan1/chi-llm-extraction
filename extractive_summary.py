from summarizer import Summarizer
import os
import re

def summarize_text(input_file):
    model = Summarizer()

    input_txt = os.path.join("converted_txt", input_file)
    with open(input_txt, 'r', encoding='utf-8') as file:
        text = file.read()

    summary = model(text, num_sentences=15)

    return summary

def summarize_paper_collection():
    print("creating extractive summaries, this will take a moment")
    txt_files = []
    txt_summaries = []
    for filename in os.listdir('converted_txt'):
        if filename.endswith('.txt'):
            txt_files.append(filename)

    for txt_file in txt_files:
        print(f"currently summarizing {txt_file}")
        txt_summaries.append(summarize_text(txt_file))
        print(f"finished summarizing {txt_file}")

    all_summaries = ''.join(txt_summaries)

    with open("output.txt", 'w') as f:
        f.write(all_summaries)

    print("created extractive summaries")
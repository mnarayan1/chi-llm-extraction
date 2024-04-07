from summarizer import Summarizer
import os
import re

def summarize_text(input_file):
    model = Summarizer()

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    summary = model(text, num_sentences=15)

    return summary

def summarize_paper_collection():
    txt_files = []
    txt_summaries = []
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            txt_files.append(filename)

    for txt_file in txt_files:
        txt_summaries.append(summarize_text(txt_file))

    return txt_summaries
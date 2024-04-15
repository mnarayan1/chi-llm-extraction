import re
import os

def remove_citations_and_links(text):
    citation_pattern = r'\d+\.\s*[^.]+\.'
    link_pattern = r'\[https?:\/\/(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?\]|\[http?:\/\/(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?\]|\[http?:\/\/(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)? [^\]]+\]|\[https?:\/\/(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)? [^\]]+\]'
    
    text = re.sub(citation_pattern, '', text)
    text = re.sub(link_pattern, '', text)
    
    last_index = max(text.rfind("References"), text.rfind("REFERENCES"), text.rfind("Citations"), text.rfind("citations"))
    if last_index != -1:
        return text[:last_index]
    return text

def clean_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    cleaned_content = remove_citations_and_links(content)

    with open(output_file, 'w') as f:
        f.write(cleaned_content)

def process_txt():
    for file_name in os.listdir("converted_txt"):
        if file_name.endswith(".txt"):
            input_file = os.path.join("converted_txt", file_name)
            clean_file(input_file, input_file)
    print("All files processed.")
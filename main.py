from pdftxt import pdf_to_txt
from cleantxt import process_txt
from extractive_summary import summarize_paper_collection
from gemini_summarize import gemini_abstractive

def main():
    print("Input your sources separated by a comma: ")
    sources = input()

    pdf_to_txt() # output converted txt files to converted_txt folder
    process_txt() # removing citations and most links
    summarize_paper_collection() # summarize from relevent papers
    gemini_abstractive("output.txt", sources)

if __name__ == "__main__":
    main()

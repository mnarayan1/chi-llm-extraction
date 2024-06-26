from pdfreader import SimplePDFViewer
import os

def convert_pdf_to_txt(pdf_path, txt_path):
    viewer = SimplePDFViewer(open(pdf_path, 'rb'))
    
    text_content = ""
    
    with open(pdf_path, 'rb') as file:
        for canvas in viewer:
            text_content += ''.join(canvas.strings)
    
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text_content)

def pdf_files_to_convert():
    pdf_paths = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdf_paths.append(filename)
    
    for pdf_path in pdf_paths:
        print(pdf_path)
    
    return pdf_paths
        

def pdf_to_txt():
    pdf_names = pdf_files_to_convert()

    output_folder = "converted_txt"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for pdf_name in pdf_names:
        output_name = os.path.join(output_folder, os.path.splitext(os.path.basename(pdf_name))[0] + '.txt')
        print(f"now converting {pdf_name}")
        convert_pdf_to_txt(pdf_name, output_name)

    print("PDF converted to text successfully, output files in converted_txt")
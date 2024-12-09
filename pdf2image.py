import os
import sys
import fitz  # PyMuPDF

def convert_pdf_to_images(pdf_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        
        # Create an output folder named after the PDF file (excluding extension)
        output_folder = os.path.splitext(pdf_path)[0]
        os.makedirs(output_folder, exist_ok=True)

        # Convert each page to an image
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pix = page.get_pixmap()
            output_file = os.path.join(output_folder, f"page_{page_number + 1}.png")
            pix.save(output_file)

        pdf_document.close()
        print(f"Successfully converted: {pdf_path}")
    except Exception as e:
        print(f"Failed to convert {pdf_path}: {e}")

def process_input(input_path):
    if os.path.isfile(input_path) and input_path.lower().endswith('.pdf'):
        # Input is a single PDF file
        convert_pdf_to_images(input_path)
    elif os.path.isdir(input_path):
        # Input is a folder, process all PDF files in the folder
        for file_name in os.listdir(input_path):
            file_path = os.path.join(input_path, file_name)
            if file_name.lower().endswith('.pdf'):
                convert_pdf_to_images(file_path)
    else:
        print("Invalid input. Please provide a PDF file or a folder containing PDF files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    process_input(input_path)

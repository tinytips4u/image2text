# Image To Text
Convert image to text using Python (Tesseract OCR)

A. Image to Text:
1. Python should be installed on your system. If it is not installed then you can install Anaconda from [here](https://www.anaconda.com/download/success).
2. Install Tesseract OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki).
3. Run the command: `pip install pytesseract pillow` <br />
Check if the requirement is satisfied or not. If not then the above command will install the package.<br />
4. Command to check which language codes Tesseract OCR identifies:
   `tesseract --list-langs`
5. Syntax to run the image2Text.py is:<br />
   `python image2Text.py path-to-input-image-or-folder path-of-output-folder --languages language-code`

B. If you want to merge all the text files into a single text file then use merge-text.bat <br />
Syntax: <br />
`merge-text.bat path-to-folder-containing-text-files` <br />
It will create the merged text file in the same location that contains the text files. <br />

C. If you want to convert pages of a pdf file or multiple pdf files to images then use pdf2image.py <br />
1. Run the command: `pip install pymupdf` <br />
2. It takes the input argument as a path to a single pdf file or a path to a folder containing multiple pdf files. <br />
3. It does not require an argument to define the output path. It will automatically create folders as per the name of the pdf file and store it's converted pages as images there. the output folder will be created in the same place where the pdf is located. <br />
Syntax: <br />
`pdf2image.py path-to-pdf-or-folder-containing-pdf`

import os
import pytesseract
from PIL import Image
import glob

def ocr_image(image_path, output_path, languages='eng'):
    """ Convert image to text and save it to a text file. """
    try:
        # Open image
        img = Image.open(image_path)

        # Run Tesseract OCR on the image
        text = pytesseract.image_to_string(img, lang=languages)

        # Save the text to a file
        base_name = os.path.basename(image_path)
        text_file_name = os.path.splitext(base_name)[0] + '.txt'
        text_file_path = os.path.join(output_path, text_file_name)

        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"Processed {image_path} -> {text_file_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_images(input_path, output_path, languages='eng'):
    """ Process a single image or all images in a directory. """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Check if input_path is a file or directory
    if os.path.isdir(input_path):
        # Process all images in the directory
        image_files = glob.glob(os.path.join(input_path, '*.*'))
        image_files = [f for f in image_files if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        
        for image_file in image_files:
            ocr_image(image_file, output_path, languages)
    
    elif os.path.isfile(input_path):
        # Process a single image file
        ocr_image(input_path, output_path, languages)
    else:
        print(f"Invalid input path: {input_path}")

if __name__ == "__main__":
    import argparse

    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Convert images to text using OCR.')
    parser.add_argument('input', help='Path to a single image or a directory of images')
    parser.add_argument('output', help='Directory to save the output text files')
    parser.add_argument('--languages', default='eng', help='Comma-separated list of languages to use in OCR (default: eng)')

    args = parser.parse_args()

    # Run the OCR processing
    process_images(args.input, args.output, args.languages)

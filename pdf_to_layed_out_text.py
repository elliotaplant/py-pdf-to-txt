# pdf_to_layed_out_text.py
import pdftotext
import pytesseract
from pdf2image import convert_from_path
from pytesseract import TesseractError


def pdf_to_layed_out_text(pdf_path):
    # Attempt to read the PDF with pdftotext into layed out text
    with open(pdf_path, "rb") as file:
        try:
            # Use pdftotext to extract text with layout preservation
            pdf = pdftotext.PDF(file, physical=True)

            # If the read was successful
            if pdf:
                # Combining all pages' text with new lines
                text = "\n\n".join(pdf)

                # If the output is layed out, utf8 text (checking if the text isn't empty)
                if text.strip():
                    return text
        except RuntimeError as e:
            print(f"Error with pdftotext: {e}")

    # Attempt to read the PDF with pytesseract into layed out text
    try:
        # Convert the PDF into a list of images
        images = convert_from_path(pdf_path)

        # Extract text from each image
        # texts = [pytesseract.image_tostring(image) for image in images]

        # Combine text from all images
        # text = "\n\n".join(texts)

        # HOCR example
        texts = [str(pytesseract.image_to_pdf_or_hocr(
            image, extension='hocr'), encoding='utf-8') for image in images]

        # Combine text from all images
        text = "\n\n".join(texts)

        # If the read was successful
        if text and text.strip():
            return text

    except TesseractError as e:
        print(f"Error with pytesseract: {e}")

    return "Failed to extract text."

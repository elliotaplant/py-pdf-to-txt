# pdf_to_layed_out_text.py
import pdftotext
import pytesseract
from pdf2image import convert_from_path
from pytesseract import TesseractError
from hocr_to_text import hocr_to_text


def pdf_to_layed_out_text(pdf_path, metadata, ocr, hocr):
    # Attempt to read the PDF with pdftotext into layed out text
    if metadata:
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

        config = '--psm 6 -c preserve_interword_spaces=1'
        if ocr:
            # Text example
            # Extract text from each image while trying to maintain layout
            texts = [pytesseract.image_to_string(
                image, config=config) for image in images]

            # Combine text from all images
            text = "\n\n".join(texts)

        elif hocr:
            # PDF => hocr -> text
            hocr_outputs = [pytesseract.image_to_pdf_or_hocr(
                image, extension='hocr', config=config) for image in images]

            decoded_hocrs = [str(hocr_output, encoding='utf-8')
                             for hocr_output in hocr_outputs]

            # Convert each hOCR output to text format with layout preservation
            texts = [hocr_to_text(decoded_hocr)
                     for decoded_hocr in decoded_hocrs]

            # Combine text from all images
            text = "\n\n".join(texts)

        # If the read was successful
        if text and text.strip():
            return text

    except TesseractError as e:
        print(f"Error with pytesseract: {e}")

    raise RuntimeError("Failed to extract text")

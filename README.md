# PDF Text Extractor

Extract text from a PDF file while attempting to maintain its layout. This tool offers various methods of extraction, including metadata extraction, OCR, and hOCR.

## Dependencies

Install the required packages with:
```
pip install -r requirements.txt
```


### Other Dependencies

You'll need to install `poppler` and `tesseract` on your machine

#### macOS with homebrew:
```
brew install poppler
brew install tesseract
```

#### Linux:

Depending on your distribution, you can install `poppler` and `tesseract` using your package manager. Here's an example for Debian/Ubuntu:

```
sudo apt-get install poppler-utils
sudo apt-get install tesseract-ocr
```

## Usage

You can use the `pdf_text_extractor.py` script to extract text from a PDF:

```
python pdf_text_extractor.py <path_to_pdf> <path_to_output_txt> [--metadata] [--ocr] [--hocr]
```

**Arguments:**
- `<path_to_pdf>`: Path to the source PDF file.
- `<path_to_output_txt>`: Path to the desired output text file.

**Optional Flags:**
- `--metadata`: Use text metadata extraction with layout preservation. Enabled by default.
- `--ocr`: Use OCR with layout preservation. Enabled by default.
- `--hocr`: Use hOCR with layout preservation. Enabled by default.

If multiple flags are enabled, the program will try to extract text using each method in order until successful.

## Methods of Extraction

1. **Metadata Extraction (`--metadata`)**
   Attempts to extract the text from the PDF's metadata while preserving the layout.

2. **OCR (`--ocr`)**
   Converts the PDF into a list of images and then uses OCR (Optical Character Recognition) to extract text from the images. This method tries to maintain the layout of the text.

3. **hOCR (`--hocr`)**
   Converts the PDF into a list of images and then uses hOCR (a format for representing OCR output) to extract text from the images. The hOCR output is then transformed into a text format with layout preservation.

## Notes

- The tool uses the `pdftotext`, `pdf2image`, and `pytesseract` libraries to perform text extraction.
- The `hocr_to_text.py` utility converts hOCR content into a text format with layout preservation.
- The quality and layout fidelity of the extracted text depend on the PDF's contents, structure, and the method used for extraction.

## Contributing

Contributions are welcome! Please submit a pull request or create an issue if you find a bug or have a feature request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

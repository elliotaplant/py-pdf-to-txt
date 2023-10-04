# pdf_text_extractor.py
import argparse
from pdf_to_layed_out_text import pdf_to_layed_out_text


def main():
    parser = argparse.ArgumentParser(description='Extract text from a PDF.')
    parser.add_argument('pdf_file', type=str, help='Path to the PDF file.')
    parser.add_argument('output_file', type=str,
                        help='Path to the output text file.')
    parser.add_argument('--metadata', default=True, action=argparse.BooleanOptionalAction,
                        help='Try text metadata extraction with layout preservation')
    parser.add_argument('--ocr', default=True, action=argparse.BooleanOptionalAction,
                        help='Try OCR with layout preservation')
    parser.add_argument('--hocr', default=True, action=argparse.BooleanOptionalAction,
                        help='Try hOCR with layout preservation')

    args = parser.parse_args()

    # Extract text
    extracted_text = pdf_to_layed_out_text(
        args.pdf_file, metadata=args.metadata, ocr=args.ocr, hocr=args.hocr)

    # Save to output file
    with open(args.output_file, 'w') as file:
        file.write(extracted_text)


if __name__ == "__main__":
    main()

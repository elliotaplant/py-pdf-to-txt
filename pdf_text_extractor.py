# pdf_text_extractor.py
import argparse
from pdf_to_layed_out_text import pdf_to_layed_out_text


def main():
    parser = argparse.ArgumentParser(description='Extract text from a PDF.')
    parser.add_argument('pdf_file', type=str, help='Path to the PDF file.')
    parser.add_argument('output_file', type=str,
                        help='Path to the output text file.')

    args = parser.parse_args()

    # Extract text
    extracted_text = pdf_to_layed_out_text(args.pdf_file)

    # Save to output file
    with open(args.output_file, 'w') as file:
        file.write(extracted_text)


if __name__ == "__main__":
    main()

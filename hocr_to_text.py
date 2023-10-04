from bs4 import BeautifulSoup


def extract_bbox(title):
    """Extract bounding box from title attribute in hOCR"""
    return [int(val.strip(';')) for val in title.split(' ')[1:5]]


def hocr_to_text(hocr_content):
    # Parse the hOCR content using BeautifulSoup
    soup = BeautifulSoup(hocr_content, 'html.parser')

    # Process each ocr_line
    lines = soup.find_all(class_='ocr_line')

    text_output = []

    prev_bbox = None
    for line in lines:
        words = line.find_all(class_='ocrx_word')
        if not words:
            continue

        # Convert bounding boxes and content to a line of text
        line_text = ""
        for idx, word in enumerate(words):
            if idx > 0:
                bbox_curr = extract_bbox(word['title'].split(';')[0])
                bbox_prev = extract_bbox(words[idx - 1]['title'].split(';')[0])

                # Adjust the constant if necessary
                space_count = int((bbox_curr[0] - bbox_prev[2]) / 10)
                line_text += ' ' * space_count

            line_text += word.get_text()

        # Insert empty lines if there's a significant gap in y-coordinates
        if prev_bbox:
            line_bbox = extract_bbox(line['title'])
            y_diff = line_bbox[1] - prev_bbox[3]

            # This threshold determines when to insert an empty line
            if y_diff > 50:  # Adjust the threshold based on your needs
                empty_lines_count = y_diff // 50
                for _ in range(empty_lines_count):
                    text_output.append(' ' * len(line_text)
                                       )  # A line of spaces

        text_output.append(line_text)
        prev_bbox = extract_bbox(line['title'])

    return '\n'.join(text_output)

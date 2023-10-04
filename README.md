# tesseract Ideas

- tesseract is a cpp tool that can do OCR
  - pytesseract is a convenient python wrapper
  - It appears that it can make hOCR and/or text directly
- pdftotext is a python library that just does pdf to text

- The workflow could be:
  - Get layed-out-text
    - Try pdftotext
      - if no error
        - return layed out text?
    - Try pytesseract to layed out text?
      - if no error
        - return layed out text?
    - Try pytesseract to hOCR?
      - Figure out how to turn hOCR to layed out text

## Installation stuff

first I tried to do 
```
pip install pdftotext pytesseract
```
But that failed with
```
...
pdftotext.cpp:3:10: fatal error: 'poppler/cpp/poppler-document.h' file not found
...
```
So then I did

```
brew install poppler
```
I also did
```
brew install tesseract
```

from PyPDF2 import PdfFileReader
from fpdf import FPDF
from pathlib import Path


def get_string(img_path="../data/keppel-corporation-limited-annual-report-2018.pdf", page=12):
    """Extract text from pdf or image"""

    # Create pdf reader object
    pdf = PdfFileReader(img_path)
    print(pdf.getPageLayout())

    # grab the page number
    page_number = pdf.getPage(page-1)

    # Extract the text from the page object
    page_text = page_number.extract_text().replace(" \n", " ").replace(".\n", ".\n").replace("\n", "\n")

    # Write the text to file
    with Path('../output/output.csv').open(mode='w') as output_file:
        output_file.write(page_text)
    # Combine the text into single and save as a .csv file

    return page_text
    

get_string()
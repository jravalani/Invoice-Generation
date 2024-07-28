from fpdf import FPDF
import pandas as pd
import glob
import pathlib as path

filepaths = glob.glob("Text+Files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:

    pdf.add_page()

    # extracting filename from filepath
    filename = path.Path(filepath).stem.capitalize()

    # adding to the page
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=10, txt=filename, ln=1)

    # opening txt file
    with open(filepath, 'r') as file:
        content = file.read()

    # add the content to the pdf
    pdf.set_font(family="Times", size=12)
    lines = content.split('\n')
    for line in lines:
        pdf.multi_cell(w=0, h=5, txt=line)

pdf.output(f"Student_Exercise_PDFs/output.pdf")
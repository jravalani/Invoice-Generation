import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# using glob the get particular filepaths from a folder
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # extracting the filename using pathlib
    filename = Path(filepath).stem
    invoice_no = filename.split("-")[0]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}")
    pdf.output(f"PDFs/{filename}.pdf")
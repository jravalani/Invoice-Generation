import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# using glob the get particular filepaths from a folder
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # extracting the filename using pathlib
    filename = Path(filepath).stem
    invoice_no, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]

    # adding header of the table
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=str(columns[0]), border=1)
    pdf.cell(w=60, h=8, txt=str(columns[1]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[4]), border=1, ln=1)

    # adding table values
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30, h=8, txt=" ", border=1)
    pdf.cell(w=60, h=8, txt=" ", border=1)
    pdf.cell(w=30, h=8, txt=" ", border=1)
    pdf.cell(w=30, h=8, txt=" ", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # adding company name and logo
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)
    pdf.cell(w=30, h=8, txt=f"Company")

    pdf.output(f"PDFs/{filename}.pdf")
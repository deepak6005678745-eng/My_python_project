from fpdf import FPDF
from datetime import date

naam = ("")
din = 
rate = 
total = din * rate
aaj = date.today()

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", 'B', 16)
pdf.cell(190, 10, txt="BHAI KA OFFICIAL HISAB", ln=1, align='C')

pdf.set_font("Arial", size=10)
pdf.cell(190, 10, txt=f"Tarikh: {aaj}", ln=1, align='R')
pdf.ln(5)

pdf.set_font("Arial", size=12)
pdf.cell(190, 10, txt=f" Naam: {naam}", ln=1, border=1)
pdf.cell(190, 10, txt=f" Kul Din: {din}", ln=1, border=1)
pdf.cell(190, 10, txt=f" Rate: Rs. {rate}", ln=1, border=1)

pdf.set_font("Arial", 'B', 14)
pdf.cell(190, 12, txt=f" TOTAL PAYMENT: Rs. {total}", ln=1, border=1)

pdf.output(f"{naam}_Report.pdf")
print(f"Report Ban Gayi: {naam}_Report.pdf")

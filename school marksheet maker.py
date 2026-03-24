from fpdf import FPDF
from datetime import datetime

print("--- STUDENT DATA ENTRY ---")
naam = int(input("aapka naam"))
roll_no  = int(input("aapke marks"))
maths = int(input("aapke marks"))
science = int(input("aapke marks"))
english = int(input("aapke marks"))
hindi = int(input("aapke marks"))

total = maths + science + english + hindi
percentage = round(total / 4, 2)
tarikh = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

if percentage > 33:
    status = "PASSED"
else:
    status = "FAILED"


pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", 'B', size=16)
pdf.cell(200, 10, txt="OFFICIAL REPORT CARD", ln=1, align='C')
pdf.set_font("Arial", size=10)
pdf.cell(200, 10, txt=f"Generated on: {tarikh}", ln=1, align='R')
pdf.ln(5)

pdf.set_font("Arial", 'B', size=12)
pdf.cell(100, 10, txt=f"Name: {naam}", ln=0)
pdf.cell(100, 10, txt=f"Roll No: {roll_no}", ln=1)
pdf.ln(5)

pdf.cell(95, 10, "Subject", border=1, align='C')
pdf.cell(95, 10, "Marks", border=1, ln=1, align='C')

pdf.set_font("Arial", size=12)
subjects = [["Mathematics", maths], ["Science", science], ["English", english], ["Hindi", hindi]]

for sub in subjects:
    pdf.cell(95, 10, sub[0], border=1, align='C')
    pdf.cell(95, 10, str(sub[1]), border=1, ln=1, align='C')

pdf.set_font("Arial", 'B', size=12)
pdf.cell(95, 10, "GRAND TOTAL", border=1, align='C')
pdf.cell(95, 10, f"{total} / 400", border=1, ln=1, align='C')
pdf.ln(10)

pdf.cell(100, 10, txt=f"Percentage: {percentage}%", ln=0)
pdf.cell(100, 10, txt=f"Final Result: {status}", ln=1)

file_name = f"{naam}_Result.pdf"
pdf.output(file_name)

print("---------------------------------")
print(f"Mubarak ho! {file_name} ban gayi hai.")
print("---------------------------------")
    
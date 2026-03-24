from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Bhai Ka Digital Report", ln=1, align='C')
pdf.cell(200, 10, txt="-----------------------------------", ln=2, align='C')

naam = "
kaam_din = ""
payment = ""

pdf.cell(200, 10, txt=f"Mazdoor ka Naam: {naam}", ln=3, align='L')
pdf.cell(200, 10, txt=f"Kul Din: {kaam_din}", ln=4, align='L')
pdf.cell(200, 10, txt=f"Total Payment: Rs. {payment}", ln=5, align='L')

pdf.output("Bhai_Ki_Report.pdf")

print("Mubarak ho bhai! PDF ban gayi hai. Mobile storage mein check karo.")

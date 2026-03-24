import tkinter as tk
from tkinter import messagebox, ttk
from fpdf import FPDF
from datetime import datetime
import csv
import os

salary_records = []

def add_employee_data():
    try:
        name = entry_name.get()
        base_salary = float(entry_base_salary.get())
        days_present = int(entry_days.get())
        month = entry_month.get()

        if not name or not month:
            messagebox.showwarning("Warning", "Naam aur Mahina likhna zaroori hai!")
            return

        per_day = base_salary / 30
        final_salary = round(per_day * days_present, 2)

        salary_records.append([name, month, base_salary, days_present, final_salary])
        tree.insert("", tk.END, values=(name, month, days_present, final_salary))

        entry_name.delete(0, tk.END)
        entry_base_salary.delete(0, tk.END)
        entry_days.delete(0, tk.END)
        entry_name.focus()

    except ValueError:
        messagebox.showerror("Error", "Salary aur Days mein sahi number daalo!")

def generate_salary_report():
    if not salary_records:
        messagebox.showwarning("Warning", "Pehle employee data add karo!")
        return

    report_no = datetime.now().strftime("%Y%m%d%H%M")
    date_str = datetime.now().strftime("%d-%m-%Y")

    pdf = FPDF()
    pdf.add_page()

    pdf.set_text_color(0, 51, 153)
    pdf.set_font("Arial", 'B', size=22)
    pdf.cell(200, 20, txt="MONTHLY SALARY REPORT", ln=1, align='C')

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=10)
    pdf.cell(100, 10, f"Report ID: {report_no}")
    pdf.cell(100, 10, f"Generated On: {date_str}", ln=1, align='R')
    pdf.ln(10)

    pdf.set_text_color(0, 51, 153)
    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(50, 10, "Employee Name", border=1, align='C')
    pdf.cell(30, 10, "Month", border=1, align='C')
    pdf.cell(40, 10, "Base Salary", border=1, align='C')
    pdf.cell(30, 10, "Present", border=1, align='C')
    pdf.cell(40, 10, "Net Payable", border=1, ln=1, align='C')

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=10)

    for row in salary_records:
        pdf.cell(50, 10, f" {row[0]}", border=1)
        pdf.cell(30, 10, f"{row[1]}", border=1, align='C')
        pdf.cell(40, 10, f"{row[2]}", border=1, align='C')
        pdf.cell(30, 10, f"{row[3]} Days", border=1, align='C')
        pdf.cell(40, 10, f"{row[4]}", border=1, ln=1, align='C')

    pdf.output(f"Salary_Report_{report_no}.pdf")

    with open("salary_database.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for row in salary_records:
            writer.writerow([date_str] + row)

    messagebox.showinfo("Success", "Monthly Salary Data Saved and PDF Generated!")
    salary_records.clear()
    for i in tree.get_children():
        tree.delete(i)

root = tk.Tk()
root.title("Office Salary Management")
root.geometry("600x700")

tk.Label(root, text="EMPLOYEE SALARY SYSTEM", font=("Arial", 16, "bold"), fg="darkblue").pack(pady=15)

tk.Label(root, text="Employee Name:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

tk.Label(root, text="Month (e.g. March 2026):").pack()
entry_month = tk.Entry(root, width=40)
entry_month.pack(pady=5)

tk.Label(root, text="Full Monthly Salary (Base):").pack()
entry_base_salary = tk.Entry(root, width=40)
entry_base_salary.pack(pady=5)

tk.Label(root, text="Total Days Present:").pack()
entry_days = tk.Entry(root, width=40)
entry_days.pack(pady=5)

tk.Button(root, text="ADD TO MONTHLY LIST", command=add_employee_data, bg="orange", font=("Arial", 10, "bold"), width=30).pack(pady=15)

columns = ("Name", "Month", "Days", "Final Salary")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor='center')
tree.pack(pady=10)

tk.Button(root, text="GENERATE MONTHLY PDF", command=generate_salary_report, bg="darkblue", fg="white", font=("Arial", 11, "bold"), width=35).pack(pady=20)

root.mainloop()

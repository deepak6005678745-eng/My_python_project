import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime
import csv
import os

def generate_invoice():
    try:
        client = entry_client.get()
        item = entry_item.get()
        price = float(entry_price.get())
        qty = int(entry_qty.get())
        
        if not client or not item:
            messagebox.showwarning("Warning", "Data bharna zaroori hai!")
            return

        total_amount = price * qty
        date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        invoice_no = datetime.now().strftime("%Y%m%d%H%M")

        file_exists = os.path.isfile("office_records.csv")
        with open("office_records.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Date", "Invoice No", "Client", "Item", "Price", "Qty", "Total"])
            writer.writerow([date_str, invoice_no, client, item, price, qty, total_amount])

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=20)
        pdf.cell(200, 15, txt="OFFICE INVOICE", ln=1, align='C')
        
        pdf.set_font("Arial", size=12)
        pdf.ln(10)
        pdf.cell(100, 10, f"Invoice No: {invoice_no}")
        pdf.cell(100, 10, f"Date: {date_str}", ln=1, align='R')
        
        pdf.ln(10)
        pdf.cell(100, 10, "Description", border=1)
        pdf.cell(30, 10, "Price", border=1)
        pdf.cell(20, 10, "Qty", border=1)
        pdf.cell(40, 10, "Total", border=1, ln=1)

        pdf.cell(100, 10, f"{item}", border=1)
        pdf.cell(30, 10, f"{price}", border=1)
        pdf.cell(20, 10, f"{qty}", border=1)
        pdf.cell(40, 10, f"{total_amount}", border=1, ln=1)

        pdf.ln(10)
        pdf.set_font("Arial", 'B', size=14)
        pdf.cell(0, 10, f"Grand Total: Rs. {total_amount}", ln=1, align='R')

        pdf.output(f"Invoice_{invoice_no}.pdf")
        
        messagebox.showinfo("Success", "Record Saved and PDF Generated!")
        
        entry_client.delete(0, tk.END)
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Price aur Qty sahi daalo!")

root = tk.Tk()
root.title("Office System")
root.geometry("400x450")

tk.Label(root, text="DATA ENTRY PANEL", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(root, text="Client Name:").pack()
entry_client = tk.Entry(root, width=40)
entry_client.pack(pady=5)

tk.Label(root, text="Item:").pack()
entry_item = tk.Entry(root, width=40)
entry_item.pack(pady=5)

tk.Label(root, text="Price:").pack()
entry_price = tk.Entry(root, width=40)
entry_price.pack(pady=5)

tk.Label(root, text="Quantity:").pack()
entry_qty = tk.Entry(root, width=40)
entry_qty.pack(pady=5)

tk.Button(root, text="SAVE & PRINT", command=generate_invoice, bg="blue", fg="white", width=20).pack(pady=30)

root.mainloop()

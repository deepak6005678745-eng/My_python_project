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
        
        pdf.set_text_color(0, 51, 153) 
        pdf.set_font("Arial", 'B', size=24)
        pdf.cell(200, 20, txt="OFFICE INVOICE", ln=1, align='C')
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=10)
        pdf.ln(5)
        pdf.cell(100, 10, f"Invoice No: {invoice_no}")
        pdf.cell(100, 10, f"Date: {date_str}", ln=1, align='R')
        pdf.cell(0, 10, f"Client: {client}", ln=1)
        
        pdf.ln(10)
        
        pdf.set_text_color(0, 51, 153)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(100, 10, "Description", border=1, align='C')
        pdf.cell(30, 10, "Price", border=1, align='C')
        pdf.cell(20, 10, "Qty", border=1, align='C')
        pdf.cell(40, 10, "Total", border=1, ln=1, align='C')

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=11)
        pdf.cell(100, 10, f" {item}", border=1)
        pdf.cell(30, 10, f"{price}", border=1, align='C')
        pdf.cell(20, 10, f"{qty}", border=1, align='C')
        pdf.cell(40, 10, f"{total_amount}", border=1, ln=1, align='C')

        pdf.ln(10)
        pdf.set_font("Arial", 'B', size=14)
        pdf.set_text_color(0, 51, 153)
        pdf.cell(0, 10, f"Grand Total: Rs. {total_amount} ", ln=1, align='R')

        pdf.output(f"Invoice_{invoice_no}.pdf")
        
        messagebox.showinfo("Success", "Blue Invoice Generated!")
        
        entry_client.delete(0, tk.END)
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Price aur Qty sahi daalo!")

root = tk.Tk()
root.title("Blue Office System")
root.geometry("400x450")

tk.Label(root, text="OFFICE DATA ENTRY", font=("Arial", 14, "bold"), fg="blue").pack(pady=20)

tk.Label(root, text="Client Name:").pack()
entry_client = tk.Entry(root, width=40)
entry_client.pack(pady=5)

tk.Label(root, text="Item Description:").pack()
entry_item = tk.Entry(root, width=40)
entry_item.pack(pady=5)

tk.Label(root, text="Price per Unit:").pack()
entry_price = tk.Entry(root, width=40)
entry_price.pack(pady=5)

tk.Label(root, text="Quantity:").pack()
entry_qty = tk.Entry(root, width=40)
entry_qty.pack(pady=5)

tk.Button(root, text="GENERATE BLUE INVOICE", command=generate_invoice, bg="darkblue", fg="white", font=("Arial", 10, "bold"), width=25).pack(pady=30)

root.mainloop()

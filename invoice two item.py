import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime
import csv
import os

items_list = []

def add_item():
    try:
        item = entry_item.get()
        price = float(entry_price.get())
        qty = int(entry_qty.get())
        
        if not item:
            messagebox.showwarning("Warning", "Item ka naam bharna zaroori hai!")
            return

        total = price * qty
        items_list.append([item, price, qty, total])
        
        messagebox.showinfo("Success", f"{item} list mein jud gaya hai!")
        
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Price aur Qty sahi daalo!")

def finalize_pdf():
    if not items_list:
        messagebox.showwarning("Warning", "Pehle Add Item button se saaman jodo!")
        return
        
    client = entry_client.get()
    if not client:
        messagebox.showwarning("Warning", "Client ka naam likho!")
        return

    invoice_no = datetime.now().strftime("%Y%m%d%H%M")
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    grand_total = sum(i[3] for i in items_list)

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
    pdf.cell(90, 10, "Description", border=1, align='C')
    pdf.cell(30, 10, "Price", border=1, align='C')
    pdf.cell(20, 10, "Qty", border=1, align='C')
    pdf.cell(50, 10, "Total", border=1, ln=1, align='C')

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=11)
    
    for row in items_list:
        pdf.cell(90, 10, f" {row[0]}", border=1)
        pdf.cell(30, 10, f"{row[1]}", border=1, align='C')
        pdf.cell(20, 10, f"{row[2]}", border=1, align='C')
        pdf.cell(50, 10, f"{row[3]}", border=1, ln=1, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", 'B', size=14)
    pdf.set_text_color(0, 51, 153)
    pdf.cell(0, 10, f"Grand Total: Rs. {grand_total} ", ln=1, align='R')

    pdf.output(f"Invoice_{invoice_no}.pdf")
    
    messagebox.showinfo("Success", f"Final Bill Ban Gaya: Invoice_{invoice_no}.pdf")
    
    items_list.clear()
    entry_client.delete(0, tk.END)

root = tk.Tk()
root.title("Office Multi-Bill System")
root.geometry("400x500")

tk.Label(root, text="OFFICE DATA ENTRY", font=("Arial", 14, "bold"), fg="blue").pack(pady=15)

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

tk.Button(root, text="1. ADD ITEM TO BILL", command=add_item, bg="orange", fg="black", font=("Arial", 10, "bold"), width=25).pack(pady=10)

tk.Button(root, text="2. GENERATE FINAL PDF", command=finalize_pdf, bg="darkblue", fg="white", font=("Arial", 10, "bold"), width=25).pack(pady=10)

root.mainloop()

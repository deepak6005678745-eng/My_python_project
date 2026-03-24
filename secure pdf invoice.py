import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from fpdf import FPDF
from datetime import datetime
import sys

items_list = []

def check_password():
   
    sahi_pass = "0909"
    user_input = simpledialog.askstring("Security Check", "Enter Security PIN:", show='*')
    
    if user_input == sahi_pass:
        return True
    else:
        messagebox.showerror("Error", "Wrong Password! System Closing.")
        return False

def add_item():
    try:
        item = entry_item.get()
        price_val = entry_price.get()
        qty_val = entry_qty.get()

        if not item or not price_val or not qty_val:
            messagebox.showwarning("Warning", "Saare boxes bharo bhai!")
            return

        price = float(price_val)
        qty = int(qty_val)
        total = price * qty
        
        items_list.append([item, price, qty, total])
        tree.insert("", tk.END, values=(item, f"{price:.2f}", qty, f"{total:.2f}"))
        
        
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Price aur Qty mein sirf number daalo!")

def finalize_pdf():
    if not items_list:
        messagebox.showwarning("Warning", "Pehle items jodo!")
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
    
    # 1. GREEN BORDER ADDED
    pdf.set_draw_color(0, 128, 0)
    pdf.rect(5, 5, 200, 287)
    
    # 2. HEADER
    pdf.set_text_color(0, 51, 153) 
    pdf.set_font("Arial", 'B', size=24)
    pdf.cell(200, 20, txt="OFFICE INVOICE", ln=1, align='C')
    
    # 3. CLIENT INFO
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=10)
    pdf.ln(5)
    pdf.set_x(10)
    pdf.cell(100, 10, f"Invoice No: {invoice_no}")
    pdf.cell(90, 10, f"Date: {date_str}", ln=1, align='R')
    pdf.cell(0, 10, f"Client: {client}", ln=1)
    
    pdf.ln(10)
    
    
    pdf.set_text_color(0, 51, 153)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(85, 10, "Description", border=1, align='C')
    pdf.cell(35, 10, "Price", border=1, align='C')
    pdf.cell(25, 10, "Qty", border=1, align='C')
    pdf.cell(45, 10, "Total", border=1, ln=1, align='C')

   
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=11)
    for row in items_list:
        pdf.cell(85, 10, f" {row[0]}", border=1)
        pdf.cell(35, 10, f"{row[1]:.2f}", border=1, align='C')
        pdf.cell(25, 10, f"{row[2]}", border=1, align='C')
        pdf.cell(45, 10, f"{row[3]:.2f}", border=1, ln=1, align='C')

   
    pdf.ln(10)
    pdf.set_font("Arial", 'B', size=14)
    pdf.set_text_color(0, 128, 0) 
    pdf.cell(0, 10, f"Grand Total: Rs. {grand_total:.2f} ", ln=1, align='R')

    pdf.output(f"Invoice_{client}_{invoice_no}.pdf")
    messagebox.showinfo("Success", f"Bill Ban Gaya: Invoice_{client}.pdf")
    
    
    items_list.clear()
    for i in tree.get_children():
        tree.delete(i)
    entry_client.delete(0, tk.END)


root = tk.Tk()
root.withdraw() 

if check_password():
    root.deiconify() 
    root.title("My Professional Billing System")
    root.geometry("550x650")

    tk.Label(root, text="OFFICE DATA ENTRY SYSTEM", font=("Arial", 16, "bold"), fg="darkgreen").pack(pady=15)

    # Inputs
    tk.Label(root, text="Client Name:", font=("Arial", 10, "bold")).pack()
    entry_client = tk.Entry(root, width=45, bd=2)
    entry_client.pack(pady=5)

    frame_inputs = tk.Frame(root)
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="Item Name").grid(row=0, column=0)
    entry_item = tk.Entry(frame_inputs, width=20)
    entry_item.grid(row=1, column=0, padx=5)

    tk.Label(frame_inputs, text="Price").grid(row=0, column=1)
    entry_price = tk.Entry(frame_inputs, width=10)
    entry_price.grid(row=1, column=1, padx=5)

    tk.Label(frame_inputs, text="Qty").grid(row=0, column=2)
    entry_qty = tk.Entry(frame_inputs, width=10)
    entry_qty.grid(row=1, column=2, padx=5)

    tk.Button(root, text="+ ADD ITEM TO LIST", command=add_item, bg="green", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=10)

    # List Table
    columns = ("Item", "Price", "Qty", "Total")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=110, anchor='center')
    tree.pack(pady=10)

    # Final Button
    tk.Button(root, text="GENERATE GREEN PDF BILL", command=finalize_pdf, bg="darkblue", fg="white", font=("Arial", 12, "bold"), width=30, height=2).pack(pady=20)

    root.mainloop()
else:
    root.destroy()

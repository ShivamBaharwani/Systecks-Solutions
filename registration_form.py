import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re

def validate_data():
    # input
    name = name_entry.get().strip()
    aicte_id = aicte_id_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    college = college_entry.get().strip()

    # checking empty fields
    if not name or not aicte_id or not email or not phone or not college:
        messagebox.showerror("Error", "Please fill in all fields")
        return False

    # AICTE ID format
    if not aicte_id.isdigit():
        messagebox.showerror("Error", "AICTE ID must contain only digits")
        return False

    # email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # got these formats from trusted website
        messagebox.showerror("Error", "Invalid email format")
        return False

    # number format
    if not re.match(r"^\d{10}$", phone):
        messagebox.showerror("Error", "Invalid phone number format")
        return False

    return True

def create_pdf():
    if validate_data():
        name = name_entry.get().strip()
        aicte_id = aicte_id_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        college = college_entry.get().strip()

        # PDF
        pdf_file = f"{name}_registration.pdf"
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.drawString(100, 750, f"Name: {name}")
        c.drawString(100, 730, f"AICTE ID: {aicte_id}")
        c.drawString(100, 710, f"Email: {email}")
        c.drawString(100, 690, f"Phone: {phone}")
        c.drawString(100, 670, f"College: {college}")
        c.save()

        messagebox.showinfo("Success", f"PDF created successfully: {pdf_file}")

root = tk.Tk()
root.title("Student Registration Form")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

aicte_id_label = tk.Label(root, text="AICTE ID:")
aicte_id_label.grid(row=1, column=0)
aicte_id_entry = tk.Entry(root)
aicte_id_entry.grid(row=1, column=1)

email_label = tk.Label(root, text="E-mail:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=3, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1)

college_label = tk.Label(root, text="College:")
college_label.grid(row=4, column=0)
college_entry = tk.Entry(root)
college_entry.grid(row=4, column=1)

submit_button = tk.Button(root, text="Create PDF", command=create_pdf)
submit_button.grid(row=5, columnspan=2)

root.mainloop()

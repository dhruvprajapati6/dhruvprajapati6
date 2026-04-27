import random
import string
import tkinter as tk
from tkinter import messagebox


# Password generate function
def generate_password():
    length = entry_length.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    length = int(length)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    result_var.set(password)


# Copy to clipboard
def copy_password():
    window.clipboard_clear()
    window.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")

# Label
tk.Label(window, text="🔐 Password Generator", font=("Arial", 16)).pack(pady=10)

# Input
tk.Label(window, text="Enter Length:").pack()
entry_length = tk.Entry(window)
entry_length.pack(pady=5)

# Button generate
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

# Result
result_var = tk.StringVar()
tk.Entry(window, textvariable=result_var, width=30).pack(pady=5)

# Copy button
tk.Button(window, text="Copy Password", command=copy_password).pack(pady=10)

# Run app
window.mainloop()
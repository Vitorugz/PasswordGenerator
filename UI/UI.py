import tkinter as tk
from tkinter import ttk
from functions.generate_pass import generate_pass

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x350")
window.configure(bg="#f0f2f5")

# Window style
style = ttk.Style(window)
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11))
style.configure("TCheckbutton", font=("Arial", 10))
style.configure("Title.TLabel", font=("Arial", 16, "bold"))

# Define the variables
var_title = tk.StringVar(value="Password Generator")
var_pass = tk.StringVar()
var_generated_pass = tk.StringVar()

var_check_upper = tk.BooleanVar()
var_check_lower = tk.BooleanVar()
var_check_numbers = tk.BooleanVar()
var_check_symbols = tk.BooleanVar()

# Function to handle entry focus
def on_entry_focus_in(event):
    '''Function to handle entry focus'''
    if entry_length.get() == placeholder_text:
        entry_length.delete(0, tk.END)
        entry_length.config(foreground='black')

def on_entry_focus_out(event):
    '''Function to handle entry focus out'''
    if not entry_length.get():
        entry_length.insert(0, placeholder_text)
        entry_length.config(foreground='gray')

# Function to handle generate button
def handle_generate():
    '''Function to handle generate button'''
    try:
        length = int(entry_length.get())
    except ValueError:
        var_pass.set("Invalid length")
        return

    password = generate_pass(
        length,
        var_check_upper.get(),
        var_check_lower.get(),
        var_check_numbers.get(),
        var_check_symbols.get()
    )
    if password:
        var_pass.set("Generated Password:")
        var_generated_pass.set(password)
        label_pass.pack()
        label_generated_pass.pack()
        frame_copy.pack(pady=5)

# Title
ttk.Label(window, textvariable=var_title, style="Title.TLabel", background="#f0f2f5").pack(pady=10)

# Entry for password length
placeholder_text = "Enter password length"

entry_length = ttk.Entry(window, font=("Arial", 11), width=30, foreground='gray')
entry_length.insert(0, placeholder_text)
entry_length.bind("<FocusIn>", on_entry_focus_in)
entry_length.bind("<FocusOut>", on_entry_focus_out)
entry_length.pack(pady=5)

# Checkboxes
frame_checks = tk.Frame(window, bg="#f0f2f5")
frame_checks.pack(pady=10)

ttk.Checkbutton(frame_checks, text="Uppercase", variable=var_check_upper).grid(row=0, column=0, sticky="w", padx=10, pady=2)
ttk.Checkbutton(frame_checks, text="Lowercase", variable=var_check_lower).grid(row=0, column=1, sticky="w", padx=10, pady=2)
ttk.Checkbutton(frame_checks, text="Numbers", variable=var_check_numbers).grid(row=1, column=0, sticky="w", padx=10, pady=2)
ttk.Checkbutton(frame_checks, text="Symbols", variable=var_check_symbols).grid(row=1, column=1, sticky="w", padx=10, pady=2)

# Label for generated password ( headless initially )
label_pass = ttk.Label(window, textvariable=var_pass, font=("Arial", 12, "bold"))
label_generated_pass = ttk.Label(window, textvariable=var_generated_pass, font=("Arial", 10))

# Buttons
frame_button = tk.Frame(window, bg="#f0f2f5")
frame_button.pack(pady=10)

ttk.Button(frame_button, text="Generate", command=handle_generate).pack(side="left", padx=5)
ttk.Button(frame_button, text="Close", command=window.destroy).pack(side="left", padx=5)

# Copy button ( headless initially )
frame_copy = tk.Frame(window, bg="#f0f2f5")
ttk.Button(frame_copy, text="Copy", command=lambda: window.clipboard_clear() or window.clipboard_append(var_generated_pass.get())).pack()

window.mainloop()

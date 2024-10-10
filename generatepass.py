import tkinter as tk
import random
import string

def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters  # Upper and lower case letters
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    # Get the password length from the entry
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be at least 1.")
        password = generate_password(length)
        password_label.config(text=password)
    except ValueError:
        password_label.config(text="Please enter a valid length.")

# Create the main window
parent = tk.Tk()
parent.title("Random Password Generator")
parent.geometry("300x200")

# Create and place the widgets
length_label = tk.Label(parent, text="Enter password length:")
length_label.pack(pady=10)

length_entry = tk.Entry(parent)
length_entry.pack(pady=5)

generate_button = tk.Button(parent, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

password_label = tk.Label(parent, text="", font=("Helvetica", 12))
password_label.pack(pady=10)

# Run the application
parent.mainloop()

import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("When you press a button the message will pop up")
root.geometry('500x300')

# Function to handle button click
def onClick():
    messagebox.showinfo("Welcome to TYBBACA Student", "Hi I'm Ramesh")

# Create a button
button = tk.Button(root, text="Click Me", command=onClick, height=5, width=10)
button.pack(side='bottom')

# Start the main loop
root.mainloop()

import tkinter as tk

# Create the main application window
parent = tk.Tk()
parent.title("Welcome to College Student")

# Create a label and place it in the grid
my_label = tk.Label(parent, text="Hello", font=("Arial Bold", 70))
my_label.grid(column=0, row=0)

# Start the main loop
parent.mainloop()

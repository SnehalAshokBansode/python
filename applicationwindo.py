from tkinter import *

# Create the main application window
app = Tk()
app.title("Hi! Welcome to TYBBACA Students")
app.geometry("800x500")

# Create the menu bar
menubar = Menu(app, background='blue', fg='white')

# Create the File menu
file = Menu(menubar, tearoff=False, background='yellow')
file.add_command(label="New")
file.add_command(label="Exit", command=app.quit)

# Create the Edit menu
edit = Menu(menubar, tearoff=False, background='pink')
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

# Add the menus to the menu bar
menubar.add_cascade(label="File", menu=file)
menu

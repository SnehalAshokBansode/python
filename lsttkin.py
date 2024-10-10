import tkinter as tk

# Create the main window
parent = tk.Tk()
parent.geometry("250x200")

# Create a label
label1 = tk.Label(parent, text="A list of Computer Science Courses")
label1.pack()

# Create a listbox
listbox = tk.Listbox(parent)
listbox.insert(1, "PHP")
listbox.insert(2, "Python")
listbox.insert(3, "Java")
listbox.insert(4, "C#")
listbox.pack()

# Run the application
parent.mainloop()

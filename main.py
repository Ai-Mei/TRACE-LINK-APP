import tkinter as tk
from tkinter import ttk


# Create a window.
root = tk.Tk()
root.title("TrackrBee")
root.geometry("500x500")

# Change the icon of the window.
icon_path = r"C:\Users\Administrator\Documents\2ND SEMESTER\OOP\FINAL PROJECT\TraceBee\icon.gif"
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon)


# Make the window a scrollable window.
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)


root.mainloop()
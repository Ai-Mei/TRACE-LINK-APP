import tkinter as tk
from tkinter import ttk
from USERINTERFACE import UserInterface
ui = UserInterface()

# Create a window.
top = tk.Tk()
top.title("TrackrBee")
top.geometry("500x500")

# Change the icon of the window.
icon_path = r"C:\Users\Administrator\Documents\2ND SEMESTER\OOP\FINAL PROJECT\TraceBee\icon.gif"
icon = tk.PhotoImage(file=icon_path)
top.iconphoto(True, icon)


# Make the window a scrollable window.
canvas = tk.Canvas(top)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Call the functions from UserInterface 
ui.top = top
ui.buttons(frame)


top.mainloop()
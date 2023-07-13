import tkinter as tk
from tkinter import ttk
from USERINTERFACE import UserInterface

top = tk.Tk()
top.title("TrackrBee")
top.geometry("500x500")

icon_path = r"C:\Users\Administrator\Documents\2ND SEMESTER\OOP\Dump\FINAL PROJECT\icon.gif"
icon = tk.PhotoImage(file=icon_path)
top.iconphoto(True, icon)

canvas = tk.Canvas(top)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_bar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=canvas.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)


ui = UserInterface(top)
ui.buttons(frame)



top.mainloop()



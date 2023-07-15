import tkinter as tk
from tkinter import ttk
from USERINTERFACE import UserInterface

top = tk.Tk()
top.title("TrackrBee")
top.geometry("500x500")

ui = UserInterface(top)
ui.background(r"C:\Users\Administrator\Documents\2ND SEMESTER\OOP\FINAL PROJECT\TraceBee\bg.png")
ui.icon(r"C:\Users\Administrator\Documents\2ND SEMESTER\OOP\FINAL PROJECT\TraceBee\icon.gif")

ui.buttons(top)


top.mainloop()



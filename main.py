import tkinter as tk
from USERINTERFACE import UserInterface

top = tk.Tk()
top.title("TrackrBee")
top.geometry("500x500")

# Initiliaze the UserInterface
ui = UserInterface(top)
# Set the background of the main window
ui.background(r"C:\Users\Administrator\Documents\2ND SEMESTER\OOP\FINAL PROJECT\TraceBee\bg.png")
# Set the icon of the whole app
ui.icon(r"C:\Users\Administrator\Documents\2ND SEMESTER\OOP\FINAL PROJECT\TraceBee\icon.gif")
# Add buttons
ui.buttons(top)

top.mainloop()



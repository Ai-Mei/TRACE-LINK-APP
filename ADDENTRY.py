import tkinter as tk
from tkinter import ttk
from UINEWPAGE import UINewPage
ui = UINewPage()

class AddEntry:
    def __init__(self, top=None):
        self.top = top

    def add_entry(self):
        # Close the main window to display the new page
        self.top.withdraw()
        # Create the next page
        new_page = tk.Toplevel(self.top)
        new_page.geometry("500x500")
        new_page.title("Add New Entry")

        # Create a canvas with a scrollbar
        canvas = tk.Canvas(new_page)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(new_page, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Create a frame inside the canvas for the scrollable content
        content_frame = tk.Frame(canvas)
        content_frame.pack(fill="both", expand=True)

        # Configure the scrolling
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        ui = UINewPage()
        # Add the initial data needed for contact tracing.
        ui.create_form(content_frame)
        # Add a back button
        ui.back_button(content_frame, self.top)

        # Update the window
        content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))














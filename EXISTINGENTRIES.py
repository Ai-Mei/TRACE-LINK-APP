import tkinter as tk
from tkinter import ttk
from UINEWPAGE import UINewPage

class ExistingEntries:
    def __init__(self, top):
        self.top = top
        self.search_entry = None

    def existing_entries(self):
        # Close the main window to display the new page
        self.top.withdraw()

        # Create the next page
        new_page = tk.Toplevel(self.top)
        new_page.geometry("500x500")
        new_page.title("Existing Entries")

        # Create a canvas with a scrollbar
        canvas = tk.Canvas(new_page)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(new_page, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Create a frame inside the canvas for the scrollable content
        content_frame = tk.Frame(canvas)
        content_frame.configure(bg="#950101")
        content_frame.pack(fill="both", expand=True)

        # Configure the canvas scrolling
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Create an instance of UINewPage
        ui = UINewPage()

        # Add a search bar and button
        ui.create_search(content_frame)
        ui.display_file_contents(content_frame)

        # Add a back button
        ui.back_button(content_frame, self.top)

        # Update the canvas scrollable area
        content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

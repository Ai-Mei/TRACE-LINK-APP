import tkinter as tk
from UINEWPAGE import UINewPage
ui = UINewPage()

class AddEntry:
    def __init__(self, top):
        self.top = top

    def add_entry(self):
        # Close the main window to display the new page
        self.top.withdraw()
        # Create the next page
        new_page = tk.Toplevel(self.top)
        new_page.geometry("500x500")
        new_page.title("Add New Entry")


        ui = UINewPage()
        # Add the initial data needed for contact tracing.
        ui.create_form(new_page)
        # Add a back button
        ui.back_button(new_page, self.top)














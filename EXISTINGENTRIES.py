import tkinter as tk
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

        # Contents

 
        ui = UINewPage()
        # Add a search bar and button
        ui.create_search(new_page)
        # Add a back button
        ui.back_button(new_page, self.top)

    def searched_word(self):
        searched = self.search_entry.get()
        print("Searching for:", searched)

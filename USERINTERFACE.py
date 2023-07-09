import tkinter as tk

# Create a class for UserInterface
class UserInterface:
    # Make a function for opening a new page
    def open_new_page(self, page_title):
        # close the main window to display the new
        self.top.withdraw()

        # Create the next page 
        new_page = tk.Toplevel(self.top)
        new_page.geometry("500x500")
        new_page.title(page_title)

        # # Contents of the new page
        # label = tk.Label(new_page, text=f"This is {page_title}")
        # label.pack()

        # Add a back button
        back_button = tk.Button(new_page, text="Back", command=lambda: self.close_next_page(new_page))
        back_button.pack()

    # Create a function that will go back to the main page
    def close_next_page(self, page):
        # Close the next page window
        page.destroy()
        # Show the previous window (top)
        self.top.deiconify()

    # Make buttons for 2 options (free browsing in the existing data and add a new entry)
    def buttons(self, frame):
        button1 = tk.Button(frame, text="Add New Entry", command=lambda: self.open_new_page("Add New Entry"), width=70, height=15)
        button1.pack(fill=tk.X, expand=True)

        # Add a button to open the second next page
        button2 = tk.Button(frame, text="See Existing Entries", command=lambda: self.open_new_page("Existing Entries"), width=70, height=15)
        button2.pack(fill=tk.X, expand=True)

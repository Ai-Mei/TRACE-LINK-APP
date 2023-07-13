import tkinter as tk

class UINewPage:
    def back_button(self, new_page, top):
        back_button = tk.Button(new_page, text="Back to Homepage", command=lambda: self.close_next_page(new_page, top))
        back_button.pack()

    def close_next_page(self, page, top):
        # Close the next page window
        page.destroy()
        # Show the previous window (top)
        top.deiconify()

    def create_search(self, new_page):
        self.search_entry = tk.Entry(new_page)
        self.search_entry.pack()

        search_button = tk.Button(new_page, text="Search", command=self.searched_word)
        search_button.pack()

    # Get the search word
    def searched_word(self):
        searched = self.search_entry.get()


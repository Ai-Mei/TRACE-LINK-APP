import tkinter as tk
from ADDENTRY import AddEntry
from EXISTINGENTRIES import ExistingEntries

class UserInterface:
    def __init__(self, top):  
        self.top = top

    def buttons(self, frame):
        add_entry = AddEntry(self.top) 
        existing_entries = ExistingEntries(self.top)

        button1 = tk.Button(frame, text="Add New Entry", command=lambda: add_entry.add_entry(), width=70, height=15)
        button1.pack(fill=tk.X, expand=True)

        button2 = tk.Button(frame, text="See Existing Entries", command=lambda: existing_entries.existing_entries(), width=70, height=15)
        button2.pack(fill=tk.X, expand=True)

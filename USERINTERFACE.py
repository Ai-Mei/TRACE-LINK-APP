import tkinter as tk
from PIL import ImageTk, Image
from ADDENTRY import AddEntry
from EXISTINGENTRIES import ExistingEntries

class UserInterface:
    def __init__(self, top):  
        self.top = top

    def buttons(self, frame):
        add_entry = AddEntry(self.top) 
        existing_entries = ExistingEntries(self.top)

        add_entry = AddEntry(self.top) 
        existing_entries = ExistingEntries(self.top)

        font_format = ("Century Gothic", 16, "bold")

        button1 = tk.Button(frame, text="Add New Entry", command=lambda: add_entry.add_entry(), width=25, height=2, font=font_format)
        button1.place(relx=0.5, rely=0.65, anchor=tk.CENTER) 

        button2 = tk.Button(frame, text="See Existing Entries", command=lambda: existing_entries.existing_entries(), width=25, height=2, font=font_format)
        button2.place(relx=0.5, rely=0.85, anchor=tk.CENTER) 


    def background(self, image_path):
        # Load and resize the background image
        background_image = Image.open(image_path)
        background_image = background_image.resize((500, 500), Image.ANTIALIAS)

        # Create a PhotoImage object from the resized image
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label and set the image as its background
        background_label = tk.Label(self.top, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.lower()


    def icon(self, icon_path):
        self.icon = tk.PhotoImage(file=icon_path)
        self.top.iconphoto(True, self.icon)

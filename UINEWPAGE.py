import tkinter as tk
import tkinter.messagebox as messagebox

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
        self.search_entry = tk.Entry(new_page, width=50)
        self.search_entry.pack(pady=20)
        
        search_button = tk.Button(new_page, text="Search", command=self.searched_word, width=10, height=1)
        search_button.pack()

    # Get the search word
    def searched_word(self):
        searched = self.search_entry.get()

    def save_data(self, new_page):
        # Get the input values from the user
        full_name = self.entry_full_name.get()
        phone_number = self.entry_phone_number.get()
        # Validate phone number
        if len(phone_number) != 11 or not phone_number.isdigit():
            messagebox.showerror("Error", "Please enter a valid 11-digit phone number.")
            return
        address = self.entry_address.get()
        age = self.entry_age.get()
        # Validate age
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")
            return
        sex = self.selected_sex.get()
        email = self.entry_email.get()
        occupation = self.entry_occupation.get()

        # If any of the fields are left with no entry, send an error message
        if not full_name or not phone_number or not address or not age or not sex or not email or not occupation:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return
        
        # Create a tuple to store the user's information
        user_data = (full_name.title(), phone_number, address.title(), age, sex.capitalize(), email, occupation.title())

        # Save the data in a file named BEE_INFORMATION
        with open("BEE_INFORMATION.txt", "a") as file:
            file.write("User Information:\n")
            file.write(f"Full Name: {user_data[0]}\n")
            file.write(f"Phone Number: {user_data[1]}\n")
            file.write(f"Address: {user_data[2]}\n")
            file.write(f"Age: {user_data[3]}\n")
            file.write(f"Gender: {user_data[4]}\n")
            file.write(f"Email Address: {user_data[5]}\n")
            file.write(f"Occupation: {user_data[6]}\n")
            file.write("\n")

        messagebox.showinfo("Success", "Data saved successfully.")


        # GENERATE A PRINT CHECK TO ENSURE THAT THE DATA WERE PROPERLY RECORDED
        print(user_data)


    def create_form(self, new_page):
        # Create labels and entry fields for each information field
        label_full_name = tk.Label(new_page, text="Full Name:")
        label_full_name.pack(anchor='w', padx=50)
        self.entry_full_name = tk.Entry(new_page)
        self.entry_full_name.pack(anchor='w', padx=50)
        self.entry_full_name.config(width=50)

        label_phone_number = tk.Label(new_page, text="Phone Number:")
        label_phone_number.pack(anchor='w', padx=50)
        self.entry_phone_number = tk.Entry(new_page)
        self.entry_phone_number.pack(anchor='w', padx=50)
        self.entry_phone_number.config(width=50)

        label_address = tk.Label(new_page, text="Address:")
        label_address.pack(anchor='w', padx=50)
        self.entry_address = tk.Entry(new_page)
        self.entry_address.pack(anchor='w', padx=50)
        self.entry_address.config(width=50)

        label_age = tk.Label(new_page, text="Age:")
        label_age.pack(anchor='w', padx=50)
        self.entry_age = tk.Entry(new_page)
        self.entry_age.pack(anchor='w', padx=50)
        self.entry_age.config(width=50)

        # Create a checkbox for users to select sex
        label_sex = tk.Label(new_page, text="Sex:")
        label_sex.pack(padx=50, anchor='w')
        
        sex_choices = ["Female", "Male", "Intersex"]
        self.selected_sex = tk.StringVar()
        for sex in sex_choices:
            checkbox = tk.Checkbutton(new_page, text=sex, variable=self.selected_sex, onvalue=sex, offvalue="")
            checkbox.pack(anchor='w', padx=50)

        label_email = tk.Label(new_page, text="Email Address:")
        label_email.pack(anchor='w', padx=50)
        self.entry_email = tk.Entry(new_page)
        self.entry_email.pack(anchor='w', padx=50)
        self.entry_email.config(width=50)

        label_occupation = tk.Label(new_page, text="Occupation:")
        label_occupation.pack(anchor='w', padx=50)
        self.entry_occupation = tk.Entry(new_page)
        self.entry_occupation.pack(anchor='w', padx=50)
        self.entry_occupation.config(width=50)

        # Create the save button
        save_button = tk.Button(new_page, text="Save", command=lambda: self.save_data(new_page))
        save_button.pack(anchor='w', padx=50, pady=40)

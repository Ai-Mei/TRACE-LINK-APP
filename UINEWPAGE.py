import tkinter as tk
from tkinter import font
import datetime
import tkinter.messagebox as messagebox

class UINewPage:
    def back_button(self, new_page, top):
        back_button = tk.Button(new_page, text="Back to Homepage", command=lambda: self.close_next_page(new_page, top))
        back_button.pack()

    def close_next_page(self, new_page, top):
        # Close the next page window
        new_page.destroy()
        # Destroy any other Toplevel windows except the main page
        for window in top.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()
        # Show the main page (top)
        top.deiconify()

    def create_search(self, new_page):
        bold_font = font.Font(weight="bold")
        self.search_entry = tk.Entry(new_page, width=50)
        self.search_entry.pack(pady=20)

        search_button = tk.Button(new_page, text="Search", command=lambda: self.searched_word(new_page), width=10, height=1)
        search_button.pack()

        self.result_label = tk.Label(new_page, text="Results:", font=bold_font)
        self.result_label.pack(anchor='w', padx=50)

        self.text_widget = tk.Text(new_page, height=10, width=50)
        self.text_widget.pack()

    # Get the search word and display the matching entry
    def searched_word(self, new_page):
        searched = self.search_entry.get()
        with open("BEE_INFORMATION.txt", "r") as file:
            contents = file.read()
            index = contents.find(searched)
            if index != -1:
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, contents)
                self.text_widget.tag_add("bold", f"1.{index}", f"1.{index + len(searched)}")
                bold_font = font.Font(self.text_widget, self.text_widget.cget("font"))
                bold_font.configure(weight="bold")
                self.text_widget.tag_configure("bold", font=bold_font)

                self.result_label.config(text=f"Result: Word found - {searched}")
            else:
                self.text_widget.delete("1.0", tk.END)
                self.result_label.config(text="Result: Word not found.")

    # UPDATE THE SAVE DATA TO GET ALL OF THE INFORMATION IN THE HEALTH INFORMATION
    def save_data(self):
        # Get the date
        date = self.entry_date.get()
        try:
            # Parse the date string into a datetime object
            datetime_obj = datetime.datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please enter a date in MM/DD/YYYY format.")
            return
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
        vax = self.selected_vax.get()
        symptoms = ", ".join([symptom for symptom, var in self.selected_symptoms if var.get() == 1])
        exposure = self.selected_exposure.get()
        exposure1= self.selected_exposure1.get()
        test = self.selected_test.get()


        # If any of the fields are left with no entry, send an error message
        if not date or not full_name or not phone_number or not address or not age or not sex or not email or not occupation or not vax or not symptoms or not exposure or not exposure1 or not test:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        # Create a tuple to store the user's information
        user_data = (date, full_name.title(), phone_number, address.title(), age, sex.capitalize(), email, occupation.title(), vax, symptoms, exposure, exposure1, test)


        # Save the data in a file
        with open("BEE_INFORMATION.txt", "a+") as file:
            file.seek(0)
            lines = file.readlines()
            # Get the current number of entries
            entry_no = len(lines) // 21
            file.write(f"Entry No.: {entry_no + 1}\n")
            file.write(f"Date: {user_data[0]}\n")  
            file.write("\n")
            file.write("User Information:\n")
            file.write(f"Full Name: {user_data[1]}\n")
            file.write(f"Phone Number: {user_data[2]}\n")
            file.write(f"Address: {user_data[3]}\n")
            file.write(f"Age: {user_data[4]}\n")
            file.write(f"Sex: {user_data[5]}\n")
            file.write(f"Email Address: {user_data[6]}\n")
            file.write(f"Occupation: {user_data[7]}\n")
            file.write("\n")
            file.write("Health Information:\n")
            file.write(f"Vaccine: {user_data[8]}\n")
            file.write(f"Symptomps: {user_data[9]}\n")
            file.write(f"Exposure: {user_data[10]}\n")
            file.write(f"Exposure: {user_data[11]}\n")
            file.write(f"Test: {user_data[12]}\n")
            file.write("\n")
            file.write("==================================================")
            file.write("\n")

        messagebox.showinfo("Success", "Data saved successfully.")

    def display_file_contents(self, new_page):
        bold_font = font.Font(weight="bold")
        # Read the contents of the file
        with open("BEE_INFORMATION.txt", "r") as file:
            contents = file.read()
        self.result_label = tk.Label(new_page, text="All Entries:", font=bold_font)
        self.result_label.pack(anchor='w', padx=50)
        # Create a text widget to display the file contents
        text_widget = tk.Text(new_page, height=10, width=50)
        text_widget.pack(pady=10, padx=30)

        # Insert the file contents without formatting
        text_widget.insert("1.0", contents)

    def create_form(self, new_page):
        bold_font = font.Font(weight="bold")
        # Ask the date of entry
        date = tk.Label(new_page, text="Date (MM/DD/YYYY)", font=bold_font)
        date.pack(anchor='w', padx=50)
        self.entry_date = tk.Entry(new_page)
        self.entry_date.pack(anchor='w', padx=50)
        self.entry_date.config(width=30)

        # Create labels and entry fields for each information field
        head1 = tk.Label(new_page, text="PERSONAL INFORMATION", font=bold_font)
        head1.pack(pady=10)

        label_full_name = tk.Label(new_page, text="Full Name:", font=bold_font)
        label_full_name.pack(anchor='w', padx=50)
        self.entry_full_name = tk.Entry(new_page)
        self.entry_full_name.pack(anchor='w', padx=50)
        self.entry_full_name.config(width=60)

        label_phone_number = tk.Label(new_page, text="Phone Number:", font=bold_font)
        label_phone_number.pack(anchor='w', padx=50)
        self.entry_phone_number = tk.Entry(new_page)
        self.entry_phone_number.pack(anchor='w', padx=50)
        self.entry_phone_number.config(width=60)

        label_address = tk.Label(new_page, text="Address:", font=bold_font)
        label_address.pack(anchor='w', padx=50)
        self.entry_address = tk.Entry(new_page)
        self.entry_address.pack(anchor='w', padx=50)
        self.entry_address.config(width=60)

        label_age = tk.Label(new_page, text="Age:", font=bold_font)
        label_age.pack(anchor='w', padx=50)
        self.entry_age = tk.Entry(new_page)
        self.entry_age.pack(anchor='w', padx=50)
        self.entry_age.config(width=60)

        label_sex = tk.Label(new_page, text="Sex:", font=bold_font)
        label_sex.pack(padx=50, anchor='w')
        sex_choices = ["Female", "Male", "Intersex"]
        self.selected_sex = tk.StringVar()
        for sex in sex_choices:
            checkbox = tk.Checkbutton(new_page, text=sex, variable=self.selected_sex, onvalue=sex, offvalue="")
            checkbox.pack(anchor='w', padx=50)

        label_email = tk.Label(new_page, text="Email Address:", font=bold_font)
        label_email.pack(anchor='w', padx=50)
        self.entry_email = tk.Entry(new_page)
        self.entry_email.pack(anchor='w', padx=50)
        self.entry_email.config(width=60)

        label_occupation = tk.Label(new_page, text="Occupation:", font=bold_font)
        label_occupation.pack(anchor='w', padx=50)
        self.entry_occupation = tk.Entry(new_page)
        self.entry_occupation.pack(anchor='w', padx=50)
        self.entry_occupation.config(width=60)


        head2 = tk.Label(new_page, text="HEALTH INFORMATION", font=bold_font)
        head2.pack(pady=10)

        label_vax = tk.Label(new_page, text="Have you been vaccinated for COVID-19?", font=bold_font)
        label_vax.pack(padx=50, anchor='w')
        vax_choices = ["Not Yet", "1st Dose", "2nd Dose (Fully Vaccinated)", "1st Booster Shot", "2nd Booster Shot"]
        self.selected_vax = tk.StringVar()
        for vax in vax_choices:
            checkbox = tk.Checkbutton(new_page, text=vax, variable=self.selected_vax, onvalue=vax, offvalue="")
            checkbox.pack(anchor='w', padx=50)

        label_symptoms = tk.Label(new_page, text="Symptoms (select all that apply):", font=bold_font)
        label_symptoms.pack(padx=50, anchor='w')
        symptom_choices = [
            "Fever",
            "Cough",
            "Colds",
            "Muscle/body pains",
            "Sore throat",
            "Diarrhea",
            "Headache",
            "Shortness of breath",
            "Difficulty of breathing",
            "Loss of taste",
            "Loss of smell",
            "None of the above"
        ]
        self.selected_symptoms = []
        for symptom_choice in symptom_choices:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(new_page, text=symptom_choice, variable=var)
            checkbox.pack(anchor='w', padx=50)
            self.selected_symptoms.append((symptom_choice, var))

        label_exposure = tk.Label(new_page, text="In the last 14 days, were you exposed to a possible\nor confirmed case?", font=bold_font)
        label_exposure.pack(anchor='w', padx=50)
        exposure_choices = ["Yes", "No", "Not Sure"]
        self.selected_exposure = tk.StringVar()
        for exposure in exposure_choices:
            checkbox = tk.Checkbutton(new_page, text=exposure, variable=self.selected_exposure, onvalue=exposure, offvalue="")
            checkbox.pack(anchor='w', padx=50)

        label_exposure1 = tk.Label(new_page, text="In the previous week, did you come into touch with\n anyone who was experiencing body aches, colds,\nheadaches, sore throats, fevers, diarrhea, coughs,\nshortness of breath, loss of taste, or loss of smell? ", font=bold_font)
        label_exposure1.pack(anchor='w', padx=50)
        exposure1_choices = ["Yes", "No"]
        self.selected_exposure1 = tk.StringVar()
        for exposure1 in exposure1_choices:
            checkbox = tk.Checkbutton(new_page, text=exposure1, variable=self.selected_exposure1, onvalue=exposure1, offvalue="")
            checkbox.pack(anchor='w', padx=50)

        label_test = tk.Label(new_page, text="Have you had a Covid-19 test within the previous\n14 days? ", font=bold_font)
        label_test.pack(anchor='w', padx=50)
        test_choices = ["No", "Yes-Positive", "Yes-Negative", "Yes-Pending"]
        self.selected_test = tk.StringVar()
        for test in test_choices:
            checkbox = tk.Checkbutton(new_page, text=test, variable=self.selected_test, onvalue=test, offvalue="")
            checkbox.pack(anchor='w', padx=50)

        # Create the save button
        save_button = tk.Button(new_page, text="Save", command=lambda: self.save_data())
        save_button.pack(anchor='w', padx=50, pady=40)
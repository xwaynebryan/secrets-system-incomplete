from tkinter import messagebox
from tkinter import *
from secrets_login import login
from tkinter import ttk


def signup():
    signup_window = Toplevel()
    signup_window.geometry('800x700')
    signup_window.title('Account signup')
    signup_window.config(background='lightgrey')

    # Submit button functionalities
    def submit():
        # prompt_count = 0
        # prompt_limit = 1

        entries = {
            first_name_entry.get(),
            second_name_entry.get(),
            phone_number_entry.get(),
            id_number_entry.get(),
            email_address_entry.get(),
            password_entry.get(),
            password_retry_entry.get(),
            gender_combo.get(),
        }
        for space_entry in entries:
            if space_entry == "":
                empty_field = messagebox.showinfo("EMPTY FIELD(S)", "Kindly fill in all fields!")
                if empty_field == "ok":
                    signup_window.destroy()
                    signup()
        else:
            signup_congrats = messagebox.showinfo("", f"Congratulations, {first_name_entry.get()}!  "
                                                      f"Your account has been successfully created")
            signup_window.destroy()
            if signup_congrats == "ok":
                signup_window.destroy()
                login()

    form_type = Label(signup_window, text='Registration Form', font=('ravie', 30, 'bold'), fg='black', bg='lightgrey')
    form_type.pack(anchor='center', pady=20)

    # Field names
    first_name = Label(signup_window, text="First Name:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
    second_name = Label(signup_window, text="Second Name:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
    phone_number = Label(signup_window, text="Phone Number:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
    id_number = Label(signup_window, text="ID Number:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
    email_address = Label(signup_window, text="Email:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
    gender = Label(signup_window, text="Gender:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
    submit_button = Button(signup_window, text='Submit', font=('courie', 15, 'bold'), activebackground='grey',
                           command=submit)
    gender_list = ['Male', 'Female', 'Other']
    password = Label(signup_window, text="Password:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
    password_retry = Label(signup_window, text="Retry-Password:", font=('Times New Roman', 20, 'bold'), bg='lightgrey')

    # field packing on window
    first_name.place(relx=.01, rely=.15)
    second_name.place(relx=.01, rely=.25)
    phone_number.place(relx=.01, rely=.35)
    id_number.place(relx=.01, rely=.45)
    email_address.place(relx=.01, rely=.55)
    gender.place(relx=.01, rely=.65)
    password.place(relx=.01, rely=.75)
    password_retry.place(relx=.01, rely=.85)
    submit_button.place(relx=.50, rely=.92)

    # Creating entries
    first_name_entry = Entry(signup_window, width=40, font=('courie', 14), borderwidth=5, relief='sunken')
    second_name_entry = Entry(signup_window, width=40, font=('courie', 14), borderwidth=5, relief='sunken')
    phone_number_entry = Entry(signup_window, width=40, font=('courie', 14), borderwidth=5, relief='sunken')
    id_number_entry = Entry(signup_window, width=40, font=('courie', 14), borderwidth=5, relief='sunken')
    email_address_entry = Entry(signup_window, width=40, font=('courie', 14), borderwidth=5, relief='sunken')
    gender_combo = ttk.Combobox(signup_window, width=20, font=('courie', 14), values=gender_list)
    password_entry = Entry(signup_window, width=40, font=('courie', 14), borderwidth=5, relief='sunken', show='•')
    password_retry_entry = Entry(signup_window, width=40, font=('courie', 14), borderwidth=5, relief='sunken', show='•')

    # Place entries on window
    first_name_entry.place(relx=.30, rely=.15)
    second_name_entry.place(relx=.30, rely=.25)
    phone_number_entry.place(relx=.30, rely=.35)
    id_number_entry.place(relx=.30, rely=.45)
    email_address_entry.place(relx=.30, rely=.55)
    gender_combo.place(relx=.30, rely=.65)
    password_entry.place(relx=.30, rely=.75)
    password_retry_entry.place(relx=.30, rely=.85)
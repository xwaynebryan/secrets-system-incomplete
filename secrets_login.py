from tkinter import messagebox
from tkinter import *
import time
from tkinter import ttk
from maindash import main_dash_window


def login():
    def signin():
        if username_entry.get() == "" or password_entry.get() == "":
            login_win.destroy()
            empty_field = messagebox.showinfo('EMPTY FIELD(S)', 'Kindly Provide your Username and Password!')
            if empty_field == 'ok':
                login()
        elif username_entry.get() == "Bryan" and password_entry.get() == "Bryan":

            # Logging in Progressive bar
            signing_progress()
            login_win.destroy()
            user_reply = messagebox.showinfo('Successful', 'Login Successful 😊')
            if user_reply == 'ok':
                main_dash_window()

        else:
            login_win.destroy()
            incorrect_credentials = messagebox.showerror('Incorrect credentials', 'Invalid Username or Password!')
            if incorrect_credentials == 'ok':
                login()

    login_win = Toplevel()
    login_win.geometry('500x300')
    login_win.title('Log in')

    def signing_progress():
        loading_label = Label(login_win, text='Almost done...', font=('courie', 12, 'normal'), fg='grey')
        loading_label.place(relx=.40, rely=.75)

        login_progress = ttk.Progressbar(login_win, length=200, mode='determinate', orient=HORIZONTAL)
        login_progress.place(relx=.35, rely=.85)

        for step in range(5):
            login_progress['value'] += 20
            login_win.update_idletasks()
            time.sleep(1)

    # Username and password labels
    username_label = Label(login_win, text='👤 Username:', font=('Times New Roman', 15, 'normal'))
    username_label.place(relx=.01, rely=.08)

    password_label = Label(login_win, text='⨀ Password:', font=('Times New Roman', 15, 'normal'))
    password_label.place(relx=.01, rely=.30)

    # Username and password entry space
    username_entry = Entry(login_win, width=25, font=('courie', 14, 'normal'), borderwidth=5, relief='sunken')
    username_entry.place(relx=.30, rely=.08)

    password_entry = Entry(login_win, width=25, font=('courie', 14, 'normal'), show='*', borderwidth=5, relief='sunken')
    password_entry.place(relx=.30, rely=.30)

    signin_button = Button(login_win, text='SignIn', font=('courie', 15, 'bold'), activebackground='lightgrey', width=6,
                           command=signin)
    signin_button.place(relx=.50, rely=.50)

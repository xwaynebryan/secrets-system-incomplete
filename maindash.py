from tkinter import *

import os


def main_dash_window():
    main_dash_win = Tk()
    main_dash_win.geometry('800x700')
    main_dash_win.title('Dashboard')
    main_dash_win.config(background='lightgray')

    new_secret_button = Button(main_dash_win, text="New Secret", font=('courie', 17, 'bold'), width=20, height=7, activebackground="grey", command=lambda: first_secret())
    new_secret_button.place(relx=.1, rely=.1)

    my_secrets_button = Button(main_dash_win, text="My Secrets", font=('courie', 17, 'bold'), width=20, height=7, activebackground="grey")
    my_secrets_button.place(relx=.5, rely=.1)

    settings_button = Button(main_dash_win, text="Settings", font=('courie', 17, 'bold'), width=20, height=7, activebackground="grey")
    settings_button.place(relx=.1, rely=.5)

    recycle_button = Button(main_dash_win, text="Recycle Bin", font=('courie', 17, 'bold'), width=20, height=7, activebackground="grey")
    recycle_button.place(relx=.5, rely=.5)

    main_dash_win.mainloop()




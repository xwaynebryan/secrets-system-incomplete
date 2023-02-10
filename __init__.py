from tkinter import *
from secrets_signup import signup
from secrets_login import login


is_male = 'Male'
is_female = 'Female'
is_other = 'Other'


def main():

    def main_window():
        main_win = Tk()
        main_win.geometry('1000x700')
        main_win.title('Swish Sacco system')
        main_win.config(background='lightgray')

        main_label = Label(main_win, text='WELCOME TO TOP SECRETS 😊', font=('ravie', 30, 'bold'), bg='lightgray',
                           fg='black')
        main_label.pack(anchor='center', pady=40)

        emoji4 = Label(main_win, text='📜', font=('ravie', 100, 'bold'), bg='lightgray',
                       fg='black')
        emoji4.place(relx=.10, rely=.60)

        log_in_button = Button(main_win, text='Login', font=('courie', 15, 'bold'), width=10, activebackground='grey',
                               command=login)
        log_in_button.place(relx=.43, rely=.30)

        sign_up_label = Label(main_win, text='Have no account? Sign Up below.', font=('courie', 15, 'normal'),
                              bg='lightgray', fg='grey')
        sign_up_label.place(relx=.35, rely=.37)

        sign_up_button = Button(main_win, text='SignUp', font=('courie', 15, 'bold'), width=6, activebackground='grey',
                                command=signup)
        sign_up_button.place(relx=.45, rely=.55)

        main_label.pack(anchor='center', pady=40)

        main_win.mainloop()

    main_window()


main()

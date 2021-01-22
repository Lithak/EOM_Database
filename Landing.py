import tkinter
import mysql.connector
from tkinter import *
from tkinter import messagebox


# function to open this module
def popup():
    pass


# GUI properties/styles
kane = Tk()
kane.geometry("700x400")
kane.title('Log - In Page')
kane.configure(background='white')

head = Label(kane, text='Life Choices Online', font='times 15 bold ',
             fg='#19C300',
             bg='white')
head.pack(padx=50, pady=10)

reg_frame = Frame(kane)
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- ADMINISTRATION LOGIN -',
                font='times 30 bold underline',
                fg='#0B5800',
                bg='white')
heading.pack(pady=10)


def login():
    messagebox.showinfo("Login", "Input Details")
    kane.destroy()
    import LoginPage
    LoginPage.popup()


def register():
    kane.destroy()
    import Register


myButton = Button(kane, text="LOGIN", width=15, background='#1ca509', fg='black', command=login)
myButton.pack(pady=11)
myButton = Button(kane, text="REGISTER", width=15, background='#1ca509', fg='black', command=register)
myButton.pack(pady=5)

kane.mainloop()

# LITHA KANE'S DATABASE WORK
# USERNAME: Litha
# PASSWORD: 2021

# THIS IS MY FIRST INTERFACE

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
kane.configure(background='#ABC895')

# My heading
head = Label(kane, text='Life Choices Online', font='times 15 bold ',
             fg='#19C300',
             bg='#ABC895')
head.pack(padx=50, pady=10)

# Frame for my heading
reg_frame = Frame(kane, bg='#ABC895')
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- ADMINISTRATION LOGIN -',
                font='times 30 bold underline',
                fg='#0B5800',
                bg='#ABC895')
heading.pack(pady=10)


# Function to import the Log in GUI
def login():
    messagebox.showinfo("Login", "Input Details")
    kane.destroy()
    import LoginPage


# Function to import the Registration GUI
def register():
    kane.destroy()
    import Register


# My buttons to call the above functions
myButton = Button(kane, text="LOGIN", width=15, background='#1ca509', fg='black', command=login)
myButton.pack(pady=11)
myButton = Button(kane, text="REGISTER", width=15, background='#1ca509', fg='black', command=register)
myButton.pack(pady=5)

# Keep showing my GUI
kane.mainloop()

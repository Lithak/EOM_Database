# LITHA KANE'S LOG IN GUI
# THIS IS MY 3ND INTERFACE - Registration


import tkinter
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *


# function to open this module
def popup():
    pass


# GUI properties/styles
register = Tk()
register.geometry("600x670")
register.title('Registration page')
register.configure(background='#D4F1BE')

# DATABASE CONNECTOR STATEMENT
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='Lifechoicesonline',
                               host='127.0.0.1',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


# Getting Data from entries to the database
# Registration function
def post():
    a = Name.get()
    b = Surname.get()
    c = Email.get()
    d = Pass.get()

    sql = "INSERT INTO Admin_Staff (LastName, FirstName, EmailAddress, Password) VALUES (%s, %s, %s, %s)"
    val = (a, b, c, d)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    messagebox.showinfo('Data inserted', 'Successfully Recorded \n Continue to login page!')
    register.destroy()
    import LoginPage


# My labels for GUI
head = Label(register, text='Life Choices Online', font='times 12 bold ',
             fg='#19C300',
             bg='#D4F1BE')
head.pack(pady=10)

# Time & Date
clock = Label(register, font="bold")
clock.pack(pady=3)

time = datetime.now()
clock.config(text=time.strftime("%d/%m/%y  %H:%M:%S %p"), font='times 12', bg='#D4F1BE', fg='black')

# Frame & Labels & Entries
reg_frame = Frame(register, bg='#D4F1BE')
reg_frame.pack(pady=10)
heading = Label(reg_frame, text='- REGISTERATION FORM -',
                font='times 22 bold underline',
                fg='#0B5800',
                bg='#D4F1BE')
heading.pack()

# Warning - Admin only
note = Label(register, text='!ADMINSTRATOR REGISTRATION ONLY!', font='arial 8',
             fg='red',
             bg='#D4F1BE')
note.pack(pady=15)

# Entries & their Labels
entry_log = Label(register, text="Enter Your Name:",
                  font='arial 15 bold italic',
                  fg='#1ca509',
                  bg='#D4F1BE')
entry_log.pack(pady=10)
Name = Entry(width=25)
Name.pack(pady=15)

Surname = Label(register, text="Enter Surname:",
                font='arial 15 bold italic',
                fg='#1ca509',
                bg='#D4F1BE')
Surname.pack(pady=10)
Surname = Entry(width=25)
Surname.pack(pady=15)

entry_log = Label(register, text="Enter Email Address:",
                  font='arial 15 bold italic',
                  fg='#1ca509',
                  bg='#D4F1BE')
entry_log.pack(pady=10)
Email = Entry(width=25)
Email.pack(pady=15)

# Create new password
gen_lab = Label(register, text="Password", font=("arial", 12, 'bold'), bg='#D4F1BE', fg='#1ca509')
gen_lab.pack()
Pass = Entry(register, show='#')
Pass.pack(pady=12)

# Registration button
myButton = Button(register, text="Register", width=15, bg='#1ca509', fg='black', command=post)
myButton.pack(pady=11)


# Back function to 1st GUI
def back():
    register.destroy()
    import LoginPage


# My back Button
myButton = Button(register, text="Back to landing page", width=15, bg='#1ca509', fg='black', command=back)
myButton.pack(pady=11)

# Keep My GUI alive
register.mainloop()

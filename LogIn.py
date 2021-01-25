# LITHA KANE'S DATABASE WORK
# THIS IS MY 5th INTERFACE

from tkinter import *
from tkinter import messagebox
import mysql.connector


# function to open this module
def popup():
    pass


# GUI properties/styles
logstu = Tk()
logstu.title("IN & OUT")
logstu.geometry("700x680")
logstu.config(background='#ABC895')

# DATABASE CONNECTOR STATEMENT
mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1',
                               database='Lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

# My Labels & Headings
head = Label(logstu, text='Life Choices Online', font='times 12 bold ',
             fg='#19C300',
             bg='#ABC895')
head.pack()

# Frame & Labels
reg_frame = Frame(logstu, bg='#ABC895')
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- SIGN IN AND OUT -',
                font='times 22 bold underline',
                fg='#0B5800',
                bg='#ABC895')
heading.pack(pady=10)


# My Sign In at current time Function for students
def log():
    time = name_entry.get()
    sql = "UPDATE Users set LOGIN = curtime() where firstname = %s"
    mycursor.execute(sql, (time,))

    mydb.commit()

    user = name_entry.get()
    sql = 'SELECT * FROM Users WHERE firstname = %s'
    mycursor.execute(sql, (user,))
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("successfully", 'Logged In')
    else:
        messagebox.showinfo('error', 'try again')


# My Sign Out at current time Function for students
def out():
    timeout = name_entry.get()
    sql = "UPDATE Users set LOGOUT=curtime() where firstname = %s"
    mycursor.execute(sql, (timeout,))
    messagebox.showinfo("successfully", 'Logged Out')
    mydb.commit()

    user = name_entry.get()
    sql = 'SELECT * FROM Users WHERE firstname = %s'
    mycursor.execute(sql, (user,))
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("successfully", 'Logged Out')
    else:
        messagebox.showinfo('UNKOWN STUDENT', 'Student not on Database')


# Function to Go to Visitor GUI
def visitor():
    messagebox.showinfo("Visitor", 'Go to Sing In Visitors?')
    logstu.destroy()
    import visitor


# back to Admin function
def back():
    logstu.destroy()
    import admin


# Labels & their entries
name_label = Label(logstu, text="Name:", font='arial 15 bold',
                   fg='black',
                   bg='#ABC895')
name_label.pack(pady=10)
name_entry = Entry(logstu)
name_entry.pack(pady=10)

# My buttons to call the above functions
In_button = Button(logstu, text="Sign In", width=15, bg='#1ca509', fg='black',
                   command=log)
In_button.pack(pady=10)

out_button = Button(logstu, text="Sign Out", width=15, bg='#1ca509', fg='black',
                    command=out)
out_button.pack(pady=10)

visit_button = Button(logstu, text="Sign Visitors", width=15, bg='#1ca509', fg='black',
                      command=visitor)
visit_button.pack(pady=10)

bck_button = Button(logstu, text="Back to Admin", width=15, bg='#1ca509', fg='black',
                    command=back)
bck_button.pack(pady=10)

# Keep my GUI Looping
logstu.mainloop()

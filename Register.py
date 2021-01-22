import tkinter
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# function to open this module
def popup():
    pass


# GUI properties/styles
litha = Tk()
litha.geometry("700x800")
litha.title('Log - In Page')
litha.configure(background='white')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='Lifechoicesonline',
                               host='127.0.0.1',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


# Getting Data
def post():
    a = Name.get()
    b = Surname.get()
    c = Phone.get()
    d = Position.get()

    sql = "INSERT INTO Users (firstname, surname, Cell_no, Position) VALUES (%s, %s, %s, %s)"
    val = (a, b, c, d)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    messagebox.showinfo('Data inserted', 'Successfully Recorded \n Continue to login page!')
    litha.destroy()
    import LoginPage
    LoginPage.popup()


head = Label(litha, text='Life Choices Online', font='times 12 bold ',
             fg='#19C300',
             bg='white')
head.pack()

reg_frame = Frame(litha)
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- REGISTERATION FORM -',
                font='times 22 bold underline',
                fg='#0B5800',
                bg='white')
heading.pack(pady=10)

entry_log = Label(litha, text="Enter Your Name:",
                  font='arial 15 bold italic',
                  fg='#1ca509',
                  bg='white')
entry_log.pack(pady=10)
Name = Entry(width=25)
Name.pack(pady=15)

Surname = Label(litha, text="Enter Surname:",
                font='arial 15 bold italic',
                fg='#1ca509',
                bg='white')
Surname.pack(pady=10)
Surname = Entry(width=25)
Surname.pack(pady=15)

entry_log = Label(litha, text="Enter Cellphone Number:",
                  font='arial 15 bold italic',
                  fg='#1ca509',
                  bg='white')
entry_log.pack(pady=10)
Phone = Entry(width=25)
Phone.pack(pady=15)

# ============================Gender
gen_lab = Label(litha, text="Position", font=("arial", 12, 'bold'), bg='white', fg='#1ca509')
gen_lab.pack()
Position = ttk.Combobox(litha, state="readonly")
Position['values'] = ('Admin', "Student", "Visitor")
Position.pack()

myButton = Button(litha, text="Register", width=15, bg='#1ca509', fg='black', command=post)
myButton.pack(pady=11)


def back():
    litha.destroy()
    import Landing
    Landing.popup()


myButton = Button(litha, text="Back to landing page", width=15, bg='#1ca509', fg='black', command=back)
myButton.pack(pady=11)

litha.mainloop()

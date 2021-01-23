import tkinter
import mysql.connector
from tkinter import *
from tkinter import messagebox


# function to open this module
def popup():
    pass


# GUI properties/styles
litha = Tk()
litha.geometry("540x500")
litha.title('Lifechoices Academy Log - In Page')
litha.configure(background='#D4F1BE')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='Lifechoicesonline',
                               host='127.0.0.1',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def verify():
    user_verification = Username.get()
    pass_verification = Password.get()
    sql = "select * from Admin_Staff where LastName = %s and Password = %s"
    mycursor.execute(sql, [(user_verification), (pass_verification)])
    results = mycursor.fetchall()
    if results:
        for x in results:
            logged()
            break
    else:
        failed()


def logged():
    messagebox.showinfo("You have Successfully \n Logged In ", "WELCOME")
    litha.destroy()
    import testing
    testing.initialize_user_interface()


def failed():
    messagebox.showerror("admin log in only", 'UNKNOWN USER')
    Username.delete(0, END)
    Password.delete(0, END)


head = Label(litha, text='Life Choices Online', font='times 12 bold ',
             fg='#19C300',
             bg='#D4F1BE')
head.pack()

reg_frame = Frame(litha, bg='#D4F1BE')
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- LOGIN PAGE -',
                font='times 22 bold underline',
                fg='#0B5800',
                bg='#D4F1BE')
heading.pack(pady=10)

entry_log = Label(litha, text="Enter username:",
                  font='arial 15 bold italic',
                  fg='#1ca509',
                  bg='#D4F1BE')
entry_log.pack(pady=10)

Username = Entry(width=25)
Username.pack(pady=15)

entry_log = Label(litha, text="Please enter password:",
                  font='arial 15 bold italic',
                  fg='#1ca509',
                  bg='#D4F1BE')
entry_log.pack(pady=10)

Password = Entry(width=20, show='*')
Password.pack(pady=10)

myButton = Button(litha, text="LOGIN", width=15, bg='#1ca509', fg='black', command=verify)
myButton.pack(pady=11)

litha.mainloop()

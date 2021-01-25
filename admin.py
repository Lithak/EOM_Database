# LITHA KANE'S DATABASE WORK
# THIS IS MY 4th INTERFACE

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import mysql.connector


# function to open this module
def popup():
    pass


# GUI properties/styles
admin = Tk()
admin.title("ADMINISTRATOR")
admin.geometry("700x680")
admin.config(background='#ABC895')

# DATABASE CONNECTOR STATEMENT
mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1',
                               database='Lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

# My Labels & Headings
head = Label(admin, text='Life Choices Online', font='times 12 bold ',
             fg='#19C300',
             bg='#ABC895')
head.pack()

# Frame & Labels
reg_frame = Frame(admin, bg='#ABC895')
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- REGISTER STUDENTS -',
                font='times 22 bold underline',
                fg='#0B5800',
                bg='#ABC895')
heading.pack(pady=10)

# Labels & their entries
firstname = Label(admin, text="Firstname", font='arial 10 bold',
                  fg='black',
                  bg='#ABC895')
firstname.pack(pady=7, padx=10)

name = Entry(admin)
name.pack(pady=7, padx=10)

user_lbl = Label(admin, text="Surname", font='arial 10 bold',
                 fg='black',
                 bg='#ABC895')
user_lbl.pack(pady=7, padx=10)

Username = Entry(admin)
Username.pack(pady=7, padx=10)

phone_lbl = Label(admin, text="Phone number", font='arial 10 bold',
                  fg='black',
                  bg='#ABC895')
phone_lbl.pack(pady=7, padx=10)

Cell_no = Entry(admin)
Cell_no.pack(pady=12, padx=10)

# Combobox to choose position
gen_lab = Label(admin, text="Position", font=("arial", 12, 'bold'), bg='#ABC895', fg='black')
gen_lab.pack(pady=6)
com = ttk.Combobox(admin, state="readonly")
com['values'] = ('Student', "Visitor", "Other")
com.pack(pady=10)


# INSERT FUNCTION
def reg():
    a = name.get()
    b = Username.get()
    c = Cell_no.get()
    d = com.get()

    sql = "INSERT INTO Users (firstname, surname, Cell_no, Position) VALUES (%s, %s, %s, %s)"
    val = (a, b, c, d)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    messagebox.showinfo('Data inserted', 'Successfully Recorded \n Continue to login page!')

    try:
        mycursor.execute(sql, val)

        mydb.commit()

    except:
        messagebox.showinfo("DONE", "Successfully")
        Username.delete(0, END)
        com.delete(0, END)
        Cell_no.delete(0, END)
        name.delete(0, END)


# DELETE Function
def delete():
    firstname = str(name.get())
    sql_Delete_query = "DELETE FROM Users WHERE firstname = %s"

    mycursor.execute(sql_Delete_query, [firstname])

    messagebox.showinfo("DONE", " delete succesfully")
    mydb.commit()
    name.delete(0, END)
    Username.delete(0, END)
    com.delete(0, END)
    Cell_no.delete(0, END)


# Update function
def update():
    a = name.get()
    b = Username.get()
    c = Cell_no.get()
    d = com.get()

    sql = "Update Users SET firstname=%s, surname=%s, Cell_no=%s where Position = %s;"

    mycursor.execute(sql, [(b), (c), (d), (a)])
    mydb.commit()
    name.delete(0, END)
    Username.delete(0, END)
    com.delete(0, END)
    Cell_no.delete(0, END)

# View Info on display function
def view():
    mycursor.execute("Select * from Users")
    for i in mycursor:
        diplay_names.insert(END, i)

    name.delete(0, END)
    Username.delete(0, END)
    com.delete(0, END)
    Cell_no.delete(0, END)


# Go to LogIn function
def exit_window():
    messagebox.askquestion('Sing In & Out Students?', 'GO Sign In & Out Students?')
    admin.destroy()
    import LogIn


# MY Listbox to show data from database
diplay_names = Listbox(admin, bg="#ABC895", fg="black", width=60, selectbackground="white", selectforeground="black")
diplay_names.pack(pady=9)

# Frame for my Buttons to line up
btn_frame = Frame(admin, bg='#ABC895')
btn_frame.pack()

# My buttons to call the above functions
insert_button = Button(btn_frame, text="New Student", bg='#1ca509', fg='black', command=reg)
insert_button.grid(row=0, column=1, padx=10)

get_button = Button(btn_frame, text="GET", bg='#1ca509', fg='black', command=view)
get_button.grid(row=0, column=2, padx=10)

delete_button = Button(btn_frame, text="DELETE", bg='#1ca509', fg='black', command=delete)
delete_button.grid(row=0, column=3, padx=10)

update_button = Button(btn_frame, text="UPDATE", bg='#1ca509', fg='black', command=update)
update_button.grid(row=0, column=4, padx=10)

exit_button = Button(btn_frame, text="Sign Students", bg='#1ca509', fg='black', command=exit_window)
exit_button.grid(row=0, column=6, padx=10)

# keep my window live
admin.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import mysql.connector


# function to open this module
def popup():
    pass


root = Tk()
root.title("ADMINISTRATOR")
root.geometry("700x680")
root.config(background='#ABC895')

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1',
                               database='Lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

head = Label(root, text='Life Choices Online', font='times 12 bold ',
             fg='#19C300',
             bg='#ABC895')
head.pack()

reg_frame = Frame(root, bg='#ABC895')
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- ADMINISTRATOR -',
                font='times 22 bold underline',
                fg='#0B5800',
                bg='#ABC895')
heading.pack(pady=10)

firstname = Label(root, text="Firstname", font='arial 10 bold',
                  fg='black',
                  bg='#ABC895')
firstname.pack(pady=7, padx=10)

name = Entry(root)
name.pack(pady=7, padx=10)

user_lbl = Label(root, text="Surname", font='arial 10 bold',
                 fg='black',
                 bg='#ABC895')
user_lbl.pack(pady=7, padx=10)

Username = Entry(root)
Username.pack(pady=7, padx=10)

Description_lbl = Label(root, text="Phone number", font='arial 10 bold',
                        fg='black',
                        bg='#ABC895')
Description_lbl.pack(pady=7, padx=10)

Cell_no = Entry(root)
Cell_no.pack(pady=12, padx=10)

gen_lab = Label(root, text="Position", font=("arial", 12, 'bold'), bg='#ABC895', fg='black')
gen_lab.pack(pady=6)
com = ttk.Combobox(root, state="readonly")
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
    name.delete(0, END)

    mydb.commit()


def update():
    a = name.get()
    b = Username.get()
    c = Cell_no.get()
    d = com.get()

    sql = "Update Users SET firstname=%s, surname=%s, Cell_no=%s where Position = %s;"

    mycursor.execute(sql, [(b), (c), (d), (a)])

    mydb.commit()


def view():
    mycursor.execute("Select * from Users")
    for i in mycursor:
        diplay_names.insert(END, i)


def exit_window():
    message_box = messagebox.askquestion('Exit ADMIN', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        root.destroy()
        import testing
    else:
        pass


diplay_names = Listbox(root, bg="#ABC895", fg="black", width=60, selectbackground="white", selectforeground="black")
diplay_names.pack(pady=9)

btn_frame = Frame(root, bg='#ABC895')
btn_frame.pack()

insert_button = Button(btn_frame, text="New Student", bg='#1ca509', fg='black', command=reg)
insert_button.grid(row=0, column=1, padx=10)

get_button = Button(btn_frame, text="GET", bg='#1ca509', fg='black', command=view)
get_button.grid(row=0, column=2, padx=10)

delete_button = Button(btn_frame, text="DELETE", bg='#1ca509', fg='black', command=delete)
delete_button.grid(row=0, column=3, padx=10)

update_button = Button(btn_frame, text="UPDATE", bg='#1ca509', fg='black', command=update)
update_button.grid(row=0, column=4, padx=10)

exit_button = Button(btn_frame, text="Exit", bg='#1ca509', fg='black', command=exit_window)
exit_button.grid(row=0, column=6, padx=10)

root.mainloop()

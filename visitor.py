# LITHA KANE'S DATABASE WORK
# THIS IS MY 6th INTERFACE

import tkinter as tk
import mysql
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import *


# My GUI in Class form
class Application(tk.Frame):
    def __init__(self, root):
        self.visit = root
        self.visit.geometry('950x750')
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.visit.title("Lifechoices - Visitor page")
        self.visit.grid_rowconfigure(0, weight=1)
        self.visit.grid_columnconfigure(0, weight=1)
        self.visit.config(background="#ABC895")

        # Time & Date
        self.clock = tk.Label(self.visit, font="bold")
        self.clock.grid(row=0, column=0)

        time = datetime.now()
        self.clock.config(text=time.strftime('Date: ' + "%d/%m/%y\n" + 'Time: ' + "%H:%M:%S %p"), font='times 15',
                          fg='black', bg='#ABC895')

        self.heading = tk.Label(self.visit, text='- SIGNING VISITOR -',
                                font='times 22 bold underline',
                                fg='#0B5800',
                                bg='#ABC895')
        self.heading.grid(row=0, column=1)

        # GUI widgets (Labels, entries & buttons)
        self.name_label = tk.Label(self.visit, text="Name:", font='arial 15 bold',
                                   fg='black',
                                   bg='#ABC895')
        self.name_label.grid(row=1, column=0)

        self.name_entry = tk.Entry(self.visit)
        self.name_entry.grid(row=1, column=1, pady=10)

        self.idnumber_label = tk.Label(self.visit, text="Position:", font='arial 15 bold',
                                       fg='black',
                                       bg='#ABC895')
        self.idnumber_entry = tk.Entry(self.visit)
        self.idnumber_label.grid(row=2, column=0)
        self.idnumber_entry.grid(row=2, column=1, pady=40)

        # Option to choose gender
        self.gen_lab = tk.Label(self.visit, text="Gender", font=("arial", 12, 'bold'), bg='#ABC895', fg='black')
        self.gen_lab.grid(row=3, column=0)
        com = ttk.Combobox(self.visit, state="readonly")
        com['values'] = ('Male', "Female", "Other")
        com.grid(row=3, column=1, pady=20)

        # My buttons for the below functions
        self.submit_button = tk.Button(self.visit, text="Sign In", width=15, bg='#1ca509', fg='black',
                                       command=self.insert_data)
        self.submit_button.grid(row=5, column=0)

        self.delete_button = tk.Button(self.visit, text="Delete", width=15, bg='#1ca509', fg='black',
                                       command=self.delete_data)
        self.delete_button.grid(row=5, column=1)

        self.exit_button = tk.Button(self.visit, text=" Back to Students", width=15, bg='#1ca509', fg='black',
                                     command=self.back)
        self.exit_button.grid(row=5, column=2, pady=40)

        # Set the treeview
        self.tree = ttk.Treeview(self.visit, columns=('Name', 'Position', 'Status', 'Time', 'Date'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Status')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Position')
        self.tree.heading('#3', text='Time')
        self.tree.heading('#4', text='Date')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)
        self.tree.column('#4', stretch=tk.YES)

        self.tree.grid(row=6, columnspan=4, rowspan=10)
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    # Insert to a non-Database table on screen
    def insert_data(self):
        now = datetime.now()
        time = now.strftime("%H:%M")
        self.treeview.insert('', 'end', iid=self.iid, text="Signed_In" + str(self.id),
                             values=(self.name_entry.get(),
                                     self.idnumber_entry.get(), time, now))
        self.iid = self.iid + 1
        self.id = self.id + 1

    # Remove Info from Table function
    def delete_data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)

    # Go to Students page function
    def back(self):
        self.visit.destroy()
        import admin
        admin.popup()


# Loop my Visitor Screen
app = Application(tk.Tk())
app.visit.mainloop()

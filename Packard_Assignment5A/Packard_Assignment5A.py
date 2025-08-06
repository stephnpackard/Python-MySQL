from tkinter import *
from tkinter import messagebox as mb
import sqlite3

class searchContact:
    def __init__(self):
        self.root = Tk()
        self.root.title("Contacts")

        self.first = Label(self.root, text="First Name").grid(column=0, row=0, padx=5, pady=5)
        self.firstStr = StringVar()
        self.firstBox = Entry(self.root, textvariable=self.firstStr).grid(column=1, row=0, padx=5, pady=5)

        self.last = Label(self.root, text="Last Name").grid(column=2, row=0, padx=5, pady=5)
        self.lastStr = StringVar()
        self.lastBox = Entry(self.root, textvariable=self.lastStr).grid(column=3, row=0, padx=5, pady=5)

        self.phone = Label(self.root, text="Phone Number").grid(column=2, row=1, padx=5, pady=5)
        self.phoneStr = StringVar()
        self.phoneBox = Entry(self.root, textvariable=self.phoneStr, state='readonly').grid(column=3, row=1, padx=5, pady=5)

        self.commandButton = Button(self.root, text="Submit", command=self.display).grid(row=1, columnspan=2, padx=5, pady=5)

    def display(self):
        conn = sqlite3.connect('ContactsDB.db')
        c = conn.cursor()
        firstName = self.firstStr.get().lower()
        lastName = self.lastStr.get().lower()
        try:
            if (firstName == ""):
                raise Exception()
            if (lastName == ""):
                raise Exception()
            c.execute("SELECT PhoneNumber FROM Contacts WHERE FirstName=? AND LastName=?",(firstName,lastName,))
            self.phoneBox = Entry(self.root, state='normal')
            results = c.fetchall()
            if (results == None):
                self.phoneStr.set("N/A")
            elif (results == []):
                self.phoneStr.set("N/A")
            else:
                for person in results:
                    self.phoneStr.set(person[0])
            self.phoneBox = Entry(self.root, state='readonly')
            conn.close()
        except:
            w = mb.showerror('Error', 'Please be sure to fill out both the first and last names.')
            conn.close()
        
searchContact = searchContact()

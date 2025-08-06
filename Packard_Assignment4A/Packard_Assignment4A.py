from tkinter import *
from tkinter import messagebox as mb
import sqlite3

class addContact:
    def __init__(self):
        self.root = Tk()
        self.root.title("Contacts")
        self.root.columnconfigure(0, weight = 1)
        self.root.columnconfigure(1, weight = 1)

        self.id = Label(self.root, text="ID Value").grid(column=0, row=0, padx=5, pady=5)
        self.idStr = StringVar()
        self.idBox = Entry(self.root, textvariable=self.idStr).grid(column=1, row=0, padx=5, pady=5)

        self.first = Label(self.root, text="First Name").grid(column=0, row=1, padx=5, pady=5)
        self.firstStr = StringVar()
        self.firstBox = Entry(self.root, textvariable=self.firstStr).grid(column=1, row=1, padx=5, pady=5)

        self.last = Label(self.root, text="Last Name").grid(column=0, row=2, padx=5, pady=5)
        self.lastStr = StringVar()
        self.lastBox = Entry(self.root, textvariable=self.lastStr).grid(column=1, row=2, padx=5, pady=5)

        self.phone = Label(self.root,text="Phone Number").grid(column=0, row=3, padx=5, pady=5)
        self.phoneStr = StringVar()
        self.phoneBox = Entry(self.root, textvariable=self.phoneStr).grid(column=1, row=3, padx=5, pady=5)

        self.commandButton = Button(self.root, text="Submit", command=self.display).grid(row = 4, columnspan=2, padx=5, pady=5)

    def display(self):
        conn = sqlite3.connect('ContactsDB.db')
        c = conn.cursor()
        custID = self.idStr.get()
        firstName = self.firstStr.get().lower()
        lastName = self.lastStr.get().lower()
        phone = self.phoneStr.get()
        try:
            if (custID ==""):
                raise Exception()
            if (firstName ==""):
                raise Exception()
            if (lastName ==""):
                raise Exception()
            if (phone ==""):
                raise Exception()
            custID = int(custID)
            c.execute("INSERT INTO Contacts (CustomerID, FirstName, LastName, PhoneNumber) VALUES(?,?,?,?)", (custID, firstName, lastName, phone,))
            w = mb.showinfo("Submit", "Customer "+firstName.title()+" "+lastName.title()+" with the phone number "+phone+" was added with the customer ID of "+str(custID)+".")
            conn.commit()
            conn.close()
        except ValueError:
            w = mb.showerror('Error', 'Please be sure that the ID Value is a whole number.')
            conn.close()
        except:
            w = mb.showerror('Error', 'Please fill out all boxes and try again.')
            conn.close()
            

addContact = addContact()

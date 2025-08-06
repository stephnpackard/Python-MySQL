

from tkinter import *
from tkinter import messagebox as mb
import sqlite3

class EmptyException(Exception):
    pass

class records:
    def __init__(self):
        self.root = Tk()
        self.root.title("Records")

        self.id = Label(self.root, text="ID Number").grid(column=0, row=0, padx=2, pady=2)
        self.idStr = StringVar()
        self.idBox = Entry(self.root, textvariable=self.idStr)
        self.idBox.grid(column=1,row=0,padx=2,pady=2)

        self.name = Label(self.root, text="Name").grid(column=0, row=1, padx=2, pady=2)
        self.nameStr = StringVar()
        self.nameBox = Entry(self.root, textvariable=self.nameStr)
        self.nameBox.grid(column=1, row=1, padx=2, pady=2)

        self.category = Label(self.root, text="Category").grid(column=0, row=2, padx=2, pady=2)
        self.categoryStr = StringVar()
        self.categoryBox = Entry(self.root, textvariable=self.categoryStr)
        self.categoryBox.grid(column=1, row=2, padx=2, pady=2)

        self.price = Label(self.root, text="Price").grid(column=0, row=3, padx=2, pady=2)
        self.priceStr = StringVar()
        self.priceBox = Entry(self.root, textvariable=self.priceStr)
        self.priceBox.grid(column=1, row=3, padx=2, pady=2)

        self.onHand = Label(self.root, text="On Hand").grid(column=0, row=4, padx=2, pady=2)
        self.onHandStr = StringVar()
        self.onHandBox = Entry(self.root, textvariable=self.onHandStr)
        self.onHandBox.grid(column=1, row=4, padx=2, pady=2)

        self.saveRecordButton = Button(self.root, text="Save Record", command=self.saveRecord).grid(row=5, column=0, columnspan=2, padx=2, pady=2)

        self.clearTextButton = Button(self.root, text="Clear Text", command=self.clearText).grid(row=6, column=0, columnspan=2, padx=2, pady=2)

        self.textBox = Text(self.root, height=8, width=35, state='disabled')
        self.textBox.grid(row=0, column=3, rowspan=5, columnspan=2, padx=2, pady=2)

        self.productName = Label(self.root, text="Product Name").grid(column=3, row=5, padx=2, pady=2)
        self.productNameStr = StringVar()
        self.productNameBox = Entry(self.root, textvariable=self.productNameStr)
        self.productNameBox.grid(column=4, row=5, padx=2, pady=2)

        self.displayRecord = Button(self.root, text="Display Record", command=self.displayRecord).grid(row=6, column=3, padx=2, pady=2)

        self.clearDisplayText = Button(self.root, text="Clear Text", command=self.clearDisplayText).grid(row=6, column=4, padx=2, pady=2)

    def saveRecord(self):
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        idNumber = self.idStr.get().lower()
        name = self.nameStr.get().title()
        category = self.categoryStr.get().title()
        price = self.priceStr.get().lower()
        onHand = self.onHandStr.get().lower()

        try:
            if (idNumber == "") or (name == "") or (category == "") or (price == "") or (onHand == ""):
                raise EmptyException()
            idNumber = int(idNumber)
            price = float(price)
            onHand = int(onHand)
            #check for id match
            c.execute("SELECT PRODNAME FROM PRODUCTS WHERE ID=?",(idNumber,))
            results = c.fetchall()
            if (results == None) or (results == []):
                #check for product name match
                c.execute("SELECT ID FROM PRODUCTS WHERE PRODNAME=?",(name,))
                results = c.fetchall()
                if (results == None) or (results == []):
                    c.execute("INSERT INTO PRODUCTS VALUES(?,?,?,?,?)", (idNumber, category, name, price, onHand,))
                    mb.showinfo("Save Record", "Product with ID number "+str(idNumber)+" of "+name+" in "+category+" costing $"+str(price)+" with "+str(onHand)+" on hand succesfully added.")
                    self.idBox.delete(0, "end")
                    self.nameBox.delete(0, "end")
                    self.categoryBox.delete(0, "end")
                    self.priceBox.delete(0, "end")
                    self.onHandBox.delete(0, "end")
                    conn.commit()
                else:
                    mb.showerror('Error', 'A product with that name already exists, please choose another name.')
                    conn.close()
            else:
                mb.showerror('Error', 'A product with that ID number already exists, please choose another ID number.')
                conn.close()
            conn.close()
        except ValueError:
            mb.showerror('Error', 'Please ensure that the ID number and on hand are numbers and the price is a decimal number.')
            conn.close()
        except EmptyException:
            mb.showerror('Error', 'Please be sure to fill out all boxes.')
            conn.close()

    def clearText(self):
        self.idBox.delete(0, "end")
        self.nameBox.delete(0, "end")
        self.categoryBox.delete(0, "end")
        self.priceBox.delete(0, "end")
        self.onHandBox.delete(0, "end")

    def displayRecord(self):
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        productName = self.productNameStr.get().title()

        try:
            if (productName == ""):
                raise EmptyException()
            c.execute("SELECT * FROM PRODUCTS WHERE PRODNAME=?",(productName,))
            results = c.fetchall()
            self.textBox.configure(state='normal')
            self.textBox.delete('1.0', "end")
            if (results == None) or (results == []):
                self.textBox.insert(INSERT, 'Product Name '+productName+' not found.')
            else:
                for product in results:
                    idNumber = product[0]
                    category = product[1]
                    name = product[2]
                    price = product[3]
                    onHand = product[4]
                    self.textBox.insert(INSERT, "ID Number: "+str(idNumber)+"\nName: "+name+"\nCategory: "+category+"\nPrice: $"+str(price)+"\nOnhand: "+str(onHand))
            self.textBox.configure(state='disabled')
            conn.close()
        except EmptyException:
                mb.showerror('Error', 'Please fill out the Product Name.')

    def clearDisplayText(self):
        self.textBox.configure(state='normal')
        self.textBox.delete('1.0', "end")
        self.textBox.configure(state='disabled')
        self.productNameBox.delete(0, "end")

records = records()

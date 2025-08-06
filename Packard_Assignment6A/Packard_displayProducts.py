import sqlite3
conn = sqlite3.connect('Inventory.db')

c= conn.cursor()

def personalHeading(assignNum):
    print("Assignment {}\n".format(assignNum)
          + "Programmed by Stephanie Packard\n"
          + "Welcome to the inventory database program.")

def getClosing():
    conn.commit()
    conn.close()
    print()
    input("Thanks for using the inventory database program.\n"
          + "press the enterKey to end..")

def displayProducts():
    c.execute("SELECT * FROM Products")
    product = c.fetchall()
    print(f"{'ID':<5} {'Name':20} {'Inspection Code':20} {'Approved Date':<20}")
    for item in product:
        print(f"{item[0]:<5} {item[1].title():20} {item[2]:<20} {item[3]:<20}")

def displayDetails():
    c.execute("SELECT * FROM ProductDetails")
    product = c.fetchall()
    print(f"{'ID':<5} {'Manufacturer':20} {'Price':5}")
    for item in product:
        print(f"{item[0]:<5} {item[1].title():20} ${item[2]:<5.2f}")

def displayAll():
    c.execute("SELECT Products.PName, ProductDetails.PManu, ProductDetails.Price FROM Products INNER JOIN ProductDetails on Products.ProductID = ProductDetails.ProductID");
    product = c.fetchall()
    print(f"{'Name':20} {'Manufacturer':20} {'Price':<5}")
    for item in product:
        print(f"{item[0].title():20} {item[1]:20} ${item[2]:<5.2f}")

def main():
    assignNum = "6A"
    personalHeading(assignNum)
    print()
    displayProducts()
    print()
    displayDetails()
    print()
    displayAll()
    getClosing()

if __name__ == "__main__":
    main()

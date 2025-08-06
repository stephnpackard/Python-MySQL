import sqlite3
conn = sqlite3.connect('Inventory.db')

c = conn.cursor()

tableString = """CREATE TABLE ProductDetails(
    ProductID    INTEGER not null,
    PManu        VARCHAR(30) not null,
    Price        FLOAT not null,
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID))"""

c.execute(tableString)

c.execute("INSERT INTO ProductDetails VALUES (1, 'Dessert Company', 4.50)")
c.execute("INSERT INTO ProductDetails VALUES (2, 'Dessert Company', 2.70)")
c.execute("INSERT INTO ProductDetails VALUES (3, 'Donut Company', 1.80)")
c.execute("INSERT INTO ProductDetails VALUES (4, 'Pudding & Stuff', 3.40)")
c.execute("INSERT INTO ProductDetails VALUES (5, 'I Scream', 2.85)")
c.execute("INSERT INTO ProductDetails VALUES (6, 'Dessert Company', 2.90)")

conn.commit()

conn.close()

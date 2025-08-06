import sqlite3
conn = sqlite3.connect('Inventory.db')

c = conn.cursor()

tableString = """CREATE TABLE Products(
    ProductID      INTEGER not null primary key,
    PName          VARCHAR(33) not null,
    InspectionCode INTEGER,
    ApprovedDate   VARCHAR(10))"""

c.execute(tableString)

c.execute("INSERT INTO Products VALUES (1, 'Cake', 923, '10/24/21')")
c.execute("INSERT INTO Products VALUES (2, 'Cupcake', 923, '10/10/21')")
c.execute("INSERT INTO Products VALUES (3, 'Donut', 923, '10/13/21')")
c.execute("INSERT INTO Products VALUES (4, 'Pudding', 923, '9/27/21')")
c.execute("INSERT INTO Products VALUES (5, 'Ice Cream', 923, '10/4/21')")
c.execute("INSERT INTO Products VALUES (6, 'Cheesecake', 923, '10/23/21')")

conn.commit()

conn.close()

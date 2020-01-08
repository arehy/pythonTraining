import sqlite3

conn = sqlite3.connect('sqlite.db')

c = conn.cursor()

# Create table
""" c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''') """

# Insert a row of data
""" c.execute("INSERT INTO stocks VALUES ('2020-01-06','Kacsa','Kiskacsa',665,3.14)") """
c.execute("UPDATE stocks SET price = 40 WHERE trans = 'Kacsa'")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
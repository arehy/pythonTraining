import sqlite3
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
  print (row)
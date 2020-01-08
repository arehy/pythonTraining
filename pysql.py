import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Kiskacsa",
  passwd="matrix",
  database="mydatabase"
)

mycursor = mydb.cursor()

#ezzel lehet táblát létrehozni, benne az oszlopokkal
""" mycursor.execute("CREATE TABLE csalad (Fido VARCHAR(255), Tapp VARCHAR(255), Brumm VARCHAR(255))") """

#ezzel lehet meglévő táblához oszlopokat hozzáadni
""" mycursor.execute("ALTER TABLE csalad ADD COLUMN Kyra VARCHAR(255)")
mycursor.execute("ALTER TABLE csalad ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") """

#ezzel lehet az oszlopokat feltölteni
""" sql = "INSERT INTO csalad (Brumm, Fido, Tapp, Kyra) VALUES (%s, %s, %s, %s)"
val = ("málna", "kávé", "málna", "finomság")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.") """
#ezzel tömbbel lehet oszlopokat feltölteni (a különbség, hogy 'execute' helyett 'executemany' van)
""" sql = "INSERT INTO csalad (Brumm, Fido, Tapp, Kyra) VALUES (%s, %s, %s, %s)"
val = [
  ('macicsajok', 'kutyuscsajok', 'macilányok', 'szomszéd fekete cica'),
  ('szánkó', 'szánkó', 'szánkó', 'szánkó'),
  ('málnatorta', 'véreslábszár', 'málnajoghurt', 'kukorica')
]
mycursor.executemany(sql, val)
mydb.commit() """

#ezzel lehet az adatokat módosítani
sql = "UPDATE csalad SET Kyra = 'nyitott ajtók' WHERE id = '4'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")



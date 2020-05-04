import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_insert(con, entities):
    cursorObj = con.cursor()

    #cursorObj.execute("CREATE TABLE tienda(id, producto, precio)")
    cursorObj.execute('INSERT INTO tienda(id, producto, precio) VALUES(?, ?, ?)', entities)

    con.commit()

entities = (4, "aji", 2.00)

sql_insert(con, entities)
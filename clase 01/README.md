SQLite3 se trata de un sistema de gestión de base de datos relacional, aunque SQLite no es un motor de base de datos cliente-servidor. Usualmente es más útil usarlo para crear prototipos o MVP de aplicaciones con respecto a la base de datos, para luego mudar a otra base de datos como PostgreSQL, por ejemplo.

Para importar SQLite3 ya sea en Google Colab o Anaconda (Jupiter o VSCode), se ejecutan los siguientes comandos:

---

import sqlite3
conn = sqlite3.connect('example.db')

---

Luego de que tenga una conexión, puedo crear una tabla con sus columnas respectivas

---

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

---

Para luego ingresar datos por cada columna (por cada fila):

---

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


---
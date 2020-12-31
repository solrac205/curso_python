# python puede manejar diferentes bases de datos
# entre las cuales se puede mencionar las siguientes:
# * SQL Server
# * Oracle
# * MySQL
# * SQLite
# * PostgreSQL
# * etc.
import os
import sqlite3

def ClrScr(): #Definimos la función estableciendo el nombre que queramos
    if (os.name == "posix"):
        os.system ("clear")
    elif ((os.name == "ce") or 
          (os.name == "nt") or 
          (os.name == "dos")):
        os.system ("cls")

ClrScr()

MiConexion=sqlite3.connect("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\BasesDatosPython\\BaseSQLitePy.db")

miCursor=MiConexion.cursor()

# ****************************************************
# Insertar datos a tabla por lote de datos.
# ****************************************************
"""
VariosProductos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarrón",90,"Cerámica"),
    ("Camión",20,"Juguetería")
]

miCursor.executemany("INSERT INTO PRODUCTOS " +
                     "VALUES(?,?,?);",VariosProductos)
"""
# ****************************************************

miCursor.execute("SELECT * FROM PRODUCTOS;")

LeeProductos=miCursor.fetchall()

for Producto in LeeProductos:
    print("Nombre Artículo: ", Producto[0], " Sección: ", Producto[2])



MiConexion.commit()

MiConexion.close()

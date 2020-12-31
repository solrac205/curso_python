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

MiConexion=sqlite3.connect("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\BasesDatosPython\\GestionProductos.db")

miCursor=MiConexion.cursor()

# Si el código del producto se desea que sea númerico,
# y que autoincremente automaticamente se debería declarar
# CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
try:
    QuerySQLite='''
            CREATE TABLE PRODUCTOS(
                CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
                NOMBRE_ARTICULO VARCHAR(50),
                PRECIO DECIMAL(10,2),
                SECCION VARCHAR(20)
            );
    '''
    miCursor.execute(QuerySQLite)

    MiConexion.commit()
except:
    QuerySQLite='''
        DROP TABLE PRODUCTOS;
    '''
    miCursor.execute(QuerySQLite)

    MiConexion.commit()

    QuerySQLite='''
            CREATE TABLE PRODUCTOS(
                CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
                NOMBRE_ARTICULO VARCHAR(50),
                PRECIO DECIMAL(10,2),
                SECCION VARCHAR(20)
            );
    '''
    miCursor.execute(QuerySQLite)

    MiConexion.commit()

# Si se trabaja con el autoincrement en la lista de productos
# a insertar no se coloca el campo que se realiza el autoincrement
# y en la instruccion de insert en lugar del signo ?
# del campo que se autoincrementará se coloca NULL, esto
# permitirá la autoincrementación del código. (VALUES(NULL,?,?,?))

VariosProductos=[
    ("AR01","Pelota", 20.50, "Juguetería"),
    ("AR02","Pantalón", 15.75,"Confección"),
    ("AR03","Destornillador", 25.05,"Ferretería"),
    ("AR04","Jarrón", 45,"Cerámica"),
    ("AR05","Tren", 15.99,"Juguetería")
]

miCursor.executemany("INSERT INTO PRODUCTOS " +
                     "VALUES(?,?,?,?);",VariosProductos)



MiConexion.commit()

MiConexion.close()

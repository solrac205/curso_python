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
#***********************************************************
MiConexion=sqlite3.connect("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\BasesDatosPython\\GestionProductos2.db")

miCursor=MiConexion.cursor()
#***********************************************************
try:
    QuerySQLite='''
            CREATE TABLE PRODUCTOS(
                CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
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
                CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
                PRECIO DECIMAL(10,2),
                SECCION VARCHAR(20)
            );
    '''
    miCursor.execute(QuerySQLite)

    MiConexion.commit()
#***********************************************************

try:
    VariosProductos=[
        ("Pelota", 20.50, "Juguetería"),
        ("Pantalón", 15.75,"Confección"),
        ("Destornillador", 25.05,"Ferretería"),
        ("Jarrón", 45,"Cerámica"),
        ("Tren", 15.99,"Juguetería"),
        ("Trenes", 45.99,"Juguetería")
    ]

    miCursor.executemany("INSERT INTO PRODUCTOS " +
                        "VALUES(NULL,?,?,?);",VariosProductos)

    MiConexion.commit()
except:
    print("Registros ya existentes.")
finally:
    print("Registros insertados.")
#***********************************************************

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección';")

LeeProductos=miCursor.fetchall()

print("Al Insertar...")

for Producto in LeeProductos:
    print(Producto)
#***********************************************************

miCursor.execute('''
          UPDATE PRODUCTOS 
          SET PRECIO=16.50 
          WHERE NOMBRE_ARTICULO='Pantalón';
          ''')
MiConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección';")

LeeProductos=miCursor.fetchall()
print("Al Actualizar...")
for Producto in LeeProductos:
    print(Producto)
#***********************************************************

miCursor.execute('''
          DELETE 
          FROM PRODUCTOS 
          WHERE NOMBRE_ARTICULO='Pantalón';
          ''')
MiConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección';")

LeeProductos=miCursor.fetchall()
print("Al Borrar...")
for Producto in LeeProductos:
    print(Producto)
#***********************************************************

MiConexion.close()

#***********************************************************
#Toca video  No. 59
#***********************************************************
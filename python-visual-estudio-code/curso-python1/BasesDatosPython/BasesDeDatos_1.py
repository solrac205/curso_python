# python puede manejar diferentes bases de datos
# entre las cuales se puede mencionar las siguientes:
# * SQL Server
# * Oracle
# * MySQL
# * SQLite
# * PostgreSQL
# * etc.

import sqlite3

MiConexion=sqlite3.connect("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\BasesDatosPython\\BaseSQLitePy.db")

miCursor=MiConexion.cursor()
miCursor.execute("CREATE TABLE PRODUCTOS(Nombre_Articulo VARCHAR(50), " +
                                        "Precio INTEGER, " +
                                        "Seccion VARCHAR(20)" +
                                        ")")
MiConexion.commit()

miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES');")
MiConexion.commit()

MiConexion.close()

#Toca Video No. 56
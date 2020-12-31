import sqlite3

class AppDB():
    def __init__(self, PathAndNameDB):
        self.DBName=PathAndNameDB
        self.Estado="No Connected"

    def OpenDB(self):
        try:
            self.MiConexion=sqlite3.connect(self.DBName)
            #self.MiCursor= self.MiConexion.cursor()
            
        except:
            return "Se registro un Error al Abrir Base de Datos"
            self.Estado="No Connected"
        finally:
            self.Estado="Connected"
            return ""

    def CloseDB(self):
        try:
            self.MiConexion.close()
        except:
            self.Estado="Error en Base"
            return "No pudo ser cerrada la base de datos..."

        finally:
            del self.MiConexion
            self.Estado="No Connected"
            return ""
            
    def EstadoDB(self):
        try:
            
            return Estado
        except:
            Estado="Error en Base"
            return Estado

    def ExecQuery(self, SQLQuery):
        try:
            if self.Estado == "Connected":
            
                self.MiCursor= self.MiConexion.cursor()
                self.MiCursor.execute(SQLQuery)
                self.MiConexion.commit()
            else:
                return "Error: Conección no Establecida"


        except:
            return "Error en Sentencia SQL:\n" + SQLQuery
        finally:
            return ""
    





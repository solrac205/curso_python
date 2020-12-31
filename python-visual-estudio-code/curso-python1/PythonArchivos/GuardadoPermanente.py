import os
import MDFncArchivos
import pickle

def ClrScr(): #Definimos la función estableciendo el nombre que queramos
    if (os.name == "posix"):
        os.system ("clear")
    elif ((os.name == "ce") or 
          (os.name == "nt") or 
          (os.name == "dos")):
        os.system ("cls")

ClrScr()

print("******************************************************")
print("Curso No. 41 ... Guardado Permanente..." ) 
print("******************************************************")
print("")

class Persona:

    def __init__(self, Nombre, Genero, Edad):

        self.Nombre=Nombre
        self.Genero=Genero
        self.Edad=Edad
        print("Se ha creado una persona Nueva con el nombre de: ", self.Nombre)

    def __str__(self):
        return "{} {} {}".format(self.Nombre, self.Genero, self.Edad)

class ListaPersonas:
    Personas=[]
    NameFileOut="C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\GuardadoPermanente.cra"

    def __init__(self):

        ListaPersonas=MDFncArchivos.AbrirArchivo(self.NameFileOut,"AgregarBinario+")
        ListaPersonas.seek(0)
        try:
            self.Personas=pickle.load(ListaPersonas)
            print("Se Cargaron {} personas del fichero externo.".format(len(self.Personas)))
        except:
            print("El Registro de personas esta vacio.")
        finally:
            ListaPersonas.close()
            del(ListaPersonas)

    def AgregarPersonas(self, ObjPrsnas):
        self.Personas.append(ObjPrsnas)
        self.GuardarPersonasEnFicheroExterno()

    def MostrarPersonas(self):
        print("La información almacenada en el fichero Externo es: ")
        for p in self.Personas:
            print(p)

    def GuardarPersonasEnFicheroExterno(self):
        ListaPersonas=MDFncArchivos.AbrirArchivo(self.NameFileOut,"EscrituraBinaria")
        try:
            pickle.dump(self.Personas , ListaPersonas)
            
        except:
            print("Error al almacenar información...")
        finally:
            ListaPersonas.close()
            del(ListaPersonas)

MiLista=ListaPersonas()

Prsna=Persona("Sandra","Femenino", 29)
MiLista.AgregarPersonas(Prsna)
#MiLista.MostrarPersonas()

Prsna=Persona("Anysabel","Femenino", 38)
MiLista.AgregarPersonas(Prsna)
#MiLista.MostrarPersonas()

Prsna=Persona("Carlos","Masculino", 42)
MiLista.AgregarPersonas(Prsna)
#MiLista.MostrarPersonas()

MiLista.MostrarPersonas()


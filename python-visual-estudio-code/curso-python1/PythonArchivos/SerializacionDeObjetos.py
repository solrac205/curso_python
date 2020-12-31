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
print("Curso No. 40 ... Serialización II..." ) 
print("******************************************************")
print("")

class Vehiculos():
    def __init__(self, Marca, Modelo):
        self.Marca=Marca
        self.Modelo=Modelo
        self.EnMarcha=False
        self.Acelera=False
        self.Frena=False

    def Arrancar(self):
        self.EnMarcha=True

    def Acelerar(self):
        self.Acelera=True

    def Frenar(self):
        self.Frena=True

    def Estado(self):
        print("Marca: ", self.Marca, 
              "\nModelo: ", self.Modelo,
              "\nEn Marcha: ", self.EnMarcha, 
              "\nAcelerando: ", self.Acelera,
              "\nFrenando: ", self.Frena )


Coche1=Vehiculos("Chevrolet","2011")

Coche2=Vehiculos("Toyota","2016")

Coche3=Vehiculos("Mazda","2018")

Coche4=Vehiculos("Mitsubishi","2011")

ListaCoches=[Coche1, Coche2, Coche3, Coche4]

NameFileOut="C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\PruebaBinaria2.cra"

BinaryFile=MDFncArchivos.AbrirArchivo(NameFileOut,"EscrituraBinaria")

pickle.dump(ListaCoches, BinaryFile)

BinaryFile.close()

del(BinaryFile)

print("La lista de objetos ha sido almacenada en el archivo:\n"+
      NameFileOut)

print("")      
print("******************************************************")


BinaryFile=MDFncArchivos.AbrirArchivo(NameFileOut, "LecturaBinaria")

ListaLectura=""

ListaLectura=pickle.load(BinaryFile)

BinaryFile.close()

del(BinaryFile)

i=0
while i<=len(ListaLectura)-1:

    ListaLectura[i].Estado()
    i=i+1

for c in ListaLectura:
    c.Estado()

print("")
print("******************************************************")
print("")

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
print("Curso No. 39 ... Serialización..." ) 
print("******************************************************")


Lista_Nombres=["Pedro", "Carlos","Luis", "Alejandra", "Andrea","Anysabel"]

BinaryFile=MDFncArchivos.AbrirArchivo("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\PruebaBinaria.cra","EscrituraBinaria")

pickle.dump(Lista_Nombres, BinaryFile)

BinaryFile.close()

del(BinaryFile)
print("La lista de nombres ha sido almacenada en el archivo:\n"+
      "C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\PruebaBinaria.cra")
print("")      

print("******************************************************")

#**************************************************************************************************
BinaryFile=MDFncArchivos.AbrirArchivo("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\PruebaBinaria.cra","LecturaBinaria")

ListaLectura=""

ListaLectura=pickle.load(BinaryFile)

print(ListaLectura)

BinaryFile.close()

del(BinaryFile)

print("")
print("******************************************************")
print("")

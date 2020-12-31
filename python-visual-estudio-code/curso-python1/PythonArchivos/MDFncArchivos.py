# io — Core tools for working with streams
# Source code: Lib/io.py

# https://docs.python.org/3/library/io.html

from io import open

def AbrirArchivo(NombreArchivo, ModoDeApertura):
    
    if (ModoDeApertura=="LecturaYEscritura"):
       return open(NombreArchivo, "r+") 
    elif (ModoDeApertura=="Lectura"):
        return open(NombreArchivo,"r")
    elif (ModoDeApertura=="Escritura"):
        return open(NombreArchivo,"w")
    elif (ModoDeApertura=="AgregaFinal"):
        return open(NombreArchivo,"a")
    elif (ModoDeApertura=="EscrituraBinaria"):
        return open(NombreArchivo,"wb")
    elif (ModoDeApertura=="LecturaBinaria"):
        return open(NombreArchivo, "rb")
    elif (ModoDeApertura=="AgregarBinario+"):
        return open(NombreArchivo, "ab+")
    else:
        return ""


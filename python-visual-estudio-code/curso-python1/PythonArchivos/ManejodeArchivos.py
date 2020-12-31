print("******************************************************")
print("Curso No. 37 ... USO de Archivos Externos..." ) 
print("******************************************************")

# io — Core tools for working with streams
# Source code: Lib/io.py

# https://docs.python.org/3/library/io.html

from io import open

#los archivos pueden ser abiertos en 
#modo Lectura, Escritura o para agregar al final.

ArchivoTexto=open("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\ArchivoPythonPrueba.txt", "w")

frase="Estupendo día para estudiar Python\nel Miércoles"

ArchivoTexto.write(frase)

ArchivoTexto.close()

#**********************************************************
ArchivoTexto=open("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\ArchivoPythonPrueba.txt", "r")

frase=""
frase=ArchivoTexto.read()

print(frase)

ArchivoTexto.close()

#****************************************************************
ArchivoTexto=open("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\ArchivoPythonPrueba.txt", "a")

frase="\n siempre es una buena ocasión para estudiar python"

ArchivoTexto.write(frase)

ArchivoTexto.close()

print("******************************************************")

#**********************************************************
#si se utiliza "r+" indica que es de lectura y escritura.
#**********************************************************

ArchivoTexto=open("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PythonArchivos\\ArchivoPythonPrueba.txt", "r")

frase=""
frase=ArchivoTexto.read()

print(frase)

ArchivoTexto.seek(0)

frase=""
frase=ArchivoTexto.read()

print(frase)

ArchivoTexto.close()

#se pueden guardar y leer por lineas utilizando .readlines() o .writelines()
#el primero retorna una lista, y la ultima instruccion recibe una lista.

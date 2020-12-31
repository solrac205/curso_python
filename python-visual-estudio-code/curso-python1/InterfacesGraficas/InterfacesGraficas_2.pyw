# Librerias para trabajar interfaces de usuario 
# graficas (GUI):
# 1.- Tkinter
# 2.- WxPython
# 3.- PyQT
# 4.- PyGTK
# Si se trabaja en linux y no se tiene la 
# libreria se puede instalar con la siguiente instruccion:
# $sudo apt-get install python3-tk
# https://docs.python.org/3.3/library/tk.html

from tkinter import *

frmPruebaLabels=Tk()

frmPruebaLabels.title("Mi Primer Ventana Python")
frmPruebaLabels.iconbitmap("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\CheckOk.ico")
frmPruebaLabels.config(bg="lightblue")

frmePrbaLabels=Frame(frmPruebaLabels, width=600, height=400)
frmePrbaLabels.pack()
frmePrbaLabels.config(bg="steelblue")

lblLabel1=Label(frmePrbaLabels, text="Hola alumnos de Python")
lblLabel1.place(x=50, y=30)
lblLabel1.config(bg="steelblue")
lblLabel1.config(font=("Comic Sans MS", 18))

FileImage="C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\Keys.gif"
MiImagen=PhotoImage(file=FileImage)

lblLabel2=Label(frmePrbaLabels, image=MiImagen)
lblLabel2.place(x=50, y=100)

frmPruebaLabels.mainloop()

#aqui llegamos hasta el video No. 44 interfaces graficas III
#Toca el video No. 45 Interfaces graficas IV
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

raiz=Tk()
raiz.title("Mi Primer Ventana Python")
raiz.iconbitmap("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\CheckOk.ico")
#ambos parametros entrantes son boolean 0=False 1=True
raiz.resizable(False, False)
raiz.geometry("650x400")
raiz.config(bg="lightblue")

frmFrame=Frame()
frmFrame.pack(side="left", anchor="n", fill="both", expand="True")
frmFrame.config(bg="steelblue")
frmFrame.config(width=600, heigh=350) #definir el tamaño del frame.
frmFrame.config(bd=2) #grosor del borde del frame.
frmFrame.config(relief="groove") #definir el tipo de borde
frmFrame.config(cursor="pirate")

raiz.mainloop()


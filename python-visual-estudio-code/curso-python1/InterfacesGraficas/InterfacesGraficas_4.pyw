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
# Cuadro de texto clase Entry

from tkinter import *

frmTextAndButtons=Tk()

frmTextAndButtons.title("Mi Primer Ventana Python")
frmTextAndButtons.iconbitmap("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\CheckOk.ico")
frmTextAndButtons.config(bg="lightblue")

frmeEntrys = Frame(frmTextAndButtons, width=600, height=400, padx=10, pady=10)
frmeEntrys.pack()
frmeEntrys.config(bg="steelblue")

miNombre=StringVar()

lblLabel1=Label(frmeEntrys, text="Nombre: ")
#lblLabel1.place(x=10, y=90)
lblLabel1.grid(row=0, column=0, sticky="e", padx=3, pady=5)
lblLabel1.config(bg="steelblue")
lblLabel1.config(font=("Comic Sans MS", 12))


txtIngresoDato=Entry(frmeEntrys, textvariable=miNombre)
#txtIngresoDato.place(x=100,y=100)
txtIngresoDato.grid(row=0, column=1, padx=3, pady=5)
txtIngresoDato.config(fg="black", justify="center")


lblLabel2=Label(frmeEntrys, text="Apellido: ")
#lblLabel1.place(x=10, y=90)
lblLabel2.grid(row=1, column=0, sticky="e", padx=3, pady=5)
lblLabel2.config(bg="steelblue")
lblLabel2.config(font=("Comic Sans MS", 12))

txtIngresoDato2=Entry(frmeEntrys)
#txtIngresoDato.place(x=100,y=100)
txtIngresoDato2.grid(row=1, column=1, padx=3, pady=5)
txtIngresoDato2.config(fg="black", justify="center")

lblLabel3=Label(frmeEntrys, text="Dirección: ")
#lblLabel1.place(x=10, y=90)
lblLabel3.grid(row=2, column=0, sticky="e", padx=3, pady=5)
lblLabel3.config(bg="steelblue")
lblLabel3.config(font=("Comic Sans MS", 12))

txtIngresoDato3=Entry(frmeEntrys)
#txtIngresoDato.place(x=100,y=100)
txtIngresoDato3.grid(row=2, column=1, padx=3, pady=5)
txtIngresoDato3.config(fg="black", justify="center")

lblLabel4=Label(frmeEntrys, text="Password: ")
#lblLabel1.place(x=10, y=90)
lblLabel4.grid(row=3, column=0, sticky="e", padx=3, pady=5)
lblLabel4.config(bg="steelblue")
lblLabel4.config(font=("Comic Sans MS", 12))

txtIngresoDato4=Entry(frmeEntrys)
#txtIngresoDato.place(x=100,y=100)
txtIngresoDato4.grid(row=3, column=1, padx=3, pady=5)
txtIngresoDato4.config(fg="black", justify="center")
txtIngresoDato4.config(show="*")


lblLabel4=Label(frmeEntrys, text="Comentarios: ")
#lblLabel1.place(x=10, y=90)
lblLabel4.grid(row=4, column=0, sticky="e", padx=3, pady=5)
lblLabel4.config(bg="steelblue")
lblLabel4.config(font=("Comic Sans MS", 12))

txtXlComentarios = Text(frmeEntrys, width=16, height=5)
txtXlComentarios.grid(row=4, column=1, padx=3, pady=5)
txtXlComentarios.config(fg="black")

scrollVert=Scrollbar(frmeEntrys, command=txtXlComentarios.yview)
scrollVert.grid(row=4, column=2, sticky="nsew", padx=0, pady=5)
txtXlComentarios.config(yscrollcommand=scrollVert.set)

def fnCodigoButton():
    miNombre.set("Carlos")

btnEnvio=Button(frmTextAndButtons, text="Enviar", padx=0, pady=5, command=fnCodigoButton)
btnEnvio.pack()


frmTextAndButtons.mainloop()


#toca el video No. 47
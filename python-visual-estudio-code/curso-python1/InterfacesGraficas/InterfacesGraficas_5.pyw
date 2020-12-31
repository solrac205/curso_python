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

frmRadioButton = Tk()

frmRadioButton.title("Mi Prueba RadioButtons Python")
frmRadioButton.iconbitmap("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\CheckOk.ico")
frmRadioButton.config(bg="lightblue", width=400, height=250)

#****************************************************************************
# Definición del bloque de pantalla de la calculadora.
#****************************************************************************
frmeRadButton = Frame(frmRadioButton, width=130, height=230)
frmeRadButton.config(bg="steelblue")
frmeRadButton.place(x=10, y=10)

frmeCheckButton = Frame(frmRadioButton, width=160, height=230)
frmeCheckButton.config(bg="steelblue")
frmeCheckButton.place(x=150, y=10)

varOpRdBtn = IntVar()

lblLabel1=Label(frmeRadButton, text="Genero: ")
lblLabel1.place(x=30, y=5)
lblLabel1.config(bg="steelblue")
lblLabel1.config(font=("Comic Sans MS", 8))

def ClickRadButton():
    Seleccion=""
    if varOpRdBtn.get()==1:
        Seleccion="Masculino"
    else:
        Seleccion="Femenino"
    lblValorSeleccionado.config(text=Seleccion)

RdbtnSexo=[Radiobutton(frmeRadButton, text="Masculino", variable=varOpRdBtn, value=1, command=ClickRadButton)]
RdbtnSexo.append(Radiobutton(frmeRadButton, text="Femenino", variable=varOpRdBtn, value=2, command=ClickRadButton))
RdbtnSexo[0].place(x=30, y=30)
RdbtnSexo[1].place(x=30, y=50)

lblValorSeleccionado=Label(frmeRadButton)
lblValorSeleccionado.place(x=30, y=80)
lblValorSeleccionado.config(bg="steelblue")
lblValorSeleccionado.config(font=("Comic Sans MS", 12))

varOpRdBtn.set(1)
ClickRadButton()

Destinos=[IntVar(), IntVar(), IntVar()]

def ShowDestinos():
    OpcionesSeleccionadas=""
    i=0
    while i<=len(Destinos)-1:
        
        if Destinos[i].get()==1:
            if i==0:
                if len(OpcionesSeleccionadas)==0:
                    OpcionesSeleccionadas+="Playa"
                else:
                    OpcionesSeleccionadas+=",\nPlaya"
            elif i==1:
                if len(OpcionesSeleccionadas)==0:
                    OpcionesSeleccionadas+="Montaña"
                else:
                    OpcionesSeleccionadas+=",\nMontaña"
            elif i==2:
                if len(OpcionesSeleccionadas)==0:
                    OpcionesSeleccionadas+="Turismo Rural"
                else:
                    OpcionesSeleccionadas+=",\nTurismo Rural"
        i=i+1
    lblValSeleccionados.config(text=OpcionesSeleccionadas)

lblLabel2=Label(frmeCheckButton, text="Destinos: ")
lblLabel2.place(x=10, y=5)
lblLabel2.config(bg="steelblue")
lblLabel2.config(font=("Comic Sans MS", 8))

ChkBtnDestinos=[Checkbutton(frmeCheckButton, text="Playa", variable=Destinos[0], onvalue=1, offvalue=0, command=ShowDestinos),
                Checkbutton(frmeCheckButton, text="Montaña", variable=Destinos[1], onvalue=1, offvalue=0, command=ShowDestinos),
                Checkbutton(frmeCheckButton, text="Turismo Rural", variable=Destinos[2], onvalue=1, offvalue=0, command=ShowDestinos)]
ChkBtnDestinos[0].place(x=30, y=30)
ChkBtnDestinos[1].place(x=30, y=50)
ChkBtnDestinos[2].place(x=30, y=70)

lblValSeleccionados=Label(frmeCheckButton)
lblValSeleccionados.place(x=30, y=100)
lblValSeleccionados.config(bg="steelblue")
lblValSeleccionados.config(font=("Comic Sans MS", 12), justify="left")

FileImage="C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\Keys.gif"
MiImagen=PhotoImage(file=FileImage)

lblLabel3=Label(frmRadioButton, image=MiImagen, width=64, height=64)
lblLabel3.place(x=321, y=10)

frmRadioButton.mainloop()

#toca curso No.52

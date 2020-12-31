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

frmCalculadora = Tk()

frmCalculadora.title("Mi Calculadora Python")
frmCalculadora.iconbitmap("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\CheckOk.ico")
frmCalculadora.config(bg="lightblue", width=262, height=380)

#****************************************************************************
# Definición del bloque de pantalla de la calculadora.
#****************************************************************************
frmeCalc1 = Frame(frmCalculadora, width=500, height=50)
frmeCalc1.config(bg="steelblue")
frmeCalc1.place(x=10, y=5)

NumeroPantalla=StringVar()

Valor1=0.00
Valor2=0.00
Valor3=0.00
Op=""


EtryPantalla = Entry(frmeCalc1, width=26, textvariable=NumeroPantalla)
EtryPantalla.grid(row=1, column=1, padx=2, pady=5)
EtryPantalla.config(background="black", fg="#03f943", justify="right")
EtryPantalla.config(font=("Comic Sans MS", 11, "bold"))
EtryPantalla.config(state="disable", disabledbackground="black", disabledforeground="#03f943")
# Se puede utilizar la instrucción columnspan=x 
# dentro del procedimiento grid para hacer
# un merge de columnas.

#--------------- Pulsaciones del teclado -----------------
def BorrarOperatoria():
    NumeroPantalla.set("")
    global Valor1
    global Valor2
    global Valor3
    global Op

    Valor1=0.00
    Valor2=0.00
    Valor3=0.00
    Op=""

def Divide():
    global Valor1
    global Valor2
    global Valor3
    global Op

    if Op!="":
        if Op=="/":
            Valor1=Valor1/float(NumeroPantalla.get())
        elif Op=="+":
            Valor1=Valor1+float(NumeroPantalla.get())
        elif Op=="-":
            Valor1=Valor1-float(NumeroPantalla.get())
        elif Op=="X":
            Valor1=Valor1*float(NumeroPantalla.get())

        Op="/"
    else:
        Op="/"
        Valor1=float(NumeroPantalla.get())

    NumeroPantalla.set("")

def Suma():
    global Valor1
    global Valor2
    global Valor3
    global Op

    if Op!="":
        if Op=="+":
            Valor1=Valor1+float(NumeroPantalla.get())
        elif Op=="-":
            Valor1=Valor1-float(NumeroPantalla.get())
        elif Op=="X":
            Valor1=Valor1*float(NumeroPantalla.get())
        elif Op=="/":
            Valor1=Valor1/float(NumeroPantalla.get())

        Op="+"

    else:
        Op="+"
        Valor1=float(NumeroPantalla.get())

    NumeroPantalla.set("")

def Resta():
    global Valor1
    global Valor2
    global Valor3
    global Op

    if Op!="":
        if Op=="-":
            Valor1=Valor1-float(NumeroPantalla.get())
        elif Op=="X":
            Valor1=Valor1*float(NumeroPantalla.get())
        elif Op=="+":
            Valor1=Valor1+float(NumeroPantalla.get())
        elif Op=="/":
            Valor1=Valor1/float(NumeroPantalla.get())

        Op="-"
    else:
        Op="-"
        Valor1=float(NumeroPantalla.get())

    NumeroPantalla.set("")

def Multipli():
    global Valor1
    global Valor2
    global Valor3
    global Op

    if Op!="":
        if Op=="X":
            Valor1=Valor1*float(NumeroPantalla.get())
        elif Op=="+":
            Valor1=Valor1+float(NumeroPantalla.get())
        elif Op=="-":
            Valor1=Valor1-float(NumeroPantalla.get())
        elif Op=="/":
            Valor1=Valor1/float(NumeroPantalla.get())

        Op="X"
    else:
        Op="X"
        Valor1=float(NumeroPantalla.get())

    NumeroPantalla.set("")

def Igual():
    global Valor1
    global Valor2
    global Valor3
    global Op

    if Op=="X":
        
        Valor2=float(NumeroPantalla.get())
        Valor3= Valor1 * Valor2
    
    elif Op=="-":
        Valor2=float(NumeroPantalla.get())
        Valor3= Valor1 - Valor2
    
    elif Op=="+":
        Valor2=float(NumeroPantalla.get())
        Valor3= Valor1 + Valor2
    elif Op=="/":
        Valor2=float(NumeroPantalla.get())
        Valor3= Valor1 / Valor2

    NumeroPantalla.set(str(Valor3))
    Valor1=0.00
    Valor2=0.00
    Valor3=0.00
    Op=""

def NumeroPulsado(PressNum):

    if PressNum in("0","1","2","3","4","5","6","7","8","9","."):

        calculo=""
        calculo=NumeroPantalla.get()

        if PressNum == ".":
            
            if ("." in calculo):
                calculo = calculo
            else:
                calculo=calculo + PressNum
        else:
            if calculo=="0" and PressNum=="0":
                calculo="0"
            else:
                if len(calculo)==0:
                    calculo=""
                elif len(calculo)>=1:
                    if ((calculo[0]=="0") and (PressNum != ".") and ("." not in calculo)):
                        calculo=calculo[1:(len(calculo)-1)]

                calculo=calculo + PressNum

        NumeroPantalla.set(calculo)
    else:
        if PressNum=="AC":
            BorrarOperatoria()
        elif PressNum=="X":
            Multipli()
        elif PressNum=="-":
            Resta()
        elif PressNum=="+":
            Suma()
        elif PressNum=="/":
            Divide()
        elif PressNum=="=":
            Igual()



#****************************************************************************
# Definición del bloque de teclado de la calculadora.
#****************************************************************************
frmeCalc2 = Frame(frmCalculadora, width=500, height=150)
frmeCalc2.config(bg="steelblue")
frmeCalc2.place(x=10,y=45)
#****************************************************************************
# Primera fila de botones.
#****************************************************************************
btnNumero7=Button(frmeCalc2, text="7", padx=10, pady=5, command=lambda:NumeroPulsado("7"))
btnNumero7.grid(row=0, column=0, padx=5, pady=5)
btnNumero7.config(font=("Comic Sans MS", 14, "bold"))
btnNumero7.config(bg="lightgray")

btnNumero8=Button(frmeCalc2, text="8", padx=10, pady=5, command=lambda:NumeroPulsado("8"))
btnNumero8.grid(row=0, column=1, padx=5, pady=5)
btnNumero8.config(font=("Comic Sans MS", 14, "bold"))
btnNumero8.config(bg="lightgray")

btnNumero9=Button(frmeCalc2, text="9", padx=10, pady=5, command=lambda:NumeroPulsado("9"))
btnNumero9.grid(row=0, column=2, padx=5, pady=5)
btnNumero9.config(font=("Comic Sans MS", 14, "bold"))
btnNumero9.config(bg="lightgray")

btnOp_Multiplica=Button(frmeCalc2, text="X", padx=10, pady=5, command=lambda:NumeroPulsado("X"))
btnOp_Multiplica.grid(row=0, column=3, padx=5, pady=5)
btnOp_Multiplica.config(font=("Comic Sans MS", 14, "bold"))
btnOp_Multiplica.config(bg="darkgray")

#****************************************************************************
# Segunda fila de botones.
#****************************************************************************
btnNumero4=Button(frmeCalc2, text="4", padx=10, pady=5, command=lambda:NumeroPulsado("4"))
btnNumero4.grid(row=1, column=0, padx=5, pady=5)
btnNumero4.config(font=("Comic Sans MS", 14, "bold"))
btnNumero4.config(bg="lightgray")

btnNumero5=Button(frmeCalc2, text="5", padx=10, pady=5, command=lambda:NumeroPulsado("5"))
btnNumero5.grid(row=1, column=1, padx=5, pady=5)
btnNumero5.config(font=("Comic Sans MS", 14, "bold"))
btnNumero5.config(bg="lightgray")

btnNumero6=Button(frmeCalc2, text="6", padx=10, pady=5, command=lambda:NumeroPulsado("6"))
btnNumero6.grid(row=1, column=2, padx=5, pady=5)
btnNumero6.config(font=("Comic Sans MS", 14, "bold"))
btnNumero6.config(bg="lightgray")

btnOp_Resta=Button(frmeCalc2, text="-", padx=10, pady=5, command=lambda:NumeroPulsado("-"))
btnOp_Resta.grid(row=1, column=3, padx=5, pady=5)
btnOp_Resta.config(font=("Comic Sans MS", 14, "bold"))
btnOp_Resta.config(bg="darkgray")

#****************************************************************************
# Tercera fila de botones.
#****************************************************************************
btnNumero1=Button(frmeCalc2, text="1", padx=10, pady=5, command=lambda:NumeroPulsado("1"))
btnNumero1.grid(row=2, column=0, padx=5, pady=5)
btnNumero1.config(font=("Comic Sans MS", 14, "bold"))
btnNumero1.config(bg="lightgray")

btnNumero2=Button(frmeCalc2, text="2", padx=10, pady=5, command=lambda:NumeroPulsado("2"))
btnNumero2.grid(row=2, column=1, padx=5, pady=5)
btnNumero2.config(font=("Comic Sans MS", 14, "bold"))
btnNumero2.config(bg="lightgray")

btnNumero3=Button(frmeCalc2, text="3", padx=10, pady=5, command=lambda:NumeroPulsado("3"))
btnNumero3.grid(row=2, column=2, padx=5, pady=5)
btnNumero3.config(font=("Comic Sans MS", 14, "bold"))
btnNumero3.config(bg="lightgray")

btnOp_Suma=Button(frmeCalc2, text="+", padx=10, pady=5, command=lambda:NumeroPulsado("+"))
btnOp_Suma.grid(row=2, column=3, padx=5, pady=5)
btnOp_Suma.config(font=("Comic Sans MS", 14, "bold"))
btnOp_Suma.config(bg="darkgray")

#****************************************************************************
# Cuarta fila de botones.
#****************************************************************************
btnOp_AC=Button(frmeCalc2, text="AC", padx=5, pady=5, command=lambda:NumeroPulsado("AC"))
btnOp_AC.grid(row=3, column=0, padx=5, pady=5)
btnOp_AC.config(font=("Comic Sans MS", 14, "bold"))
btnOp_AC.config(bg="white")

btnNumero0=Button(frmeCalc2, text="0", padx=10, pady=5, command=lambda:NumeroPulsado("0"))
btnNumero0.grid(row=3, column=1, padx=5, pady=5)
btnNumero0.config(font=("Comic Sans MS", 14, "bold"))
btnNumero0.config(bg="lightgray")

btnSepDec=Button(frmeCalc2, text=".", padx=10, pady=5, command=lambda:NumeroPulsado("."))
btnSepDec.grid(row=3, column=2, padx=5, pady=5)
btnSepDec.config(font=("Comic Sans MS", 14, "bold"))
btnSepDec.config(bg="lightgray")

btnOp_div=Button(frmeCalc2, text="/", padx=10, pady=5, command=lambda:NumeroPulsado("/"))
btnOp_div.grid(row=3, column=3, padx=5, pady=5)
btnOp_div.config(font=("Comic Sans MS", 14, "bold"))
btnOp_div.config(bg="darkgray")

#****************************************************************************
# Quinta fila de botones.
#****************************************************************************

btnOp_Igual=Button(frmeCalc2, text="=", width=17, padx=10, pady=5, command=lambda:NumeroPulsado("="))
btnOp_Igual.grid(row=4, column=0, padx=5, pady=5, columnspan=4)
btnOp_Igual.config(font=("Comic Sans MS", 14, "bold"))
btnOp_Igual.config(bg="darkgray")
#****************************************************************************


frmCalculadora.mainloop()

#Toca el video No. 50
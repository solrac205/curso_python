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
from tkinter import messagebox
from tkinter import filedialog

def VentanaEmergente():
    messagebox.showinfo("Procesador Carlos", "Programa de pruebas de menus 2020")

def AvisoLicencia():
    messagebox.showwarning("Licencia...","Proyecto bajo lic. GNU 2020")

def SalirApp():
    ValorSalir=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if ValorSalir=="yes":
        frmMenus.destroy()

def CerrarDoc():
    ValorCerrar=messagebox.askretrycancel("Reintentar","No es posible cerrar el documento, Documento Bloqueado")
    if ValorCerrar==False:
        frmMenus.destroy()

def CommondDialog():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:\\", 
                                       filetypes=(("Ficheros de Bitacora","*.log"),
                                                  ("Ficheros de Texto","*.txt"),
                                                  ("Todos los Ficheros","*.*")))
    messagebox.showinfo("Archivo Seleccionado...",fichero)




frmMenus = Tk()

frmMenus.title("Mi Prueba Menús Python")
frmMenus.iconbitmap("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\InterfacesGraficas\\CheckOk.ico")
frmMenus.config(bg="lightblue", width=400, height=250)

#********************************************************************************
mnuBarraDeMenu=Menu(frmMenus)
frmMenus.config(menu=mnuBarraDeMenu)
#********************************************************************************

mnuFileMenu=Menu(mnuBarraDeMenu, tearoff=0)
mnuFileMenu.add_command(label="Nuevo", command=CommondDialog)
mnuFileMenu.add_command(label="Guardar")
mnuFileMenu.add_command(label="Guardar Como")
mnuFileMenu.add_separator()
mnuFileMenu.add_command(label="Cerrar", command=CerrarDoc)
mnuFileMenu.add_command(label="Salir", command=SalirApp)

mnuEditMenu=Menu(mnuBarraDeMenu, tearoff=0)
mnuEditMenu.add_command(label="Copiar")
mnuEditMenu.add_command(label="Cortar")
mnuEditMenu.add_command(label="Pegar")

mnuToolsMenu=Menu(mnuBarraDeMenu, tearoff=0)

mnuHelpMenu=Menu(mnuBarraDeMenu, tearoff=0)
mnuHelpMenu.add_command(label="Licencia", command=AvisoLicencia)
mnuHelpMenu.add_command(label="Acerca de...", command=VentanaEmergente)

mnuBarraDeMenu.add_cascade(label="Archivo", menu=mnuFileMenu)
mnuBarraDeMenu.add_cascade(label="Edición", menu=mnuEditMenu)
mnuBarraDeMenu.add_cascade(label="Herramientas", menu=mnuToolsMenu)
mnuBarraDeMenu.add_cascade(label="Ayuda", menu=mnuHelpMenu)



frmMenus.mainloop()


#Toca video No. 55
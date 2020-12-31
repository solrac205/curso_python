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
from DBProccess import AppDB

#********************************************************************************

BaseApp=AppDB("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PracticaGuiadaCursoPython\\AppDB.db")

#********************************************************************************
def VentanaEmergente():
    messagebox.showinfo("Procesador Carlos", "Programa de pruebas de menus 2020")

def AvisoLicencia():
    messagebox.showwarning("Licencia...","Proyecto bajo lic. GNU 2020")

def SalirApp():
    ValorSalir=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if ValorSalir=="yes":
        global BaseApp
        ResultClose=""
        ResultClose=BaseApp.CloseDB()
        if ResultClose!="":
            messagebox.showerror("Error Cerrando Base de Datos",ResultClose)
        frmMenus.destroy()

def ConectarBase():
    global BaseApp
    ResultOpenDB=""
    ResultOpenDB=BaseApp.OpenDB()
    if ResultOpenDB!="":
        messagebox.showerror("Error Abriendo base de datos",ResultOpenDB)
    else:
        messagebox.showinfo(BaseApp.Estado,"La base de Datos ha sido Abierta")

def InitDB():
    global BaseApp
    try:
        QuerySQLite='''
                CREATE TABLE DATOSUSUARIOS(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE_USUARIO VARCHAR(50) UNIQUE,
                    PASSWORD VARCHAR(50),
                    APELLIDO VARCHAR(50),
                    DIRECCION VARCHAR(80),
                    COMENTARIOS VARCHAR(100)
                );
        '''
        QuerySQLite2='''
                DROP TABLE DATOSUSUARIOS;
        '''        
        QueryResult=BaseApp.ExecQuery(QuerySQLite)

        if QueryResult !="":
            QueryResult=BaseApp.ExecQuery(QuerySQLite2)
            if QueryResult != "":
                messagebox.showerror("Error DB", QueryResult)
            else:
                QueryResult=BaseApp.ExecQuery(QuerySQLite)
                if QueryResult != "":
                    messagebox.showerror("Error DB", QueryResult)
    except:
        messagebox.showerror("Error en Base de Datos","Error localizado al inicializar base de datos.")
    finally:
        messagebox.showinfo("SQL ejecutado.","Inicialización correcta...")

#********************************************************************************

frmMenus = Tk()

frmMenus.title("Mi Prueba Menús Python")
frmMenus.iconbitmap("C:\\Desarrollo\\Python\\python-visual-estudio-code\\curso-python1\\PracticaGuiadaCursoPython\\CheckOk.ico")
frmMenus.config(bg="lightblue", width=400, height=400)

#********************************************************************************
mnuBarraDeMenu=Menu(frmMenus)
frmMenus.config(menu=mnuBarraDeMenu)
#********************************************************************************

mnuFileMenu=Menu(mnuBarraDeMenu, tearoff=0)
mnuFileMenu.add_command(label="Conectar a Base de Datos", command=ConectarBase)
mnuFileMenu.add_command(label="Inicializar Base de Datos", command=InitDB)
mnuFileMenu.add_separator()
mnuFileMenu.add_command(label="Salir", command=SalirApp)


mnuEditMenu=Menu(mnuBarraDeMenu, tearoff=0)

mnuToolsMenu=Menu(mnuBarraDeMenu, tearoff=0)

mnuHelpMenu=Menu(mnuBarraDeMenu, tearoff=0)
mnuHelpMenu.add_command(label="Licencia", command=AvisoLicencia)
mnuHelpMenu.add_command(label="Acerca de...", command=VentanaEmergente)

mnuBarraDeMenu.add_cascade(label="BBDD", menu=mnuFileMenu)
mnuBarraDeMenu.add_cascade(label="Edición", menu=mnuEditMenu)
mnuBarraDeMenu.add_cascade(label="Herramientas", menu=mnuToolsMenu)
mnuBarraDeMenu.add_cascade(label="Ayuda", menu=mnuHelpMenu)
#********************************************************************************
frmeIngresos = Frame(frmMenus, width=380, height=275)
frmeIngresos.config(bg="steelblue")
frmeIngresos.place(x=10,y=10)

frmeCampos = Frame(frmeIngresos, width=380, height=275)
frmeCampos.config(bg="steelblue")
frmeCampos.place(x=10,y=10)
#********************************************************************************
lblLabel1=Label(frmeCampos, width=10, height=1, text="Id: ")
lblLabel1.grid(row=0, column=0, sticky="e", padx=3, pady=5)
lblLabel1.config(bg="steelblue", justify="left")
lblLabel1.config(font=("Comic Sans MS", 12))

Vr_Id = StringVar()

txtIngresoDato=Entry(frmeCampos, width=30, textvariable=Vr_Id)
txtIngresoDato.grid(row=0, column=1, padx=3, pady=5)
txtIngresoDato.config(fg="black", justify="center")
#********************************************************************************

lblLabel2=Label(frmeCampos, width=10, height=1, text="Nombre: ")
lblLabel2.grid(row=1, column=0, sticky="e", padx=3, pady=5)
lblLabel2.config(bg="steelblue", justify="left")
lblLabel2.config(font=("Comic Sans MS", 12))

Vr_Nombre = StringVar()

txtIngresoDato2=Entry(frmeCampos, width=30, textvariable=Vr_Nombre)
txtIngresoDato2.grid(row=1, column=1, padx=3, pady=5)
txtIngresoDato2.config(fg="black", justify="center")

#********************************************************************************

lblLabel3=Label(frmeCampos, width=10, height=1, text="Password: ")
lblLabel3.grid(row=2, column=0, sticky="e", padx=3, pady=5)
lblLabel3.config(bg="steelblue", justify="left")
lblLabel3.config(font=("Comic Sans MS", 12))

Vr_Password = StringVar()

txtIngresoDato3=Entry(frmeCampos, width=30, textvariable=Vr_Password)
txtIngresoDato3.grid(row=2, column=1, padx=3, pady=5)
txtIngresoDato3.config(fg="black", justify="center")
txtIngresoDato3.config(show="*")


#********************************************************************************
frmeButtons = Frame(frmMenus, width=380, height=80)
frmeButtons.config(bg="steelblue")
frmeButtons.place(x=10,y=290)
#********************************************************************************




frmMenus.mainloop()

#24-01-2020 Siguiente video: No.60
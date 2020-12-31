print("******************************************************")
print("Curso No. 24,25,26,27,28... POO" ) 
print("******************************************************")

#Sintaxis de declaracion de clases.
class Coche():
    #asignación de valores a propiedades sin usar un constructor.
    #LargoChasis=250
    #AnchoChasis=120
    #Ruedas=4
    #EnMarcha=False

    #Para crear un constructor de la clase se crea de la siguiente forma.
    def __init__ (self):
        self.LargoChasis=250
        self.AnchoChasis=120
        #Para proceder con el encapsulamiento de una propiedad o proteger su valor se utiliza "__" para preceder al nombre de la propiedad
        self.__Ruedas=4
        self.__EnMarcha=False

    def arrancar(self,Arrancamos):
        self.__EnMarcha=Arrancamos
        chequeo=False
        
        if(self.__EnMarcha):
            chequeo=self.__Chequeo_Interno()

        if(self.__EnMarcha and chequeo):
            return "El coche está Arrancado"
        elif(self.__EnMarcha and chequeo==False):
            return "Algo a salido mal al arrancar, no se puede arrancar"
        else:
            return "El coche está Detenido"

    def estado(self):
        print("El coche tiene ", self.__Ruedas, " Ruedas. un ancho de ", self.AnchoChasis, " y un largo de ", self.LargoChasis)

    #tambien es posible encapsular procedimiento.
    def __Chequeo_Interno(self):
        print("Realizando Chequeo Interno...")
        self.Gasolina="ok"
        self.Aceite="ok"
        self.Puertas="Cerradas"
        if(self.Gasolina=="ok" and self.Aceite=="ok" and self.Puertas=="Cerradas"):
            return True
        else:
            return False
            

#para instanciar un objeto de la clase coche....
miCoche=Coche()

#print("El largo del coche es: ", miCoche.LargoChasis)
#print("El coche tiene ", miCoche.Ruedas, " Ruedas")

print(miCoche.arrancar(True))

miCoche.estado()

print("********** a Continuación se crea un segundo objeto *********")

miCoche2=Coche()

#print("El largo del coche es: ", miCoche2.LargoChasis)
#print("El coche tiene ", miCoche2.Ruedas, " Ruedas")

print(miCoche2.arrancar(False))

miCoche2.estado()

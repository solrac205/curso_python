print("******************************************************")
print("Curso No. 24,25,26,27... POO" ) 
print("******************************************************")

#Sintaxis de declaracion de clases.
class Coche():
    LargoChasis=250
    AnchoChasis=120
    Ruedas=4
    EnMarcha=False

    def arrancar(self,Arrancamos):
        self.EnMarcha=Arrancamos
        if(self.EnMarcha):
            return "El coche está Arrancado"
        else:
            return "El coche está Detenido"

    def estado(self):
        print("El coche tiene ", self.Ruedas, " Ruedas. un ancho de ", self.AnchoChasis, " y un largo de ", self.LargoChasis)

#para instanciar un objeto de la clase coche....
miCoche=Coche()

print("El largo del coche es: ", miCoche.LargoChasis)
print("El coche tiene ", miCoche.Ruedas, " Ruedas")

print(miCoche.arrancar(True))

miCoche.estado()

print("********** a Continuación se crea un segundo objeto *********")

miCoche2=Coche()

print("El largo del coche es: ", miCoche2.LargoChasis)
print("El coche tiene ", miCoche2.Ruedas, " Ruedas")

print(miCoche2.arrancar(False))

miCoche2.estado()

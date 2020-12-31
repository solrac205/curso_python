print("******************************************************")
print("Curso No. 29 ... POO Herencia." ) 
print("******************************************************")

class Vehiculos():
    def __init__(self, Marca, Modelo):
        self.Marca=Marca
        self.Modelo=Modelo
        self.EnMarcha=False
        self.Acelera=False
        self.Frena=False

    def Arrancar(self):
        self.EnMarcha=True

    def Acelerar(self):
        self.Acelera=True

    def Frenar(self):
        self.Frena=True

    def Estado(self):
        print("Marca: ", self.Marca, 
              "\nModelo: ", self.Modelo,
              "\nEn Marcha: ", self.EnMarcha, 
              "\nAcelerando: ", self.Acelera,
              "\nFrenando: ", self.Frena )

class Moto(Vehiculos):
    pass

print("")
print("Prueba de Objeto aplicando objeto padre.")
print("********************************************************")
print("")

Generales=Vehiculos("Chevrolet","2011")
Generales.Estado()

print("")
print("Prueba de Objeto aplicando la Herencia del objeto padre.")
print("********************************************************")
print("")

MiMoto=Moto("Honda","2019")
MiMoto.Estado()
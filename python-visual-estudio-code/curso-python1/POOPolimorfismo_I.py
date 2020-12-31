print("******************************************************")
print("Curso No. 32 ... POO Polimorfismo." ) 
print("******************************************************")

class Coche():

    def Desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas...")

class Moto():

    def Desplazamiento(self):
        print("Me desplazo utilizando dos ruedas...")

class Camion():

    def Desplazamiento(self):
        print("Me desplazo utilizando seis ruedas...")

print("---------------Coche--------------------------")
miCoche=Coche()
miCoche.Desplazamiento()

print("---------------Moto---------------------------")
miMoto=Moto()
miMoto.Desplazamiento()

print("---------------Camion-------------------------")
miCamion=Camion()
miCamion.Desplazamiento()
print("----------------------------------------------")

def DesplazamientoVehiculo(Vehiculo):
    Vehiculo.Desplazamiento()

print("")
print("Utilizando una funcion polimorfica")
print("---------------Coche--------------------------")
DesplazamientoVehiculo(miCoche)
print("---------------Moto---------------------------")
DesplazamientoVehiculo(miMoto)
print("---------------Camion-------------------------")
DesplazamientoVehiculo(miCamion)
print("----------------------------------------------")

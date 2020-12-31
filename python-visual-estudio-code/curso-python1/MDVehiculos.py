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
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito..."

    def Estado(self):
        print("Marca: ", self.Marca, 
              "\nModelo: ", self.Modelo,
              "\nEn Marcha: ", self.EnMarcha, 
              "\nAcelerando: ", self.Acelera,
              "\nFrenando: ", self.Frena,
              "\n", self.hcaballito )

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class VElectricos(Vehiculos):
    def __init__(self, Marca, Modelo):
        super().__init__(Marca, Modelo)
        self.autonomia=100

    def CargarEnergia(self):
        self.cargando=True

class BicicletaElectrica(VElectricos, Vehiculos):
    pass


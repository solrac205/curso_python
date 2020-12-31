print("******************************************************")
print("Curso No. 24,25,26,27... POO" ) 
print("******************************************************")

#Sintaxis de declaracion de clases.
class Coche():
	LargoChasis=250
	AnchoChasis=120
	Ruedas=4
	EnMarcha=False

	#declaracion de un metodo
	#Caracteristicas
	def Arrancar(self):
		#pass
		self.EnMarcha = True

	def estado(self):
		if(self.EnMarcha):
			return "El coche esta arrancado"
		else:
			return "El coche esta detenido"

#para instanciar un objeto de la clase coche....
miCoche= Coche()

print("El largo del coche es: ", miCoche.LargoChasis)
print("El coche tiene:", miCoche.Ruedas, " Ruedas")
miCoche.Arrancar()

print("El coche esta en marcha?", miCoche.estado())

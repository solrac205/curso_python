print("******************************************************")
print("Curso No. 31 ... POO Herencia." ) 
print("******************************************************")

class Persona():

    def __init__(self, Nombre, Edad, Lugar_Residencia):
        self.nombre=Nombre
        self.edad=Edad
        self.LugarResidencia=Lugar_Residencia

    def Descripcion(self):
        print("Nombre: ", self.nombre, 
              "\nEdad: ", self.edad, 
              "\nResidencia: ", self.LugarResidencia)

class Empleado(Persona):
    def __init__(self, Salario, Antiguedad, Nombre, Edad, Residencia):
        super().__init__(Nombre, Edad, Residencia)
        self.salario=Salario
        self.antiguedad=Antiguedad

    def Descripcion(self):
        print("Nombre: ", self.nombre, 
              "\nEdad: ", self.edad, 
              "\nResidencia: ", self.LugarResidencia,
              "\nSalario: ", self.salario,
              "\nAntiguedad: ", self.antiguedad)

Antonio=Persona("Antonio", 55, "España")

Antonio.Descripcion()
print(isinstance(Antonio,Empleado))

print("******************************************************")
print("Construyendo Herencia activando ambos constructores...")
print("******************************************************")
OtroEmpleado=Empleado(5000, 15, "Antonio", 55, "España")

OtroEmpleado.Descripcion()

print(isinstance(OtroEmpleado,Persona))
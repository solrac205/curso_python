def Mensaje():

	print("Estamos Aprendiendo Python")
	print("Estamos Aprendiendo lo Basico")
	print("poco a poco...")

Mensaje()


def Suma(Num1, Num2):
	return (Num1 + Num2)

Resultado=Suma(5, 9)

print(Resultado)
print(Suma(4,6))


MiListaDeDatos=["prueba1","Prueba2","Prueba3","Prueba4","Prueba5"]

#Imprimir todos los datos de la lista.
print(MiListaDeDatos[:])
#Imprimir el dato 3 de la lista
#las listas inician en indice 0,1,2,..N
print(MiListaDeDatos[3])
#Es posible recorrer dinamicamente en reversa
print(MiListaDeDatos[-4])
#Es posible recorrer dinamicamente en rangos
print(MiListaDeDatos[1:4])
#Es posible que los rangos sean abiertos
print(MiListaDeDatos[2:])

#se pueden agregar elementos
MiListaDeDatos.append("Prueba6")
print(MiListaDeDatos[:])
#se pueden agregar elementos en posiciones intermedias.
MiListaDeDatos.insert(2,"prueba3.5")
print(MiListaDeDatos[:])
#Agregar varios datos a la vez
MiListaDeDatos.extend(["prueba7","prueba8"])
print(MiListaDeDatos[:])

print(MiListaDeDatos.index("Prueba3"))

#Las listas pueden contener valores de diferentes tipos
MiListaDeDatos.extend([7,True])
print(MiListaDeDatos[:])

#se pueden eliminar elementos
MiListaDeDatos.remove(True)
#se puede eliminar el ultimo elemento
MiListaDeDatos.pop()
print(MiListaDeDatos[:])

#se pueden sumar listas tambien solo con el operador +
lista1=["hola"]
lista2=["esta","es","prueba"]
lista3=lista1 + lista2
print(lista3[:])
lista4 = lista3 * 2
print(lista4[:])

TuplaPrueba=("Valores","de","prueba",10, 1995)
print(TuplaPrueba[:])
TuplaALista=list(TuplaPrueba)
print(TuplaALista[:])
TuplaPrueba=tuple(TuplaALista)
print(TuplaPrueba[:])

TuplaPrueba=("Valores","de","prueba",10, 1995,10)
print(TuplaPrueba)
print(TuplaPrueba.count(10))

print(len(TuplaPrueba))


tuplaFecha=("Guatemala","09","Noviembre","2019")
pais, dia, mes, agno=tuplaFecha
print(pais,dia,mes,agno)
print(pais)
print(agno)
print(mes)
print(dia)

#********************************************
#manejo de diccionarios en python
#********************************************

MiDiccionario={"Guatemala":"Ciudad Guatemala","Alemania":"Berlin",
               "Francia":"Paris","España":"Madrid"}

print(MiDiccionario)
print(MiDiccionario["Alemania"])               

MiDiccionario["Italia"]="Lisboa"
print(MiDiccionario)

MiDiccionario["Italia"]="Roma"
print(MiDiccionario)

del MiDiccionario["Italia"]
print(MiDiccionario)


mitupla=["Guatemala","Alemania","España"]
diccionarioDinamico={mitupla[0]:"Ciudad Guatemala",
                     mitupla[1]:"Berlin",
                     mitupla[2]:"Madrid"}
print(diccionarioDinamico)


DiccionarioComplejo={23:"Jordan", "Nombre":"Michael",
                     "Equipo":"Chicago", "Anillos":["2019","2018","2017"]}
print(DiccionarioComplejo)                     
print(DiccionarioComplejo["Anillos"])

DiccionarioComplejo={23:"Jordan", "Nombre":"Michael",
                     "Equipo":"Chicago", "Anillos":{"temporadas":["2019","2018","2017"]}}

print(DiccionarioComplejo)                     
print(DiccionarioComplejo["Anillos"])
print(DiccionarioComplejo.keys())
print(DiccionarioComplejo.values())
print(len(DiccionarioComplejo))

#ultimo curso visto a este punto 
#es el curso 9, curso que toca es el 10
#sentencias de condicionamientos cap. 10

# > mayor que
# > menor que
# == igual a
# >= mayor o igual
# <= menor o igual
# != diferente a 
def Evaluacion(nota):
	valoracion="Aprobado"
	if nota < 5:
		valoracion="reprobado"
	return valoracion

print(Evaluacion(3))
print(Evaluacion(10))


print("Programa de Evaluacion de notas de alumnos")


Nota_Evaluar = 4 #int(input("Ingrese nota de alumno a evaluar."))
print(Evaluacion(Nota_Evaluar))



#Es posible utilizar Else y Elif curso 11
print("******************************************************")
print("Curso No. 11")
print("******************************************************")
EdadUsuario=19

if EdadUsuario < 18:
	print("no puedes pasar")
elif EdadUsuario >100:
    print("Edad incorrecta...")	
else:
	print("puedes pasar")

#toca curso 12

#python permite utilizar operadores concatenados
print("******************************************************")
print("Curso No. 12")
print("******************************************************")

Curso12Edad=-7

if 0<Curso12Edad<100:
	print("Edad es Correcta...")
else:
	print("Edad es incorrecta...")
	
print("******************************************************")
print("Segunda prueba")
print("******************************************************")

Salario_Presidente=5000 #int(input("Introduce salario del presidente: "))
print("Salario presidente: " + str(Salario_Presidente) )

Salario_Director=4000 #int(input("Introduce salario del director: "))
print("Salario director: " + str(Salario_Director) )


Salario_JefeArea=3500   #int(input("Introduce salario del Jefe de área: "))
print("Salario Jefe de área: " + str(Salario_JefeArea) )


Salario_Administrativo= 2500  #int(input("Introduce salario del Administrativo: "))
print("Salario del Administrativo: " + str(Salario_Administrativo) )

if Salario_Administrativo<Salario_JefeArea<Salario_Director<Salario_Presidente:
	print("Todo Funciona Correctamente...")
else:
	print("Algo falla en la asignación salarial de esta empresa")


print("******************************************************")
print("Curso No. 13 operadores and y or " ) 
print("******************************************************")

print("Programa de becas año 2019")
Distancia_Escuela=50  #int(input("Introduce la distancia a la escuela en km: "))
print(Distancia_Escuela)

Numero_Hermanos=3    #int(input("Introduce el No. de Hermanos en el centro: "))
print(Numero_Hermanos)

Salario_Familiar=10000 #float(input("Introduce el Salario Familiar "))
print(Salario_Familiar)

if Distancia_Escuela > 40 and Numero_Hermanos>2 and Salario_Familiar<=20500.50:
	print("Tiene derecho a beca...")
else:
	print("No tiene derecho a beca...")

if Distancia_Escuela > 40 and Numero_Hermanos>2 or Salario_Familiar<=20500.50:
	print("Tiene derecho a beca...")
else:
	print("No tiene derecho a beca...")

print("******************************************************")
Asignaturas={"01":"Informatica Grafica","02":"Pruebas de Software","03":"Usabilidad y Accesibilidad"}

print("Asignaturas optativas año 2019")
print("Asignaturas Optativas: ")
print("01 - Informatica Grafica, 02 - Pruebas de Software, 03 - Usabilidad y Accesibilidad")

seleccion=input("Digite el número elegido: ")

if seleccion in (Asignaturas.keys()):
	print("Seleccion correcta")
else:
	print("La seleccion es erronea")


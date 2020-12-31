print("******************************************************")
print("Curso No. 19 Generadores" ) 
print("******************************************************")

#los generadores generan varios valores de forma de un cursor, es decir 
#generan de uno en uno los valores de la funcion, por ejemplo una lista de numeros
#es generada de uno en uno con forme se llama la funcion sin perder la historia
#de lo que ya generó

def generapares(limite):
	num=1
	while num < limite:
		yield num * 2

		num=num+1

devuelvepares=generapares(10)

print(next(devuelvepares))

print("aqui puede haber mas procesamiento...")

print(next(devuelvepares))

print("aqui puede haber mas procesamiento...")

print(next(devuelvepares))

print("aqui puede haber mas procesamiento...")

print(next(devuelvepares))

print("******************************************************")
print("Curso No. 20 Generadores" ) 
print("******************************************************")

def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		#for subelemento in elemento:
		#	yield subelemento
		yield from elemento

ciudades_dev=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")		

print(next(ciudades_dev))

print(next(ciudades_dev))
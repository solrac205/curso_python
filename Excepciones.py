print("******************************************************")
print("Curso No. 21 Excepciones" ) 
print("******************************************************")

def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def multiplica(num1, num2):
	return num1 * num2

def divide(num1, num2):
	try:
		return num1 / num2
	except ZeroDivisionError:
		print("No se puede dividir un valor entre 0...")
		return 0

valor1=(float(input("Ingrese el primer valor a operar: ")))
valor2=(float(input("Ingrese el Segundo valor a operar: ")))
Operacion=input("Introduzca la operación a ejecutar (suma, resta, multiplica, divide):")

if Operacion=="suma":
	print (suma(valor1, valor2))
elif Operacion=="resta":
	print(resta(valor1,valor2))
elif Operacion=="multiplica":
	print(multiplica(valor1,valor2))
elif Operacion=="divide":
	print(divide(valor1,valor2))
else:
	print("Operación no definida")

print("Operación ejecutada. Continuación del programa...")



print("******************************************************")
print("Curso No. 22 Excepciones" ) 
print("******************************************************")

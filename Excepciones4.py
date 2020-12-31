print("******************************************************")
print("Curso No. 23 Excepciones" ) 
print("******************************************************")

def divide():
	try:

		op1=(float(input("Ingrese el primer valor a operar: ")))
		op2=(float(input("Ingrese el segundo valor a operar: ")))
		print("La división es: " + str(op1/op2))

	except ValueError:
		print("El valor introducido es erróneo")

	except ZeroDivisionError:
		print("No se puede dividir entre 0!")

	print("Cálculo finalizado...")

def divide2():
	try:

		op1=(float(input("Ingrese el primer valor a operar: ")))
		op2=(float(input("Ingrese el segundo valor a operar: ")))
		print("La división es: " + str(op1/op2))

	except ValueError:
		print("El valor introducido es erróneo")

	except ZeroDivisionError:
		print("No se puede dividir entre 0!")
	
	#la instruccion finally se ejecuta 
	#siempre aun asi se haya capturado una excepción.
	finally:
		print("Cálculo finalizado...")
	#si un try no tiene la captura de error except y si finally el finally se ejecutara
	#pero luego el programa cae pues se exterioriza el error detectado anteriormente.

def divide3():
	try:

		op1=(float(input("Ingrese el primer valor a operar: ")))
		op2=(float(input("Ingrese el segundo valor a operar: ")))
		print("La división es: " + str(op1/op2))

	except:
		print("se registro un error")

	print("Cálculo finalizado...")	


def EvaluaEdad(edad):

	if edad<0:
		raise ZeroDivisionError("No se permiten edades negativas...")

	if edad <20:
		return "Eres muy Joven"
	elif edad < 40:
		return "Eres Joven"
	elif edad < 65:
		return "Eres maduro"
	elif edad < 100:
		return "Cuidate..."

import math

def CalculaRaiz(num1):
	if num1 < 0:
		raise ValueError("Error en valor, este no puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("introduce un número: ")))

try:
	print(CalculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)


print("finalizo programa")


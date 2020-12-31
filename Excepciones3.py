print("******************************************************")
print("Curso No. 22 Excepciones" ) 
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

divide3()


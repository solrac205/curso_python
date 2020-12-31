print("******************************************************")
print("Curso No. 14 bucles" ) 
print("******************************************************")

#existen bucles for
#python posee bucles determinados y bucles indeterminados.
print("esta es una prueba de bucle determinado")

for i in range(1,11):
  print(i)

print("fin del bucle")

print("Bucle recorriendo un string")
for i in "cramirez@dominiodepruebas.com":
	print(i)

print("Fin de recorrido de string.")


print("******************************************************")
print("Curso No. 17 bucles while" ) 
print("******************************************************")
i=1
while i<=10: 
#mientras la condicion se cumple, cuando ya no se cumple se rompe el bucle.
    print(f"hola {i}")
    i=i+1

print("Termino la ejecucion del while")


#instruccion Continue, Pass y Else
#Continue: Sirve para Saltar una interaccion del bucle, ignorando el contenido de la vuelta.
#

for letra in "python":

	if letra=="h":
		continue
	print(f"Viendo la letra: {letra}")


email="carlos@algundominio.com.gt"

for i in email:
	if i=="@":
		arroba=True
		break;
	print(i)
else:
	arroba = False

print(arroba)

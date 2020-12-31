def DigitoVerificador():
    
    FactorMultiplicador=2
    AcumValues=0
    CadenaTranspuesta=""

    ValorIngresado = input("ingrese el valor a generar Digito Verificador: ")

    for i in ValorIngresado:
        if i not in ("0","1","2","3","4","5","6","7","8","9"):
            print("Existe Error")
            return ""
        CadenaTranspuesta = i + CadenaTranspuesta
    #print (CadenaTranspuesta)

    for i in CadenaTranspuesta:
        #print(i + "*" + str(FactorMultiplicador) + "=" + str(int(i) * FactorMultiplicador))
        AcumValues = AcumValues + (int(i) * FactorMultiplicador)

        #if FactorMultiplicador == 7:
        #    FactorMultiplicador=2
        #else:
        FactorMultiplicador= FactorMultiplicador + 1

    #print("Valor Acumulado " + str(AcumValues))
    #print("Modulo 11 =" + str(AcumValues % 11))
    ModCalculado = (11 - (AcumValues % 11)) % 11
    #print ("Digito Resultante: " + str(ModCalculado))
    
    if ModCalculado < 10:
        return ValorIngresado + "-" + str(ModCalculado)
    elif ModCalculado == 11:
        return ValorIngresado + "-0"
    elif ModCalculado == 10:
        return ValorIngresado + "-k"


print("El nit es: " + DigitoVerificador())





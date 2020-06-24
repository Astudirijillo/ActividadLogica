def comparacion ():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    if(valor1 == valor2):
        return "0"
    else:
        if(valor1 > valor2):
            return "1"
        elif (valor1<valor2):
            return "-1"

print(comparacion())
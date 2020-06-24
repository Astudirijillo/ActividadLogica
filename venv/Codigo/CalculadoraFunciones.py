num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))

print("suma, resta, multiplicacion o division")
opcion = input("Ingrese la primera letra de la operacion a realizar: ")

def multiplicacion (num1, num2):
    print ("El resultado es", num1*num2)

def division (num1, num2):
    if (num2 == 0):
        print("No se puede dividir por 0")
    else:
        print("El resultado es", num1 / num2)

def suma():
    print("el resultado es", num1 + num2)

def suma (num1, num2):
    print ("El resultado es", num1+num2)

def resta (num1, num2):
    print ("El resultado es", num1-num2)


if(opcion.upper()== "S"):
    suma(num1, num2)
elif (opcion.upper()== "R"):
    resta(num1, num2)
elif (opcion.upper()== "M"):
    multiplicacion(num1, num2)
elif (opcion.upper()== "D"):
    division(num1, num2)


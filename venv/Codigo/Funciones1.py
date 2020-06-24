def saludo():
    print("Saludo")

def mensaje():
   print("Hola clase")
   print("Hola clase2")
   print("Hola clase3")

mensaje()
mensaje()
saludo()
mensaje()
mensaje()

def suma(): # funcion que no retorna un resultado o valor
    numero1 = 5
    numero2 = 6
    suma = 5+6
    print(suma)

def multiplicacion (num1, num2): #funcion que retorna un resultado o valor
    print ("el resultado es", num1*num2)
    return num1*num2

multiplicacion(3,4)
multiplicacion(6,5)

print(2+multiplicacion(2,3))

#crear una funcion para el area de un cuadrado, rectangulo, triangulo
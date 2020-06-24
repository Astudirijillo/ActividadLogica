print("Cuadrado, triangulo o rectangulo")
opcion = input("Ingrese la primera letra de la figura a calcular su area: ")

def cuadrado(base):
    return base * base;

def triangulo(base,altura):
    return (base*altura)/2

def rectangulo(base,altura):
    return base*altura

if(opcion.upper() =="C"):
    base = int(input("Cuanto mide la base? "))
    print("El area del cuadrado es: ",cuadrado(base))
elif(opcion.upper() =="T"):
    base = int(input("Cuanto mide la base? "))
    altura = int(input("Cuanto mide la altura? "))
    print("El area del triangulo es: ",triangulo(base, altura))
elif(opcion.upper() =="R"):
    base = int(input("Cuanto mide la base? "))
    altura = int(input("Cuanto mide la altura? "))
    print("El area del rectangulo es: ", triangulo(base, altura))
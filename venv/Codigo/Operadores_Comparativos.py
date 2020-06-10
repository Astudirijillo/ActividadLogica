## If = si; else = sino;

numero1 = input("Ingrese numero 1: ")#7
numero1 = int (numero1)

numero2 = int(input("Ingrese numero 2: "))# 8

#if(){}
if numero1 == numero2:
    print("Los numero son iguales")
#else{}
elif numero1 > numero2:
    print("El numero mayor es el primer numero", numero1)
else:
    print("El numero mayor es el segundo numero", numero2)

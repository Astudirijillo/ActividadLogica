# numero = int(input("Ingrese un valor: "))
# if numero % 2 == 0:
#     print ("El numero",numero,"es multiplo de 2")
# else:
#     print("El numero", numero, "no es multiplo de 2")
# print("")
# if numero % 4 == 0:
#     print ("El numero",numero,"es multiplo de 4")
# else:
#     print("El numero", numero, "no es multiplo de 4")
# print("")


numero=int(input("Ingrese el valor a evaluar: "))
if numero%4==0 and numero%2==0:
    print("El valor es múltiplo de 4 y de 2")
elif numero%2==0:
    print("El valor es multiplo de 2")
else:
    print("El valor no es multiplo de 2 ni de 4")

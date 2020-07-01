def funcionFor():
    print("Funcion for")
    #for variable in elemento_Iterable (lista):
    for i in "ISRAEL":
        print("i:",i)
        print(f"dentro de for {i}")

#Creamos una lista
lista_uno =['a','b','c','d']
#llamado a la funcion
#funcionFor()

# var = int(input("Cual es la cantidad de veces: "))
# for i in range(var):
#     print("i en range: ",i)

# for i in range(4,7):
#     print("i en range: ",i)

var1 = int(input("Tamaño de la lista? "))
lista = []
contador = 0
for x in range(var1):
    print("x y contador", x, contador)
    # lista[contador]= 1+contador # asignacion
    contador = 1 +contador
    lista.append(1+contador)

print("tamaño lista es: ",len(lista))

lista_numero_pares=[]
contador1 = 0
for i in range(11):
    if(i%2==0):
        lista_numero_pares.append(i)

print("Numeros pares: ",lista_numero_pares)
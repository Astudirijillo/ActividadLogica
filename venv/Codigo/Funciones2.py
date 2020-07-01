# Listas
# Conjunto de datos, ordenados segun su ingreso, separados por coma
lista_numeros = [1,2,3,4,5,6,7,9,0]
print(lista_numeros)

#las listas comienzan en la posicion cero (indice)
lista_distintos_datos = ["uno", 2, "tres", 4,]
#Orden tradicional:      0 , 1, 2, 3
#Orden invertido:        -4, -3, -2, -1
#De estas dos forma se puede acceder a los datos
print(lista_distintos_datos)

#Acceder a un dato de la lista
print(lista_distintos_datos[-1])

#Acceder a un dato desde una posicion
print("2:", lista_distintos_datos[1:])

#Suma de listas
listaFinal = lista_distintos_datos + lista_numeros
print(listaFinal)
# O tambien puede ser
print("Suma de listas:",lista_numeros+lista_distintos_datos)

lista_uno = [1,2,3,4]
lista_dos = [5,6,7,8]
lista_tres = lista_uno+lista_dos
print("Suma de listas:", lista_tres)

#Mutabilidad: reemplazar un valor por otro
lista_tres[4]=9
print("Suma de listas 2 ",lista_tres)

#agregar nuevo contenido a la lista
lista_tres.append(5)
print("Suma de listas 3",lista_tres)
lista_tres.append("0")
print("Suma de listas 3",lista_tres)
print(lista_tres[9])
print(lista_tres[:5])
print(lista_tres[5:])

lista_tres[:5] = ['a']
print(lista_tres)
print("Len: ",len(lista_tres))


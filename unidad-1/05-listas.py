lista = []  #lista vacía
lista = [1, 2, 3]
lista2 = lista.copy() #copiando lista

lista.append(4) #Agrega un elemento al final de la lista

print(lista)
print(lista2)

#Contando cuántas veces existe un elemento en esta lista
print('El elemento 1 aparece', lista2.count(1), ' veces en esta lista.')

#imprimir la longitud de una lista
print('Lista tiene una longitud de ', len(lista))

#Acceder a los elementos de un arreglo
print(lista[1])

#eliminar el último elemento de la lista
lista.pop()
print(lista)

#eliminar elemento en particular
lista.remove(2) #Se le pasa el VALOR del elemento que quiero eliminar, no la posicion
print(lista)

#Darle la vuelta a la lista
lista2.reverse()
print(lista2)

#ordenar la lista2 (Los datos deben de ser del mismo tipo)
lista2.sort()
print(lista2)

lista.clear() #limpiando lista
print(lista)

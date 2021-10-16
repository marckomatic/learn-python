
#Diccionarios
diccionarioNinio = {
    "edad": 2,
    "nombre": "Juanito",
    "sexo": "Indefinido"
}

print(diccionarioNinio)

#Para acceder a un valor del diccionario
print(diccionarioNinio["nombre"])

print(diccionarioNinio.get("sexo"))

diccionarioNinio["sexo"] = "Masculino"
print(diccionarioNinio)

print(len(diccionarioNinio))

diccionarioNinio["chingaMucho"] = "si"
print(diccionarioNinio)

#eliminar un elemento
#diccionarioNinio.pop("chingaMucho")

#eliminar el ultimo valor que se agrego al diccionario
#diccionarioNinio.popitem()

#eliminar una llave
del diccionarioNinio["chingaMucho"]
print(diccionarioNinio)

#copiar un diccionario

copiaNinio = diccionarioNinio.copy()

print(copiaNinio)

#diccionarios anidados

gatitos = {
    "fluffy": {
        "nombre": "Fluffy", 
        "edad": 12
    },
    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12
    }
}

print(gatitos)

#constructor dic
perritos = dict(nombre="Bethooven", edad=12)
print(perritos)
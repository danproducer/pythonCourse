#STRINGS & NÚMEROS

palabra = 'Hola mundo' # string
oracion = "Hola mundo con comillas dobles" # string

entero = 20 # integer
decimales = 15.6 # Float
complejo = 1j 

#print(palabra, oracion, entero, decimales, complejo)

# INTRODUCCIOON A LAS LISTAS

# lista = [1, 2, 3]
# lista2 = lista.copy() # copia de lista sin el append
# lista.append(4) # Esto es un "metodo append de la lista" cambia la lista sin necesidad de crear una nueva
# #lista.clear() # Metodo limpia y elimina los elementos de la lista

# print(lista, lista2)

# CONTANDO ELEMENTOS Y CALCULANDO EL LARGO DE UNA LISTA

# lista = [1, 2, 3, 3, 5]
# lista2 = lista.copy() # copia de lista sin el append
# lista.append(4) # Esto es un "metodo append de la lista" cambia la lista sin necesidad de crear una nueva
# #lista.clear() # Metodo limpia y elimina los elementos de la lista

# print(lista, lista2.count(3))
# print(len(lista)) # cuentame los elementos que se encuentran en esta lista

# ACCEDIENDO A ELEMENTOS DE LAS LISTAS

# lista = ['Hola', 'mundo', 'el chancho']
# lista2 = lista.copy()
# lista.append('perro')

# # print(lista[2])
# # lista.pop() # Eliminar el ultimo elemento de la lista
# # lista.remove('Hola') # Eliminar un elemento en especifico de la lista
# lista.reverse() # pone el ordén al reves
# lista.sort() # Ordena la lista del modo correcto teniendo solo strings o solo números, no pude ser datos dferentes
# print(lista)

# # TUPLAS - DIFERENCIA DE LAS LISTAS ES QUE NO SE PUEDEN MODIFICAR COMO LAS LISTAS.

# tupla  = ('hola', 'mundo', 'soy', 'una tupla')
# listaDeTupla = list(tupla)
# listaDeTupla.append('tlr')
# print(listaDeTupla)

# # RANGE DATOS QUE SIRVEN PARA TRABAJAR CON LAS ITERACIONES

# rango = range(6)
# print(rango)

#INTRO A LOS DICCIONARIOS: SON BASTANTES SIMILARES A LAS LISTAS PERO CON LA DIFERENCIA ES QUE PARA REFERIRNOS A UN VALOR EN PARTICULAR UTILIZAMOS STRINGS Y NO NUMEROS

diccionario = { #las llaves para los diccionarios
    "nombre": "juan carlos chupa pija", #siempre necesita comas
    "raza": "man",
    "edad": 30
}
# print(diccionario)
# print(diccionario["nombre"])
# print(diccionario.get('nombre'))
diccionario["nombre"] = "JuanCa" # se puede cambiar un dato en especifico del diccionario asi
print(len(diccionario)) # contar cuantos elementos contiene el diccionario

diccionario['ronronea'] = 'No, es un humano'
# print(diccionario)
# # diccionario.pop('ronronea') #eliminar propiedad en especifico dentro del diccionario
# # diccionario.popitem() Elimina el ultimo item que se agregó al diccionario
# del diccionario["ronronea"]
# copiaAnimal = diccionario.copy()
# print(diccionario, copiaAnimal)

gatitos = { # Diccionarios anidados
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Black mamba",
        "edad": "10"
    }
}
print(gatitos)

perritos = dict(nombre="Michi", edad=75) # constructor dict para crear diccionarios tambien
print(perritos)

# BOOLENAOS - VERDADERO O FALSO va a ser util con el CONTROL DE FLUJO

verdadero = True #valores true o false
falso = False

print(verdadero, falso)


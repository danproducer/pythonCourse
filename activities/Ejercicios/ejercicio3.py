# Escribir una función que encuentre el elemento menor de una lista

lista = [1, 2, 4, 5, 7, 8, -3]

menor = 'inicial'

for x in lista:
    if menor == 'inicial':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)
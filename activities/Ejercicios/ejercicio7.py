# Escribir una funcion que inidique cuantas vocales tiene una palabra

word = 'HOlandas'
vocales = 0

for x in word:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print(vocales)
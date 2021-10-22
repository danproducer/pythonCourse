# Escribir una función que reciba nombre y apellido y los vaya agregando a un archivo

def addNameToFile(nombre, apellido):
    c = open('nombre.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

addNameToFile('Pepito', 'Perez')
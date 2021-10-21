def miFuncion():
    print('Mi primer funcion, yay!')

# miFuncion()

# def impData(name, surname): # funcion se definio que debe tener si o si 2 argumentos se deben pasar los parametros de esos 2 argumentos
#     print('El nombre completo es:', name, surname)

# impData('Felipe', 'Acosta')

def showData(*name):
    print('El nombre es:', name[3])

# showData('Dan', 'Carol', 'Abi', 'Amelie', 'pepe')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto('tocarruncho', 'Amador')

def nombreCompleto2(**kwargs): #argumento por llave en sintaxis de diccionario para f
    print(kwargs['nombre'], kwargs['apellido'])

nombreCompleto2(nombre='Lalo', apellido='Pez')

#valor por defecto al argumento

def miFuncion2(argumento = 'Nene'):
    print(argumento)
# miFuncion2('Bat')
# miFuncion2()

def miFuntionList(lista):
    for el in lista:
        print(el)

miFuntionList(['Carlos', 'Gonzalez Calle'])

def concatenaNames(lista):
    i = ''
    for el in lista:
        i = i + el + ''
    return i

nombres = concatenaNames(['Ñeros','lavia'])
print(nombres)


# RECURSIVIDAD EN PYTHON: CÓMO PODEMOS REALIZAR RECURSIVIDAD

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(-1)
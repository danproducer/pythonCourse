primer = input('Ingresa el primer número: ')
try:
    primer = int(primer)
except:
    primer = 'Hola'

if primer == 'Hola':
    print('No es un valor valido, sorry, usa un entero')
    exit()

segundo = input('Ingresa el segundo número: ')
try:
    segundo = int(segundo)
except:
    segundo = 'mundo'

if segundo == 'mundo':
    print('No es un valor valido, sorry, usa un entero')
    exit()

simbolo = input('Ingrese operación: ')

if simbolo == '+':
    print('Suma: ', primer + segundo)
elif simbolo == '-':
    print('Resta: ', primer - segundo)
elif simbolo == '*':
    print('Multiplicación: ', primer * segundo)
elif simbolo == '/':
    print('División: ', primer / segundo)
else:
    print('El simbolo que ha ingresiado no es valido')

# if primer == 'Hola' or segundo == 'mundo':
#     print('Ingreso un dato erroneo, solo se aceptan números')
# else:
#     print(primer + segundo)
# primerNumero = int(primer)
# segundoNumero = int(segundo)
# print(primerNumero + segundoNumero)


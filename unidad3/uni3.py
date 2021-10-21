# BOOLENAOS - VERDADERO O FALSO va a ser util con el CONTROL DE FLUJO

verdadero = True #valores true o false
falso = False

# print(verdadero, falso)

                                #CONTROL DE FLUJO
#IF Y CONDICIONES

if 2 < 5:
    print('2 es menor que 5')

# 2 variables son iguales a == b

if 2 == 2:
    print('2 es igual a 2')

if 2 == 3:
    print('2 es igual a 3')

# una variable es menor que la otra a < b

if 2 < 1:
    print('2 es menor a 8')

# una variable es mayor a la otra a > b

if 5 > 2:
    print('5 es mayor a 2')

# una variable diferente a la otra a != b

if 2 != 8:
    print('2 es diferente a 8')

# a <= b

if 9 <= 8:
    print('9 es menor o igual a 8')

# a >= b

if 8 >= 6:
    print('8 es mayor a 6')


# IF, ELIF & ELSE

if 2 > 5:
    print('Lalo')
elif 2 > 5:
    print('2 es menor a 5 en elif')
else:
    print('Yo me imprimo solo si todo lo anterior evalua en falso')


if 6 > 8:
    print('Lalo')
else:
    print('Yo me imprimo solo si todo lo anterior evalua en falso')

# IF CORTOS Y TERNARIOS

if 2 < 3: print('if de una linea') #OPCION 1

print('cuando devuelve true') if 5 < 2 else print('cuando devuelve falso') # OPCION 2 operador ternario

# AND Y OR

if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

if 2 < 5 and 3 < 2: # si hay una falsa no se ejecuta
    print('ambas devuelven true')

if 1 < 0 or 1 < 0:
    print('una de las dos devolvio true') # si las 2 son falsas no se ejecuta

# LOOPS: WHILE LOOP -- WHILE: BREAK & CONTINUE -- FOR LOOP

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue #BREAK & CONTINUE
    print(i)
    
# usuarios = ['Fede', 'Henry', 'Pepito', 'Nasty']

# for usuario in usuarios:
#     print(usuario)



# usuarios = ['Fede', 'Henry', 'Pepito', 'Nasty']

# for usuario in usuarios:
#     if usuario == 'Pepito':
#         continue
#     print(usuario)


for x in range(1, 6):
    print(x)

for y in range(3, 30, 5):
    print(y)
else:
    print('We are done, dude! yay!')

usuarios = ['Fede', 'Henry', 'Pepito', 'Nasty']
edades = [26, 25, 15, 19]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)
else:
    print('Chao pues')

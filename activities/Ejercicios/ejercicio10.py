print('Ingrese el año: ')

anio = int(input())

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print('Año bisiesto')
else:
    print('No es un año bisiesto')
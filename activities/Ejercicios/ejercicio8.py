# Escribir una aplicacion que reciba una cantidad infinita de números hasta decir basta,
# luego que devuleva la suma de los números ingresados

lista = []
print('Ingrese números y para salir escriba "basta"')

while True:
    valor = input('Ingrese valor: ')
    if valor== 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato invalido')

resultado = 0
for x in lista:
    resultado += x

print(resultado)

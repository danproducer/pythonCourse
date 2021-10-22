c = open('textX.txt', 'a')
# print(c.read()) #Tener cuidado con el tamaño del archivo para no sobrecargar el comando a realizar
c.write('agregando una nueva linea a nuestro archivo')
c.close()
# print(c.readline())
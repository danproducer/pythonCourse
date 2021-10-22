# from uni5 import saludo, mascotas #importar lo necesario de otro modulo
import uni5 as modulo #cambiar el nombre del modulo para esta hoja
from camelcase import CamelCase # PIP HERRAMIENTA QUE NOS PERMITE GESTIONAR LOS PAQUETES Y MODULOS QUE TENEMOS INSTALADO EN PYTHON
# modulo.saludo('Daniel')

c = CamelCase() 
s = 'this is a sentence that needs camelcase'

camelcased = c.hump(s)
print(camelcased)
# print(mascotas)
# saludo('Caro')



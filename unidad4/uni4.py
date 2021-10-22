# OBJETOS

# class Usuario: #plano de un usuario: como se deberia ver un usuario #class padre
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido

#     def saludo(self): #self no es necesario pero por protocolo se debe hacer
#         print('Hola! mi nombre es', self.nombre, self.apellido)

# usuario = Usuario('Feli', 'Ferrer')
# usuario2 = Usuario('Lola','mento')

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# usuario.saludo()
# usuario.nombre = 'David'
# usuario.saludo()
# del usuario.nombre
# del usuario
# print(usuario)

# HERENCIA: PODER REUTILIZAR LO MAXIMO EL CODIFO EN ESTRUCTURAS QUE SON SIMILARES

# class Admin(Usuario):  #class hijo
#     def superSaludo(self):
#         print('Hola, me llamo', self.nombre, 'y soy el administrador, bro!')

# admin = Admin('Dan', 'Tok')
# admin.saludo()
# admin.superSaludo()

#EJERCICIO DE HERENCIA & CLASS
class Admin:  #class hijo
    def superSaludo(self):
        print('Hola, me llamo', self.nombre, 'y soy el administrador, bro!')

class Animal: #Class PADRE
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola! Soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)
class Gato(Animal): #class HIJO
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): #extendiendo el método init del PADRE
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')

class Dog(Animal): #class HIJO
    tipo = 'dog'
    def __init__(self, nombre, onomatopeya): 
        super().__init__(nombre, onomatopeya) # Otra forma para extender init del PADRE
        print('Instanciando un doggy')

gato = Gato('Michi', 'Miau')
gato.saludo()

dog = Dog('Goofi', 'wauf')
dog.saludo()
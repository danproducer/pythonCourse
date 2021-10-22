# OBJETOS

class Usuario: #plano de un usuario: como se deberia ver un usuario
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola! mi nombre es', self.nombre, self.apellido)

usuario = Usuario('Feli', 'Ferrer')
usuario2 = Usuario('Lola','mento')

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

usuario.saludo()
usuario2.saludo()
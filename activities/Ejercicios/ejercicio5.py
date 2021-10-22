# Escribir una función que indique si el usuario es mayor de edad

def esOld(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esOld(usuario)
resultado2 = esOld(usuario2)

print(resultado1, resultado2)
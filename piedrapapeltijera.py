import random

opciones = ["piedra", "papel", "tijera"]

def eleccionPC() :
    return random.choice(opciones)


def eleccionUsuario() :
    return 
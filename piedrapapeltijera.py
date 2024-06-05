import random

opciones = ["piedra", "papel", "tijera"]

def eleccionPC() :
    return random.choice(opciones)

def eleccionUsuario():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in opciones:
        eleccion = input("Entrada no válida. Elige piedra, papel o tijera: ").lower()
    return eleccion
    

def determinar_ganador(usuario,pc):
    if usuario == pc:
        return "Empate"
    elif (usuario == "piedra" and pc == "tijera") or \
         (usuario == "papel" and pc == "piedra") or \
         (usuario == "tijera" and pc == "papel"):
         return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")

    while True:
        usuario = eleccionUsuario()
        pc = eleccionPC()
        print(f"Tú elegiste: {usuario}")
        print(f"La computadora eligió: {pc}")
        resultado = determinar_ganador(usuario,pc)
        print(f"Resultado: {resultado}")
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_de_nuevo != "si":
            break

    print("¡Gracias por jugar!")


if __name__ == "__main__":
    jugar()
        



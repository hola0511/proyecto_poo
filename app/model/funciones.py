import random


class Jugador:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.puntos: int = 0

    def lanzar_dado(self):
        return random.randint(1, 6)

    def acumular_puntos(self, puntos: str):
        if puntos == 1:
            self.puntos = 0
        else:
            self.puntos += puntos

    def get_puntos(self):
        return self.puntos


class Juego:
    def __init__(self):
        self.jugadores = []

    def iniciarjuego(self):
        while True:
            try:
                num_jugadores = int(input("Ingrese el número de jugadores: "))
                if num_jugadores > 0:
                    break
                else:
                    print("Por favor ingrese un número válido mayor que 0.")
            except ValueError:
                print("Por favor ingrese un número válido mayor que 0.")

        for i in range(num_jugadores):
            nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
            self.jugadores.append(Jugador(nombre))

    def terminar_juego(self):
        print("Juego terminado.")
        for jugador in self.jugadores:
            print(f"{jugador.nombre}: {jugador.puntos} puntos.")

    def guardar_juego(self):
        # Implementar la lógica para guardar el estado del juego
        pass

    def cargar_juego(self):
        # Implementar la lógica para cargar un juego guardado previamente
        pass

def preguntar_jugar_nuevo():
    decision = input("¿Quieres empezar un nuevo juego? (s/n): ")
    return decision.lower() == 's'

def main():
    juego = Juego()
    juego.iniciarjuego()

    while True:
        for jugador in juego.jugadores:
            input(f"{jugador.nombre}, presiona Enter para lanzar el dado o 'f' para finalizar el juego.")
            decision = input("Presiona 'f' para finalizar el juego o Enter para lanzar el dado: ")
            if decision.lower() == 'f':
                juego.terminar_juego()
                if not preguntar_jugar_nuevo():
                    print("¡Hasta luego! Gracias por jugar.")
                    return
                else:
                    juego = Juego()
                    juego.iniciarjuego()
                    break
            puntos = jugador.lanzar_dado()
            jugador.acumular_puntos(puntos)
            if puntos == 1:
                print(f"{jugador.nombre} sacó un 1. ¡Pierde todos sus puntos!")
            else:
                print(f"{jugador.nombre} lanzó un dado y obtuvo {puntos} puntos. Puntos acumulados: {jugador.puntos}")
            if jugador.puntos >= 50:
                print(f"{jugador.nombre} ha alcanzado o superado los 50 puntos. ¡Ha ganado!")
                juego.terminar_juego()
                if not preguntar_jugar_nuevo():
                    print("¡Hasta luego! Gracias por jugar.")
                    return
                else:
                    juego = Juego()
                    juego.iniciarjuego()
                    break

if __name__ == "__main__":
    main()
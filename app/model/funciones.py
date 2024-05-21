import random


class Jugador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.puntos = 0

    def lanzar_dado(self):
        return random.randint(1, 6)

    def acumular_puntos(self, puntos: int):
        if puntos == 1:
            self.puntos = 0
        else:
            self.puntos += puntos

    def get_puntos(self):
        return self.puntos


class Juego:
    def __init__(self):
        self.jugadores = []

    def iniciarjuego(self, num_jugadores: int, nombres_jugadores: list):
        for nombre in nombres_jugadores:
            self.jugadores.append(Jugador(nombre))

    def terminar_juego(self):
        resultados = []
        for jugador in self.jugadores:
            resultados.append((jugador.nombre, jugador.puntos))
        return resultados

    def guardar_juego(self):
        pass

    def cargar_juego(self):
        pass


def preguntar_jugar_nuevo():
    decision = input("¿Quieres empezar un nuevo juego? (si/no): ")
    return decision.lower() == 'si'


def main():
    juego = Juego()
    num_jugadores = 0

    while True:
        try:
            num_jugadores = int(input("Ingrese el número de jugadores: "))
            if num_jugadores > 0:
                break
            else:
                print("Por favor ingrese un número válido mayor que 0.")
        except ValueError:
            print("Por favor ingrese un número válido mayor que 0.")

    nombres_jugadores = []
    for i in range(num_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
        nombres_jugadores.append(nombre)

    juego.iniciarjuego(num_jugadores, nombres_jugadores)

    while True:
        for jugador in juego.jugadores:
            decision = input(f"{jugador.nombre}, presiona Enter para lanzar el dado o 'f' para finalizar el juego.")
            if decision.lower() == 'f':
                resultados = juego.terminar_juego()
                print("Juego terminado.")
                for nombre, puntos in resultados:
                    print(f"{nombre}: {puntos} puntos.")
                if not preguntar_jugar_nuevo():
                    print("¡Hasta luego! Gracias por jugar.")
                    return
                else:
                    juego = Juego()
                    num_jugadores = 0
                    while True:
                        try:
                            num_jugadores = int(input("Ingrese el número de jugadores: "))
                            if num_jugadores > 0:
                                break
                            else:
                                print("Por favor ingrese un número válido mayor que 0.")
                        except ValueError:
                            print("Por favor ingrese un número válido mayor que 0.")
                    nombres_jugadores = []
                    for i in range(num_jugadores):
                        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
                        nombres_jugadores.append(nombre)
                    juego.iniciarjuego(num_jugadores, nombres_jugadores)
                    break
            puntos = jugador.lanzar_dado()
            jugador.acumular_puntos(puntos)
            if puntos == 1:
                print(f"{jugador.nombre} sacó un 1. ¡Pierde todos sus puntos!")
            else:
                print(f"{jugador.nombre} lanzó un dado y obtuvo {puntos} puntos. Puntos acumulados: {jugador.puntos}")
            if jugador.puntos >= 50:
                print(f"{jugador.nombre} ha alcanzado o superado los 50 puntos. ¡Ha ganado!")
                resultados = juego.terminar_juego()
                print("Juego terminado.")
                for nombre, puntos in resultados:
                    print(f"{nombre}: {puntos} puntos.")
                if not preguntar_jugar_nuevo():
                    print("¡Hasta luego! Gracias por jugar.")
                    return
                else:
                    juego = Juego()
                    num_jugadores = 0
                    while True:
                        try:
                            num_jugadores = int(input("Ingrese el número de jugadores: "))
                            if num_jugadores > 0:
                                break
                            else:
                                print("Por favor ingrese un número válido mayor que 0.")
                        except ValueError:
                            print("Por favor ingrese un número válido mayor que 0.")
                    nombres_jugadores = []
                    for i in range(num_jugadores):
                        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
                        nombres_jugadores.append(nombre)
                    juego.iniciarjuego(num_jugadores, nombres_jugadores)
                    break


if __name__ == "__main__":
    main()

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

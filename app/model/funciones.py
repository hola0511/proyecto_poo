class Jugador:
    def __init__(self, nombre: str, puntos:int):
        self.nombre: str = nombre
        self.puntos: int = puntos
    def lanzar_dado(self) -> int:
        pass

    def acumular_puntos(self, puntos:int):
        pass

    def get_puntos(self) -> int:
        pass


class Juego:
    jugadores: [Jugador]

    def iniciar_juego(self):
        pass

    def terminar_juego(self):
        pass

    def guardar_juego(self):
        pass

    def cargar_juego(self):
        pass

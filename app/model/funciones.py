import random


class JuegoDeDados:
    def __init__(self):
        self.puntos_acumulados = 0
        self.puntos_objetivo = 50
        self.record = 0

    def tirar_dado(self):
        return random.randint(1, 6)

    def jugar_turno(self):
        dado = self.tirar_dado()
        if dado == 1:
            self.puntos_acumulados = 0
            print("¡Sacaste un 1! Perdiste todos tus puntos acumulados.")
        else:
            self.puntos_acumulados += dado
            print(f"Tiraste un {dado}. Puntos acumulados: {self.puntos_acumulados}")

    def jugar_partida(self):
        while self.puntos_acumulados < self.puntos_objetivo:
            decision = input("Presiona 't' para tirar el dado o 'f' para finalizar la partida: ")
            if decision == 't':
                self.jugar_turno()
            elif decision == 'f':
                print("Partida finalizada.")
                return True
            else:
                print("Entrada no válida. Por favor, ingresa 't' o 'f'.")
        else:
            print("¡Felicidades! Has alcanzado o superado los 50 puntos. ¡Has ganado la partida!")
            return True

    def mostrar_record(self):
        print(f"El récord actual es: {self.record} puntos.")

    def actualizar_record(self):
        if self.puntos_acumulados > self.record:
            self.record = self.puntos_acumulados
            print(f"¡Nuevo récord establecido! {self.record} puntos.")


# Función para preguntar al jugador si quiere jugar de nuevo o terminar
def preguntar_jugar_nuevo():
    decision = input("¿Quieres empezar un nuevo juego? (si/no): ")
    return decision.lower() == 'si'


# Función principal del juego
def main():
    juego = JuegoDeDados()
    juego.mostrar_record()

    while True:
        if juego.jugar_partida():
            juego.actualizar_record()

            if not preguntar_jugar_nuevo():
                print("¡Hasta luego! Gracias por jugar.")
                break


if __name__ == "__main__":
    main()
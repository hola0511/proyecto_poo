import random
import json
import os


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

    def iniciar_juego(self, num_jugadores: int, nombres_jugadores: list):
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


class JugadorPersonalizado(Jugador):
    def lanzar_dado(self, min_val: int, max_val: int):
        return random.randint(min_val, max_val)


class JuegoPersonalizado(Juego):
    def __init__(self):
        super().__init__()
        self.puntos_ganar = 100
        self.min_val_dado = 1
        self.max_val_dado = 6
        self.mejores_puntuaciones = []

    def iniciar_juego(self, nzum_jugadores: int, nombres_jugadores: list, puntos_ganar: int, min_val_dado: int, max_val_dado: int):
        self.puntos_ganar = puntos_ganar
        self.min_val_dado = min_val_dado
        self.max_val_dado = max_val_dado
        for nombre in nombres_jugadores:
            self.jugadores.append(JugadorPersonalizado(nombre))

    def turno_jugador(self, jugador: JugadorPersonalizado):
        puntos = jugador.lanzar_dado(self.min_val_dado, self.max_val_dado)
        resultado = f"{jugador.nombre} ha lanzado el dado y ha sacado {puntos}"
        if puntos == 1:
            pregunta, respuesta_correcta = self.responder_pregunta()
            resultado += f"\n{pregunta}"
            respuesta_usuario = input("Tu respuesta: ")  # Pedir respuesta al usuario
            if respuesta_usuario.lower() == respuesta_correcta.lower():
                resultado += f"\n{jugador.nombre} ha respondido correctamente y mantiene sus puntos."
            else:
                jugador.puntos = 0
                resultado += f"\n{jugador.nombre} ha respondido incorrectamente y pierde todos sus puntos."
        else:
            jugador.acumular_puntos(puntos)
            resultado += f"\n{jugador.nombre} ahora tiene {jugador.get_puntos()} puntos."
            if jugador.get_puntos() >= self.puntos_ganar:
                resultado += f"\n{jugador.nombre} ha ganado el juego con {jugador.get_puntos()} puntos!"
                self.guardar_mejores_puntuaciones(jugador)
                return resultado, True
        return resultado, False

    def responder_pregunta(self):
        preguntas = [
            {
                "pregunta": "¿Cuál de estos animales no es un mamífero?",
                "opciones": ["a) Ballena", "b) Pingüino", "c) Cocodrilo", "d) Jirafa"],
                "respuesta": "c"
            },
            {
                "pregunta": "¿En qué ciudad se encuentra el Museo del Prado?",
                "opciones": ["a) Madrid", "b) Barcelona", "c) Sevilla", "d) Valencia"],
                "respuesta": "a"
            },
            {
                "pregunta": "¿Cuál es la obra más famosa de William Shakespeare?",
                "opciones": ["a) Hamlet", "b) Romeo y Julieta", "c) Macbeth", "d) El Rey Lear"],
                "respuesta": "b"
            },
            {
                "pregunta": "¿Cuál es la bandera de Colombia?",
                "opciones": [
                    "a) Verde, amarillo y azul con una franja roja horizontal en el centro",
                    "b) Rojo, amarillo y azul con una franja verde horizontal en el centro",
                    "c) Amarillo, azul y rojo con una franja verde horizontal en el centro",
                    "d) Azul, amarillo y rojo con una franja verde diagonal"
                ],
                "respuesta": "c"
            },
            {
                "pregunta": "¿Cuál es el elemento químico con símbolo Au?",
                "opciones": ["a) Plata", "b) Oro", "c) Cobre", "d) Hierro"],
                "respuesta": "b"
            },
            {
                "pregunta": "¿En qué año se descubrió América?",
                "opciones": ["a) 1492", "b) 1502", "c) 1602", "d) 1702"],
                "respuesta": "a"
            },
            {
                "pregunta": "¿Cuál es el planeta más pequeño del Sistema Solar?",
                "opciones": ["a) Mercurio", "b) Venus", "c) Tierra", "d) Marte"],
                "respuesta": "a"
            },
            {
                "pregunta": "¿Quién escribió 'Cien años de soledad'?",
                "opciones": ["a) Gabriel García Márquez", "b) Mario Vargas Llosa", "c) Isabel Allende", "d) Jorge Luis Borges"],
                "respuesta": "a"
            },
            {
                "pregunta": "¿Cuál es el río más caudaloso del mundo?",
                "opciones": ["a) Amazonas", "b) Nilo", "c) Yangtze", "d) Misisipi"],
                "respuesta": "a"
            },
            {
                "pregunta": "¿De qué está hecho el Sol?",
                "opciones": ["a) Hidrógeno y helio", "b) Oxígeno y nitrógeno", "c) Carbono y silicio", "d) Hierro y níquel"],
                "respuesta": "c"
            },
            {
                "pregunta": "¿Cuál es el río más largo del mundo?",
                "opciones": ["a) Nilo", "b) Amazonas", "c) Yangtsé", "d) Misisipi"],
                "respuesta": "b"
            },
            {
                "pregunta": "¿Quién escribió 'El principito'?",
                "opciones": ["a) Antoine de Saint-Exupéry", "b) J.K. Rowling", "c) Gabriel García Márquez", "d) William Shakespeare"],
                "respuesta": "d"
            },
            {
                "pregunta": "¿Cuál es el elemento químico más abundante en la corteza terrestre?",
                "opciones": ["a) Oxígeno", "b) Hierro", "c) Carbono", "d) Silicio"],
                "respuesta": "d"
            },
            {
                "pregunta": "¿Cuál es la capital de Australia?",
                "opciones": ["a) Sídney", "b) Canberra", "c) Melbourne", "d) Brisbane"],
                "respuesta": "b"
            },
            {
                "pregunta": "¿Quién pintó la Mona Lisa?",
                "opciones": ["a) Leonardo da Vinci", "b) Pablo Picasso", "c) Vincent van Gogh", "d) Claude Monet"],
                "respuesta": "a"
            },
            {
                "pregunta": "¿Cuál es el país más grande del mundo por territorio?",
                "opciones": ["a) China", "b) Estados Unidos", "c) Rusia", "d) Canadá"],
                "respuesta": "c"
            },
            {
                "pregunta": "¿Quién fue el primer ser humano en viajar al espacio?",
                "opciones": ["a) Yuri Gagarin", "b) Neil Armstrong", "c) Buzz Aldrin", "d) Alan Shepard"],
                "respuesta": "a"
            },
            {
                "pregunta": "¿Cuál es el océano más grande del mundo?",
                "opciones": ["a) Atlántico", "b) Índico", "c) Pacífico", "d) Ártico"],
                "respuesta": "c"
            }
        ]

        pregunta = random.choice(preguntas)
        opciones = "\n".join(pregunta["opciones"])
        return f"{pregunta['pregunta']}\n{opciones}", pregunta["respuesta"]

    def jugar(self):
        resultado = []
        ganador = False
        while not ganador:
            for jugador in self.jugadores:
                turno_resultado, ganador = self.turno_jugador(jugador)
                resultado.append(turno_resultado)
                print(turno_resultado)
                if ganador:
                    break
        return resultado

    def guardar_juego(self):
        estado = {
            'jugadores': [{'nombre': j.nombre, 'puntos': j.puntos} for j in self.jugadores],
            'puntos_ganar': self.puntos_ganar,
            'min_val_dado': self.min_val_dado,
            'max_val_dado': self.max_val_dado
        }
        with open('juego_guardado.json', 'w') as archivo:
            json.dump(estado, archivo)
        return "Juego guardado."

    def cargar_juego(self):
        if os.path.exists('juego_guardado.json'):
            with open('juego_guardado.json', 'r') as archivo:
                estado = json.load(archivo)
            self.jugadores = [JugadorPersonalizado(j['nombre']) for j in estado['jugadores']]
            for jugador, datos in zip(self.jugadores, estado['jugadores']):
                jugador.puntos = datos['puntos']
            self.puntos_ganar = estado['puntos_ganar']
            self.min_val_dado = estado['min_val_dado']
            self.max_val_dado = estado['max_val_dado']
            return "Juego cargado."
        else:
            return "No hay ningún juego guardado."

    def guardar_mejores_puntuaciones(self, jugador: Jugador):
        self.mejores_puntuaciones.append((jugador.nombre, jugador.puntos, len(self.jugadores)))
        self.mejores_puntuaciones.sort(key=lambda x: x[1], reverse=True)
        with open('mejores_puntuaciones.json', 'w') as archivo:
            json.dump(self.mejores_puntuaciones, archivo)
        return "Mejores puntuaciones actualizadas."

    def mostrar_mejores_puntuaciones(self):
        if os.path.exists('mejores_puntuaciones.json'):
            with open('mejores_puntuaciones.json', 'r') as archivo:
                self.mejores_puntuaciones = json.load(archivo)
            puntuaciones = ["Mejores puntuaciones:"]
            for puntuacion in self.mejores_puntuaciones:
                puntuaciones.append(f"Jugador: {puntuacion[0]}, Puntos: {puntuacion[1]}, Rondas: {puntuacion[2]}")
            return "\n".join(puntuaciones)
        else:
            return "No hay puntuaciones registradas."


def mostrar_menu():
    opciones = [
        "1. Juego Clásico",
        "2. Juego Personalizado",
        "3. Cargar juego",
        "4. Mostrar mejores puntuaciones",
        "5. Salir"
    ]
    return "\n".join(opciones)


def juego_principal():
    resultados = []
    while True:
        menu = mostrar_menu()
        print(menu)
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            num_jugadores = int(input("Introduce el número de jugadores: "))
            nombres_jugadores = [input(f"Introduce el nombre del jugador {i + 1}: ") for i in range(num_jugadores)]
            juego = Juego()
            juego.iniciar_juego(num_jugadores, nombres_jugadores)
            print("Juego Clásico no implementado.")
        elif opcion == '2':
            num_jugadores = int(input("Introduce el número de jugadores: "))
            nombres_jugadores = [input(f"Introduce el nombre del jugador {i + 1}: ") for i in range(num_jugadores)]
            puntos_ganar = int(input("Introduce el puntaje que se debe alcanzar para ganar (25-100): "))
            min_val_dado = int(input("Introduce el valor mínimo del dado (1-3): "))
            max_val_dado = int(input("Introduce el valor máximo del dado (4-25): "))
            juego = JuegoPersonalizado()
            juego.iniciar_juego(num_jugadores, nombres_jugadores, puntos_ganar, min_val_dado, max_val_dado)
            resultados.extend(juego.jugar())
            print("Resultados finales:")
            for nombre, puntos in juego.terminar_juego():
                print(f"{nombre}: {puntos} puntos")
        elif opcion == '3':
            juego = JuegoPersonalizado()
            cargar_resultado = juego.cargar_juego()
            print(cargar_resultado)
            if "cargado" in cargar_resultado:
                resultados.extend(juego.jugar())
        elif opcion == '4':
            juego = JuegoPersonalizado()
            mejores_puntuaciones = juego.mostrar_mejores_puntuaciones()
            print(mejores_puntuaciones)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    return resultados

if __name__ == "__main__":
    juego_principal()



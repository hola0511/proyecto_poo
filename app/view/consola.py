import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0


class JuegoDeDados:
    def __init__(self):
        self.jugadores = []
        self.rondas = 0

    def agregar_jugador(self, nombre):
        self.jugadores.append(Jugador(nombre))

    def guardar_juego(self, archivo):
        with open(archivo, 'w') as f:
            for jugador in self.jugadores:
                f.write(f"{jugador.nombre},{jugador.puntos}\n")
            f.write(f"{self.rondas}\n")

    def cargar_juego(self, archivo):
        self.jugadores = []
        with open(archivo, 'r') as f:
            for line in f:
                if ',' in line:
                    nombre, puntos = line.strip().split(',')
                    nuevo_jugador = Jugador(nombre)
                    nuevo_jugador.puntos = int(puntos)
                    self.jugadores.append(nuevo_jugador)
                else:
                    self.rondas = int(line.strip())

    def lanzar_dado(self, min_valor=1, max_valor=6):
        return random.randint(min_valor, max_valor)

    def hacer_pregunta(self):
        preguntas = [
            {
                "pregunta": "¿Cuál de estos animales no es un mamífero?",
                "opciones": ["Ballena", "Pingüino", "Cocodrilo", "Jirafa"],
                "respuesta": "Pingüino"
            },
            {
                "pregunta": "¿En qué ciudad se encuentra el Museo del Prado?",
                "opciones": ["Madrid", "Barcelona", "Sevilla", "Valencia"],
                "respuesta": "Madrid"
            },
            {
                "pregunta": "¿Cuál es la obra más famosa de William Shakespeare?",
                "opciones": ["Hamlet", "Romeo y Julieta", "Macbeth", "El Rey Lear"],
                "respuesta": "Hamlet"
            },
            {
                "pregunta": "¿Cuál es la bandera de Colombia?",
                "opciones": ["Verde, amarillo y azul con una franja roja horizontal en el centro",
                             "Rojo, amarillo y azul con una franja verde horizontal en el centro",
                             "Amarillo, azul y rojo con una franja verde horizontal en el centro",
                             "Azul, amarillo y rojo con una franja verde diagonal"],
                "respuesta": "Amarillo, azul y rojo con una franja verde horizontal en el centro"
            },
            {
                "pregunta": "¿Cuál es el elemento químico con símbolo Au?",
                "opciones": ["Plata", "Oro", "Cobre", "Hierro"],
                "respuesta": "Oro"
            },
            {
                "pregunta": "¿En qué año se descubrió América?",
                "opciones": ["1492", "1502", "1602", "1702"],
                "respuesta": "1492"
            },
            {
                "pregunta": "¿Cuál es el planeta más pequeño del Sistema Solar?",
                "opciones": ["Mercurio", "Venus", "Tierra", "Marte"],
                "respuesta": "Mercurio"
            },
            {
                "pregunta": "¿Quién escribió 'Cien años de soledad'?",
                "opciones": ["Gabriel García Márquez", "Mario Vargas Llosa", "Isabel Allende", "Jorge Luis Borges"],
                "respuesta": "Gabriel García Márquez"
            },
            {
                "pregunta": "¿Cuál es el río más caudaloso del mundo?",
                "opciones": ["Amazonas", "Nilo", "Yangtsé", "Misisipi"],
                "respuesta": "Amazonas"
            },
            {
                "pregunta": "¿De qué está hecho el Sol?",
                "opciones": ["Hidrógeno y helio", "Oxígeno y nitrógeno", "Carbono y silicio", "Hierro y níquel"],
                "respuesta": "Hidrógeno y helio"
            },
            {
                "pregunta": "¿Cuál es el río más largo del mundo?",
                "opciones": ["Nilo", "Amazonas", "Yangtsé", "Misisipi"],
                "respuesta": "Nilo"
            },
            {
                "pregunta": "¿Quién escribió 'El principito'?",
                "opciones": ["Antoine de Saint-Exupéry", "J.K. Rowling", "Gabriel García Márquez",
                             "William Shakespeare"],
                "respuesta": "Antoine de Saint-Exupéry"
            },
            {
                "pregunta": "¿Cuál es el elemento químico más abundante en la corteza terrestre?",
                "opciones": ["Oxígeno", "Hierro", "Carbono", "Silicio"],
                "respuesta": "Oxígeno"
            },
            {
                "pregunta": "¿Cuál es la capital de Australia?",
                "opciones": ["Sídney", "Canberra", "Melbourne", "Brisbane"],
                "respuesta": "Canberra"
            },
            {
                "pregunta": "¿Quién pintó la Mona Lisa?",
                "opciones": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"],
                "respuesta": "Leonardo da Vinci"
            },
            {
                "pregunta": "¿Cuál es el país más grande del mundo por territorio?",
                "opciones": ["China", "Estados Unidos", "Rusia", "Canadá"],
                "respuesta": "Rusia"
            },
            {
                "pregunta": "¿Quién fue el primer ser humano en viajar al espacio?",
                "opciones": ["Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Alan Shepard"],
                "respuesta": "Yuri Gagarin"
            },
            {
                "pregunta": "¿Cuál es el océano más grande del mundo?",
                "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"],
                "respuesta": "Pacífico"
            },
            {
                "pregunta": "¿Quién escribió 'Cien años de soledad'?",
                "opciones": ["Gabriel García Márquez", "Mario Vargas Llosa", "Isabel Allende", "Julio Cortázar"],
                "respuesta": "Gabriel García Márquez"
            },
            {
                "pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?",
                "opciones": ["Aluminio", "Hierro", "Oro", "Plata"],
                "respuesta": "Aluminio"
            }
        ]

        pregunta_seleccionada = random.choice(preguntas)
        print(pregunta_seleccionada["pregunta"])
        opciones = pregunta_seleccionada["opciones"]
        random.shuffle(opciones)
        for i, opcion in enumerate(opciones):
            print(f"{chr(97 + i)}) {opcion}")

        respuesta = input("Tu respuesta: ").strip().lower()
        indice_respuesta = ord(respuesta) - 97

        if opciones[indice_respuesta] == pregunta_seleccionada["respuesta"]:
            print("¡Correcto!")
            return True
        else:
            print("Incorrecto. La respuesta correcta era:", pregunta_seleccionada["respuesta"])
            return False

    def jugar_clasico(self):
        print("Modo Clásico: Primer jugador en llegar a 50 puntos gana.")
        objetivo = 50
        self.jugar(objetivo)

    def jugar_personalizado(self, min_valor_dado, max_valor_dado, puntos_limite):
        print(f"Modo Personalizado: Primer jugador en llegar a {puntos_limite} puntos gana.")
        self.jugar(puntos_limite, min_valor_dado, max_valor_dado)

    def jugar(self, puntos_limite, min_valor_dado=1, max_valor_dado=6):
        while True:
            self.rondas += 1
            for jugador in self.jugadores:
                input(f"{jugador.nombre}, presiona Enter para lanzar el dado...")
                dado = self.lanzar_dado(min_valor_dado, max_valor_dado)
                print(f"{jugador.nombre} lanzó un {dado}")
                if dado == 1:
                    print(f"{jugador.nombre} pierde todos sus puntos.")
                    jugador.puntos = 0
                    if min_valor_dado != 1 or max_valor_dado != 6:
                        print("¡Has sacado un 1! Debes responder una pregunta.")
                        if not self.hacer_pregunta():
                            print(f"{jugador.nombre} respondió incorrectamente y pierde todos sus puntos.")
                            jugador.puntos = 0
                        else:
                            print(f"{jugador.nombre} respondió correctamente y mantiene sus puntos.")
                else:
                    jugador.puntos += dado
                print(f"{jugador.nombre} ahora tiene {jugador.puntos} puntos.")
                if jugador.puntos >= puntos_limite:
                    print(f"{jugador.nombre} ha ganado en {self.rondas} rondas!")
                    return

                if dado == 1 and (min_valor_dado != 1 or max_valor_dado != 6):
                    continuar = input("¿Deseas continuar jugando? (si/no): ").strip().lower()
                    if continuar != 's':
                        print("Juego terminado.")
                        return


def menu():
    juego = JuegoDeDados()
    while True:
        print("\n1. Jugar Clásico")
        print("2. Jugar Personalizado")
        print("3. Guardar Juego")
        print("4. Cargar Juego")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            num_jugadores = int(input("Número de jugadores: "))
            for _ in range(num_jugadores):
                nombre = input("Nombre del jugador: ")
                juego.agregar_jugador(nombre)
            juego.jugar_clasico()
        elif opcion == "2":
            min_valor_dado = int(input("Valor mínimo del dado: "))
            max_valor_dado = int(input("Valor máximo del dado: "))
            puntos_limite = int(input("Puntaje límite para ganar: "))
            num_jugadores = int(input("Número de jugadores: "))
            for _ in range(num_jugadores):
                nombre = input("Nombre del jugador: ")
                juego.agregar_jugador(nombre)
            juego.jugar_personalizado(min_valor_dado, max_valor_dado, puntos_limite)
        elif opcion == "3":
            archivo = input("Nombre del archivo para guardar el juego: ")
            juego.guardar_juego(archivo)
            print("Juego guardado.")
        elif opcion == "4":
            archivo = input("Nombre del archivo para cargar el juego: ")
            juego.cargar_juego(archivo)
            print("Juego cargado.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()

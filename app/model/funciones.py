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

        return random.choice(preguntas)

    def verificar_respuesta(self, pregunta, respuesta):
        return respuesta == pregunta["respuesta"]

    def jugar_clasico(self):
        objetivo = 50
        return self.jugar(objetivo)

    def jugar_personalizado(self, min_valor_dado, max_valor_dado, puntos_limite):
        return self.jugar(puntos_limite, min_valor_dado, max_valor_dado)

    def jugar(self, puntos_limite, min_valor_dado=1, max_valor_dado=6):
        self.rondas += 1
        for jugador in self.jugadores:
            dado = self.lanzar_dado(min_valor_dado, max_valor_dado)
            if dado == 1:
                if min_valor_dado != 1 or max_valor_dado != 6:
                    pregunta = self.hacer_pregunta()
                    return (pregunta, jugador)
                else:
                    jugador.puntos = 0
            else:
                jugador.puntos += dado
            if jugador.puntos >= puntos_limite:
                return f"{jugador.nombre} ha ganado en {self.rondas} rondas!"
        return None

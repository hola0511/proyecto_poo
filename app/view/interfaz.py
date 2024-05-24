import pygame
import sys
from app.model.funciones import JuegoDeDados

pygame.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

FUENTE = pygame.font.SysFont("Arial", 24)
FUENTE_TITULO = pygame.font.SysFont("Arial", 36)

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Dados")


def mostrar_texto(texto, x, y, color=NEGRO):
    texto_render = FUENTE.render(texto, True, color)
    pantalla.blit(texto_render, (x, y))


def mostrar_titulo(texto, x, y, color=NEGRO):
    texto_render = FUENTE_TITULO.render(texto, True, color)
    pantalla.blit(texto_render, (x, y))


def boton(texto, x, y, w, h, color_normal, color_hover, accion=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(pantalla, color_hover, (x, y, w, h))
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_normal, (x, y, w, h))

    texto_superficie = FUENTE.render(texto, True, NEGRO)
    texto_rect = texto_superficie.get_rect()
    texto_rect.center = ((x + (w / 2)), (y + (h / 2)))
    pantalla.blit(texto_superficie, texto_rect)


class InputBox:
    def __init__(self, x, y, w, h, texto=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactivo = NEGRO
        self.color_activo = AZUL
        self.color = self.color_inactivo
        self.texto = texto
        self.texto_final = ''
        self.txt_surface = FUENTE.render(texto, True, self.color)
        self.activo = False

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.activo = not self.activo
            else:
                self.activo = False
            self.color = self.color_activo if self.activo else self.color_inactivo
        if evento.type == pygame.KEYDOWN:
            if self.activo:
                if evento.key == pygame.K_RETURN:
                    self.texto_final = self.texto
                elif evento.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                else:
                    self.texto += evento.unicode
                self.txt_surface = FUENTE.render(self.texto, True, self.color)

    def actualizar(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def dibujar(self, pantalla):
        pantalla.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(pantalla, self.color, self.rect, 2)


def input_jugadores(juego, modo):
    num_jugadores_box = InputBox(300, 250, 200, 40)
    nombre_jugadores_boxes = []
    continuar = [False]

    def agregar_nombre_jugadores():
        if num_jugadores_box.texto_final.isdigit():
            num_jugadores = int(num_jugadores_box.texto_final)
            for i in range(num_jugadores):
                nombre_jugadores_boxes.append(InputBox(300, 300 + i * 50, 200, 40))
            continuar[0] = True

    while not continuar[0]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()
            num_jugadores_box.manejar_evento(evento)
            if len(nombre_jugadores_boxes) > 0:
                for nombre_box in nombre_jugadores_boxes:
                    nombre_box.manejar_evento(evento)

        pantalla.fill(BLANCO)
        mostrar_titulo("Ingresar Jugadores", 300, 150)
        mostrar_texto("Número de jugadores", 300, 220)
        num_jugadores_box.actualizar()
        num_jugadores_box.dibujar(pantalla)
        if len(nombre_jugadores_boxes) > 0:
            for i, nombre_box in enumerate(nombre_jugadores_boxes):
                mostrar_texto(f"Jugador {i + 1}:", 300, 270 + (i * 50))
                nombre_box.actualizar()
                nombre_box.dibujar(pantalla)

        boton("Continuar", 300, 500, 200, 40, VERDE, AZUL, agregar_nombre_jugadores)
        pygame.display.flip()

    continuar[0] = False

    def confirmar_jugadores():
        nombres = [nombre_box.texto_final for nombre_box in nombre_jugadores_boxes]
        for nombre in nombres:
            juego.agregar_jugador(nombre)
        if modo == 'clasico':
            jugar_clasico(juego)
        else:
            input_valores_personalizados(juego, nombres)

    while not continuar[0]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()
            for nombre_box in nombre_jugadores_boxes:
                nombre_box.manejar_evento(evento)

        pantalla.fill(BLANCO)
        mostrar_titulo("Confirmar Jugadores", 300, 150)
        for i, nombre_box in enumerate(nombre_jugadores_boxes):
            mostrar_texto(f"Jugador {i + 1}:", 300, 270 + (i * 50))
            nombre_box.actualizar()
            nombre_box.dibujar(pantalla)

        boton("Confirmar", 300, 500, 200, 40, VERDE, AZUL, confirmar_jugadores)
        pygame.display.flip()


def input_valores_personalizados(juego, nombres):
    min_valor_box = InputBox(300, 200, 200, 40)
    max_valor_box = InputBox(300, 250, 200, 40)
    puntos_limite_box = InputBox(300, 300, 200, 40)
    continuar = [False]

    def confirmar_personalizado():
        min_valor = min_valor_box.texto_final
        max_valor = max_valor_box.texto_final
        puntos_limite = puntos_limite_box.texto_final
        if min_valor.isdigit() and max_valor.isdigit() and puntos_limite.isdigit():
            min_valor = int(min_valor)
            max_valor = int(max_valor)
            puntos_limite = int(puntos_limite)
            for nombre in nombres:
                juego.agregar_jugador(nombre)
            continuar[0] = True
            jugar_personalizado(juego, min_valor, max_valor, puntos_limite)

    while not continuar[0]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()
            min_valor_box.manejar_evento(evento)
            max_valor_box.manejar_evento(evento)
            puntos_limite_box.manejar_evento(evento)

        pantalla.fill(BLANCO)
        mostrar_titulo("Modo Personalizado", 300, 150)
        mostrar_texto("Valor mínimo del dado", 300, 180)
        min_valor_box.actualizar()
        min_valor_box.dibujar(pantalla)
        mostrar_texto("Valor máximo del dado", 300, 230)
        max_valor_box.actualizar()
        max_valor_box.dibujar(pantalla)
        mostrar_texto("Puntaje límite para ganar", 300, 280)
        puntos_limite_box.actualizar()
        puntos_limite_box.dibujar(pantalla)

        boton("Confirmar", 300, 350, 200, 40, VERDE, AZUL, confirmar_personalizado)
        pygame.display.flip()


def input_guardar(juego):
    archivo_box = InputBox(300, 300, 200, 40)

    def guardar():
        archivo = archivo_box.texto_final
        if archivo:
            juego.guardar_juego(archivo)
            main_menu()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()
            archivo_box.manejar_evento(evento)

        pantalla.fill(BLANCO)
        mostrar_titulo("Guardar Juego", 300, 150)
        mostrar_texto("Nombre del archivo", 300, 270)
        archivo_box.actualizar()
        archivo_box.dibujar(pantalla)
        boton("Guardar", 300, 350, 200, 40, VERDE, AZUL, guardar)
        pygame.display.flip()


def input_cargar(juego):
    archivo_box = InputBox(300, 300, 200, 40)

    def cargar():
        archivo = archivo_box.texto_final
        if archivo:
            juego.cargar_juego(archivo)
            main_menu()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()
            archivo_box.manejar_evento(evento)

        pantalla.fill(BLANCO)
        mostrar_titulo("Cargar Juego", 300, 150)
        mostrar_texto("Nombre del archivo", 300, 270)
        archivo_box.actualizar()
        archivo_box.dibujar(pantalla)
        boton("Cargar", 300, 350, 200, 40, VERDE, AZUL, cargar)
        pygame.display.flip()


def jugar_clasico(juego):
    while True:
        resultado = juego.jugar_clasico()
        if resultado:
            if isinstance(resultado, tuple):
                pregunta, jugador = resultado
                mostrar_pregunta(pregunta, jugador, juego, 'clasico')
            else:
                mostrar_resultado(resultado)


def jugar_personalizado(juego, min_valor, max_valor, puntos_limite):
    while True:
        resultado = juego.jugar_personalizado(min_valor, max_valor, puntos_limite)
        if resultado:
            if isinstance(resultado, tuple):
                pregunta, jugador = resultado
                mostrar_pregunta(pregunta, jugador, juego, 'personalizado', min_valor, max_valor, puntos_limite)
            else:
                mostrar_resultado(resultado)


def mostrar_pregunta(pregunta, jugador, juego, modo, min_valor=None, max_valor=None, puntos_limite=None):
    respuesta_box = InputBox(300, 300, 200, 40)
    continuar = [False]

    def confirmar_respuesta():
        respuesta = respuesta_box.texto_final
        if juego.verificar_respuesta(pregunta, respuesta):
            mostrar_texto("¡Correcto! No pierdes puntos.", 300, 400)
        else:
            jugador.puntos = 0
            mostrar_texto(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}", 300, 400)
        continuar[0] = True

    while not continuar[0]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()
            respuesta_box.manejar_evento(evento)

        pantalla.fill(BLANCO)
        mostrar_titulo("Pregunta", 300, 150)
        mostrar_texto(pregunta['pregunta'], 300, 200)
        for i, opcion in enumerate(pregunta['opciones']):
            mostrar_texto(f"{chr(97 + i)}) {opcion}", 300, 230 + (i * 30))
        mostrar_texto(f"{jugador.nombre}, ingresa tu respuesta:", 300, 270)
        respuesta_box.actualizar()
        respuesta_box.dibujar(pantalla)
        boton("Confirmar", 300, 350, 200, 40, VERDE, AZUL, confirmar_respuesta)
        pygame.display.flip()

    if modo == 'clasico':
        jugar_clasico(juego)
    else:
        jugar_personalizado(juego, min_valor, max_valor, puntos_limite)


def mostrar_resultado(mensaje):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()

        pantalla.fill(BLANCO)
        mostrar_titulo("Resultado del Juego", 300, 150)
        mostrar_texto(mensaje, 300, 250)
        boton("Volver al Menú Principal", 300, 350, 200, 40, VERDE, AZUL, main_menu)
        pygame.display.flip()


def cerrar_programa():
    pygame.quit()
    sys.exit()


def main_menu():
    juego = JuegoDeDados()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_programa()

        pantalla.fill(BLANCO)
        mostrar_titulo("Juego de Dados", 300, 50)
        boton("Jugar Clásico", 300, 150, 200, 40, VERDE, AZUL, lambda: input_jugadores(juego, 'clasico'))
        boton("Jugar Personalizado", 300, 200, 200, 40, VERDE, AZUL, lambda: input_jugadores(juego, 'personalizado'))
        boton("Guardar Juego", 300, 250, 200, 40, VERDE, AZUL, lambda: input_guardar(juego))
        boton("Cargar Juego", 300, 300, 200, 40, VERDE, AZUL, lambda: input_cargar(juego))
        boton("Salir", 300, 350, 200, 40, ROJO, AZUL, cerrar_programa)

        pygame.display.flip()


if __name__ == "__main__":
    main_menu()

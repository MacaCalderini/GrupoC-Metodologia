import pygame

ANCHO, ALTURA = 800, 800
FILAS, COLUMNAS = 6, 6

TAMANIO_CUADRADO = ANCHO//COLUMNAS

ROJO = (255, 105, 97)
BLANCO = (224, 176, 255)
NEGRO = (20, 20, 20)
GRIS = (128, 128, 128)
AZUL = (59, 131, 189)

#CORONA = imagen de la corona(buscar)

class Piezas:
    RELLENO = 15
    BORDE = 2

    def __init__(self, fil, col, color):
        self.fil = fil
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = TAMANIO_CUADRADO * self.col + TAMANIO_CUADRADO // 2
        self.y = TAMANIO_CUADRADO * self.fil + TAMANIO_CUADRADO // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radio = TAMANIO_CUADRADO // 2 - self.RELLENO
        pygame.draw.circle(win, GRIS, (self.x, self.y), radio + self.BORDE)
        pygame.draw.circle(win, self.color,(self.x, self.y), radio)
        if self.king:
            win.blit(CORONA, (self.x - CORONA.get_width()//2, self.y - CORONA.get_height()//2))

    def move(self, fil, col):
        self.fil = fil
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

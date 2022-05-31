import pygame
from constantes import TAMANIOCUADRADOTOTAL, GRIS, CORONA


class Piezas:
    RELLENO = 15
    BORDE = 2

    def __init__(self, filas, columnas, color):
        self.x = 0
        self.y = 0

        self.filas = filas
        self.columnas = columnas

        self.color = color
        self.king = False

        self.calcularPosicionX()
        self.calcularPosicionY()

    def __repr__(self):
        return str(self.color)


    def calcularPosicionX(self):
        self.x = TAMANIOCUADRADOTOTAL * self.columnas + TAMANIOCUADRADOTOTAL // 2

    def calcularPosicionY(self):
        self.y = TAMANIOCUADRADOTOTAL * self.filas + TAMANIOCUADRADOTOTAL // 2

    def mover(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
k
        self.calcularPosicionX()
        self.calcularPosicionY()


    def rey(self):
        self.rey = True

    def dibujo(self, ganar):
        radio = TAMANIOCUADRADOTOTAL // 2 - self.RELLENO

        pygame.dibujo.circle(ganar, GRIS, (self.x, self.y), radio + self.BORDE)
        pygame.dibujo.circle(ganar, self.color,(self.x, self.y), radio)

        if self.king:
            ganar.blit(CORONA, (self.x - CORONA.ancho()//2, self.y - CORONA.alto()//2))

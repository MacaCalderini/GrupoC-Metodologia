import pygame
from constantes import FILAS, COLUMNAS, TAMANIOCUADRADOTOTAL, NEGRO, VIOLETA, BLANCO
from piezas import Piezas


class Tablero:
    def init(self):
        self.tablero = []
        self.violetaIzq = self.blancoIzq = 12
        self.violetaRey = self.blancoRey = 0
        self.crearTablero()

    def crearCuadrado(self, ganar):
        ganar.fill(NEGRO)

        for filas in range(FILAS):
            for columnas in range(filas % 2, COLUMNAS, 2):
                pygame.draw.rect(ganar, VIOLETA, (
                    filas * TAMANIOCUADRADOTOTAL, columnas * TAMANIOCUADRADOTOTAL, TAMANIOCUADRADOTOTAL,
                    TAMANIOCUADRADOTOTAL))


    def crearTablero(self):
        for filas in range(FILAS):
            self.tablero.append([])

            for columnas in range(COLUMNAS):
                if columnas % 2 == ((filas + 1) % 2):
                    if filas < 3:
                        self.tablero[filas].append(Piezas(filas, columnas, BLANCO))
                    elif filas > 4:
                        self.tablero[filas].append(Piezas(filas, columnas, VIOLETA))
                    else:
                        self.tablero[filas].append(0)
                else:
                    self.tablero[filas].append(0)

    def moverFicha(self, pieza, filas, columnas):
        self.tablero[pieza.filas][pieza.columnas], self.tablero[filas][columnas] = self.tablero[filas][columnas], \
                                                                                   self.tablero[pieza.filas][
                                                                                       pieza.columnas]
        pieza.moverFicha(filas, columnas)

        if filas == FILAS - 1 or filas == 0:
            if pieza.color == BLANCO:
                self.blancoRey += 1
            else:
                self.violetaRey += 1

    def obtenerPiezas(self, filas, columnas):
        return self.tablero[filas][columnas]

    def dibujar(self, ganar):
        self.crearCuadrado(ganar)
        for filas in range(FILAS):
            for columnas in range(COLUMNAS):
                piezas = self.tablero[filas][columnas]
                if piezas != 0:
                    piezas.dibujo(ganar)

    def movimientosValidos(self, piezas):
        movimientos = {}

        izquierda = piezas.columnas - 1
        derecha = piezas.columnas + 1

        filas = piezas.filas

        if piezas.color == VIOLETA or piezas.rey:
            movimientos.update(self.atraIzq(filas - 1, max(filas - 3, -1), -1, piezas.color, izquierda))
            movimientos.update(self.atraDer(filas - 1, max(filas - 3, -1), -1, piezas.color, derecha))

        if piezas.color == BLANCO or piezas.king:
            movimientos.update(self.atraIzq(filas + 1, min(filas + 3, FILAS), 1, piezas.color, izquierda))
            movimientos.update(self.atraDer(filas + 1, min(filas + 3, FILAS), 1, piezas.color, derecha))
            return movimientos

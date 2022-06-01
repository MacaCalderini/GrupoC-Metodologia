import pygame
from piezas import Piezas


class Tablero: #Esta clase tablero sirve para manejar los movimientos de las piezas, las elimina, las pone en pantalla, etc
    def init(self):
        self.tablero = [] #Esto es para guardar objetos en un lista
        self.violetaIzq = self.blancoIzq = 12 #Cantidad de piezas en total
        self.violetaRey = self.blancoRey = 0

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

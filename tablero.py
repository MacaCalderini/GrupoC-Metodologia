import pygame
from constantes import FILAS, COLUMNAS, TAMANIOCUADRADOTOTAL, NEGRO, VIOLETA, BLANCO
from piezas import Piezas


class Tablero:
    def init(self):
        self.tablero = []
        self.violetaIzq = self.blancoIzq = 12
        self.violetaRey = self.blancoRey = 0

import pygame
from piezas import Piezas


class Tablero: #Esta clase tablero sirve para manejar los movimientos de las piezas, las elimina, las pone en pantalla, etc
    def init(self):
        self.tablero = [] #Esto es para guardar objetos en un lista
        self.violetaIzq = self.blancoIzq = 12 #Cantidad de piezas en total
        self.violetaRey = self.blancoRey = 0

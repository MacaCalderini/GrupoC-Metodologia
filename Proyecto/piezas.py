import pygame
from constantes import TAMANIOCUADRADOTOTAL, GRIS, CORONA


class Piezas:
    RELLENO = 15
    BORDE = 2

    def __init__(self, fil, col, color):#Metodo __init__ inicializara atributos que yo cree

        self.x = 0
        self.y = 0

        self.fil = fil
        self.col = col

        self.color = color
        self.king = False #Nos dice si la pieza es rey o no, si lo es cambia los movimientos

        self.calcularPosicion()

    def __repr__(self):#Esto sirve para depurar
        return str(self.color)


    def calcularPosicion(self): #Metodo para calcular posicion en Y(columnas)
        self.x = TAMANIOCUADRADOTOTAL * self.col + TAMANIOCUADRADOTOTAL // 2
        self.y = TAMANIOCUADRADOTOTAL * self.fil + TAMANIOCUADRADOTOTAL // 2 #Esto se tiene que hacer para que la pieza no se encuentre en la esquina o fuera del casillero, sino que queda en el medio del cuadrado


    def mover(self, fil, col): #Metodo para los movimientos de las fichas
        self.fil = fil
        self.col = col

        self.calcularPosicion()

    def make_king(self): #Metodo para transformar una ficha normal en rey, se hace cuando llega al final
        self.king = True

    def dibujo(self, ganar): #Este metodo dibuja las fichas
        radio = TAMANIOCUADRADOTOTAL // 2 - self.RELLENO #Se calcula el radio de las fichas, para que nos sean mas grandes que los casilleros

        pygame.draw.circle(ganar, GRIS, (self.x, self.y), radio + self.BORDE)
        pygame.draw.circle(ganar, self.color,(self.x, self.y), radio) #Se agrega un circulo con color, asi se resalta mas

        if self.king:
            ganar.blit(CORONA, (self.x - CORONA.get_width()//2, self.y - CORONA.get_height()//2)) #blit es para poner una imagen arriba de algo
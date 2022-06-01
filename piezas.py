import pygame
from constantes import TAMANIOCUADRADOTOTAL, GRIS, CORONA


class Piezas:
    RELLENO = 15
    BORDE = 2

    def __init__(self, filas, columnas, color):#Metodo __init__ inicializara atributos que yo cree

        self.x = 0
        self.y = 0

        self.filas = filas
        self.columnas = columnas

        self.color = color
        self.king = False #Nos dice si la pieza es rey o no, si lo es cambia los movimientos

        self.calcularPosicionX()
        self.calcularPosicionY()

    def __repr__(self):#Esto sirve para depurar
        return str(self.color)


    def calcularPosicionY(self): #Metodo para calcular posicion en Y(columnas)
        self.x = TAMANIOCUADRADOTOTAL * self.columnas + TAMANIOCUADRADOTOTAL // 2

    def calcularPosicionX(self):#Metodo para calcular posicion en X(filas)
        self.y = TAMANIOCUADRADOTOTAL * self.filas + TAMANIOCUADRADOTOTAL // 2 #Esto se tiene que hacer para que la pieza no se encuentre en la esquina o fuera del casillero, sino que queda en el medio del cuadrado


    def mover(self, filas, columnas): #Metodo para los movimientos de las fichas
        self.filas = filas
        self.columnas = columnas

        self.calcularPosicionX()
        self.calcularPosicionY()


    def rey(self): #Metodo para transformar una ficha normal en rey, se hace cuando llega al final
        self.rey = True

    def dibujo(self, ganar): #Este metodo dibuja las fichas
        radio = TAMANIOCUADRADOTOTAL // 2 - self.RELLENO #Se calcula el radio de las fichas, para que nos sean mas grandes que los casilleros

        pygame.dibujo.circle(ganar, GRIS, (self.x, self.y), radio + self.BORDE)
        pygame.dibujo.circle(ganar, self.color,(self.x, self.y), radio) #Se agrega un circulo con color, asi se resalta mas

        if self.king:
            ganar.blit(CORONA, (self.x - CORONA.ancho()//2, self.y - CORONA.alto()//2)) #blit es para poner una imagen arriba de algo

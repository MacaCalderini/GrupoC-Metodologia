import pygame

#Constantes
FILAS, COLUMNAS = 8, 8
YINICIAL = 0
XINICIAL = 0


COLORFONDO = (53, 150, 80)
NUMJUGADORES = 2

TAMANIOANCHO, TAMANIOALTO = 496, 496
ANCHO, ALTO = 720, 640
NUMEROPIEZAS = 8

#Se carga las imagenes de las piezasm, del tablero y de las piezas con corona, por defecto la imagen es grande, entonces se le da un tamaño para que entre en las piezas
CORONABLANCA = pygame.transform.scale(pygame.image.load("blancoRey.png"), (44, 25))
CORONANEGRA = pygame.transform.scale(pygame.image.load("negroRey.png"), (44, 25))

#FRAME = pygame.image.load('frame.png')


PIEZANEGRA = pygame.transform.scale(pygame.image.load("negro.png"), (44, 25))
PIEZABLANCA = pygame.transform.scale(pygame.image.load("blanco.png"), (44, 25))

TABLERO = pygame.image.load("tablero.png")




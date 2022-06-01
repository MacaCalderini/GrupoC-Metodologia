import pygame

#Constantes
FILAS, COLUMNAS = 8, 8
ANCHO, ALTURA = 800, 800

#Se carga la imagen de la corona, por defecto la imagen es grande, entonces se le da un tamaño para que entre en las piezas
CORONA = pygame.transform.scale(pygame.image.load("corona.png"), (44, 25))

#Se le da un tamaño al tablero
TAMANIOCUADRADOTOTAL = ANCHO//COLUMNAS

#Colores RGB que se usaran
VIOLETA = (38, 43, 26)

BLANCO = (224, 176, 255)

NEGRO = (20, 20, 20)

GRIS = (128, 128, 128)

AZUL = (59, 131, 189)


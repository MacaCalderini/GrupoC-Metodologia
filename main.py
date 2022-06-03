import pygame
from constantes import ANCHO, ALTURA, TAMANIOCUADRADOTOTAL
from juego import  Juego

pygame.display.set_caption('Mundamitas')#Nombre del juego


FPS = 60 #Fotogramas por segundo, no se puso en las constantes porque se puede renderizar y darle forma al juego
WIN = pygame.display.set_mode((ANCHO, ALTURA)) #Se elige el ancho y el alto

def posicionMouse(posicion): #Se toma la posicion del mouse
    x, y = posicion #Esto te dice en que fila y en que columna nos encontramos
    fil = y // TAMANIOCUADRADOTOTAL #Si el TC es 100, "y" esta en 650, entonces nos encontramos en la fila 6
    col = x // TAMANIOCUADRADOTOTAL #Lo mismo pero con "x" o sea, en columnas
    return fil, col

def main(): #Aca se ejecuta el juego
    run = True #Bucle de eventos
    clock = pygame.time.Clock() #Esto es para que el juego no se ejecute ni muy rapido, ni muy lento
    game = Juego(WIN)

    while run:
        clock.tick(FPS)

        if game.ganador() != None:
            print(game.ganador())
            run = False

        for event in pygame.event.get(): #Esto comprueba que esta pasando en el juego
            if event.type == pygame.QUIT: #Opcion para cerrar el juego
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: #Esto quiere decir que tiene que presionar una tecla del mouse, es para saber si se esta moviendo, si toque otra pieza de color, los turnos, etc
                pos = pygame.mouse.get_pos()
                fil, col = posicionMouse(pos)
                game.seleccionar(fil, col)

        game.actualizar() #Se va actualizando el juego

    pygame.quit()


main()

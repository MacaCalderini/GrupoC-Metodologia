import pygame

pygame.display.set_caption('Mundamitas')

FPS = 60
WIN = pygame.display.set_mode((ANCHO, ALTURA))

def filasColumnas(posicion):
    x, y = posicion
    filas = y // TAMANIOCUADRADOTOTAL
    columnas = x // TAMANIOCUADRADOTOTAL
    return filas, columnas

def main():
    run = True
    clock = pygame.time.Clock()
    game = Juego(WIN)

    while run:
        clock.tick(FPS)

        if game.ganador() != None:
            print(game.ganador())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fil, col = filasColumnas(pos)
                game.select(fil, col)

        game.update()

    pygame.quit()
    print("                s   ")
main()
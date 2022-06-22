import pygame, sys
from constantes import *
from server import Server
import cliente as cl

pygame.init()
pygame.display.set_caption('Mundamitas')#Nombre del juego
#coment
# constantes
WIDTH = 800
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font(None, 32)
Lfont = pygame.font.Font(None, 96)
Mfont = pygame.font.Font(None, 60)
# colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

FPS = 60 #Fotogramas por segundo, no se puso en las constantes porque se puede renderizar y darle forma al juego
WIN = pygame.display.set_mode((790, 720)) #Se elige el ancho y el alto

def menu():
    #Definicion de las variables de texto del menu y dimensionamiento
    titulo_menu = Lfont.render("MUNDAMITAS", True, green)
    titulo_menu_dim = titulo_menu.get_rect()
    titulo_menu_dim.center = (WIDTH // 2, HEIGHT // 2 - 200)

    quit_text = FONT.render("Quit", True, white)
    quit_text_dim = quit_text.get_rect()
    quit_text_dim.center = (WIDTH // 2, HEIGHT // 2 + 230)

    play_text = FONT.render("Play", True, white)
    play_text_dim = play_text.get_rect()
    play_text_dim.center = (WIDTH // 2, HEIGHT // 2 + 130)

    fixture_text = FONT.render("Fixture", True, white)
    fixture_text_dim = fixture_text.get_rect()
    fixture_text_dim.center = (WIDTH // 2, HEIGHT // 2 + 180)

    back_text = FONT.render("Back", True, white)
    back_text_dim = back_text.get_rect()
    back_text_dim.center = (WIDTH // 2, HEIGHT // 2 + 200)

    # loop del menu
    run = True
    while run:
        #Pantalla en negro
        SCREEN.fill(black)
        # display del texto
        SCREEN.blit(titulo_menu, titulo_menu_dim)
        SCREEN.blit(play_text, play_text_dim)
        SCREEN.blit(quit_text, quit_text_dim)
        SCREEN.blit(fixture_text, fixture_text_dim)

        #Se escuchan los eventos y se redirige a la funcion de la opcion seleccionada
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #En el caso de cerrarse por el icono de la ventana, se cierra la libreria y el programa
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_text_dim.collidepoint(event.pos):
                    cl.main()
                if fixture_text_dim.collidepoint(event.pos):
                    import creaciontxt
                if quit_text_dim.collidepoint(event.pos): #Si se selecciona la opcion Quit el programa acaba
                    pygame.quit() #Se cierra la libreria
                    sys.exit()    #Se cierra el programa
        pygame.display.update()


menu()
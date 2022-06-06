import pygame, sys

pygame.init()

# constantes
WIDTH = 1080
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font(None, 32)
Lfont = pygame.font.Font(None, 96)
Mfont = pygame.font.Font(None, 60)
# colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)

def play():
    play()

def fixture():
    fixture()


def menu():

    #Definicion de las variables de texto del menu y dimensionamiento
    titulo_menu = Lfont.render("MUNDAMITAS", True, red)
    titulo_menu_dim = titulo_menu.get_rect()
    titulo_menu_dim.center = (WIDTH // 2, HEIGHT // 2 - 200)

    quit_text = FONT.render("Quit", True, green)
    quit_text_dim = quit_text.get_rect()
    quit_text_dim.center = (WIDTH // 2, HEIGHT // 2 + 250)

    play_text = FONT.render("Play", True, green)
    play_text_dim = play_text.get_rect()
    play_text_dim.center = (WIDTH // 2, HEIGHT // 2 + 150)

    fixture_text = FONT.render("Fixture", True, green)
    fixture_text_dim = fixture_text.get_rect()
    fixture_text_dim.center = (WIDTH // 2, HEIGHT // 2 + 200)

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
                #f play_text_dim.collidepoint(event.pos):
                    #play()
                #if fixture_text_dim.collidepoint(pygame.mouse.get_pos()):
                    #fixture()
                if quit_text_dim.collidepoint(event.pos): #Si se selecciona la opcion Quit el programa acaba
                    pygame.quit() #Se cierra la libreria
                    sys.exit()    #Se cierra el programa
        pygame.display.update()


menu()
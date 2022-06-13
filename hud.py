import pygame
#
class Hud:
    XOFF, YOFF = 0, 0 #Intentar cambiar por constantes

    def __init__(self, sAncho, sAlto, tabAncho, tabAlto, jugador):
        self.sAncho = sAncho
        self.sAlto = sAlto
        self.tabAncho = tabAncho
        self.tabAlto = tabAlto
        self.blanco = jugador.blanco

    def dibujarJugadores(self, win, tablero):
        font = pygame.font.SysFont(None, 50)
        esqSupIzquierda = tablero.rect[0]

        j2x, j2y = self.sAncho // 2, esqSupIzquierda[1] // 2
        j1x, j1y = self.sAncho // 2, esqSupIzquierda[1] + self.tabAlto + esqSupIzquierda[1] // 2
        j2txt = font.render('Jugador 1', True, (0, 0, 0))
        j1txt = font.render('Jugador 2', True, (0, 0, 0))

        j2w = j2txt.get_width()
        j2h = j2txt.get_height()
        j1w = j1txt.get_width()
        j1h = j1txt.get_height()

        j2x -= j2w // 2
        j2y -= j2h // 2
        j1x -= j1w // 2
        j1y -= j1h // 2

        win.blit(j2txt, (j2x, j2y))
        win.blit(j1txt, (j1x, j1y))

    def dibujarCapturadas(self, win, tablero):
        imgBlanca = pygame.image.load('blanco.png')#Intentar cambiar por constantes
        imgNegra = pygame.image.load('negro.png')#Intentar cambiar por constantes
        bxoff, byoff = tablero.rect[0]
        x1, x2, y_init = bxoff // 2 - 31, int(bxoff * (3/2)) + self.tabAncho - 31, byoff
        y_inc = self.tabAlto // 16

        for i in range(max(tablero.piezaBlanca, tablero.piezaNegra)):
            if i < tablero.piezaBlanca:
                win.blit(imgBlanca, (x1, y_init))
            if i < tablero.piezaNegra:
                win.blit(imgNegra, (x2, y_init))
            y_init += y_inc

    def dibujarTurnos(self):
        pass

    def dibujar(self, win, tablero):
        self.dibujarJugadores(win, tablero)
        self.dibujarCapturadas(win, tablero)
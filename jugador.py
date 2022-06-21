import pygame
from piezatablero import *
#Class Jugador

class Jugador:
    def __init__(self, blanco):
        self.connected = False
        self.blanco = blanco
        self.esTurno = True if self.blanco else False
        self.piezaBloqueada = None
        self.movPosiblesBloqueados = []
        self.piezasMovidas = None
        self.piezaComida = []
        self.posMovida = None
        self.anim_move_ri = 0
        self.anim_move_ri_built = 0
        self.anim_move_r = [6, 7, 8, 9, 10, 11, 10, 9, 8, 7]
        self.revancha = False

    def controlMov(self, tablero, posMouse):
        x, y = posMouse
        tr, tc = y // tablero.cell_h, x // tablero.cell_w
        legal, kills = self.movLegal((tr, tc))

        if legal:
            self.piezaComida = kills
            self.piezasMovidas = self.piezaBloqueada
            self.posMovida = (tr, tc)
            self.piezaBloqueada = None
            self.movPosiblesBloqueados = []

    def controlClicks(self, tablero, posMouse):
        if not self.esTurno:
            return

        pieza = self.obtPiezaClick(tablero, posMouse)

        if pieza is not None:
            self.controlBloqueada(tablero, pieza)
        elif self.piezaBloqueada is not None:
            self.controlMov(tablero, posMouse)

    def controlBloqueada(self, tablero, pieza):
        self.piezaBloqueada = pieza
        self.movPosiblesBloqueados = pieza.movPosibles(tablero)

    def bloqAnim(self, win, tablero, sp=0.15):
        r = int(self.anim_move_r[self.anim_move_ri])

        self.dibujarPosiblesMov(win, tablero, r)
        self.anim_move_ri_built = (self.anim_move_ri_built + sp) % (1 + sp)
        self.anim_move_ri = (self.anim_move_ri + int(self.anim_move_ri_built)) % len(self.anim_move_r)

    def bloqDibujar(self, win, tablero):
        if self.piezaBloqueada is not None:
            self.bloqAnim(win, tablero)

    def obtPiezas(self, tablero):
        return [pieza for pieza in tablero.piezas if pieza.blanco is self.blanco]

    def obtPiezaClick(self, tablero, posMouse):
        x, y = posMouse
        r, c = y // tablero.cell_h, x // tablero.cell_w

        for pieza in self.obtPiezas(tablero):
            if pieza.pos == (r, c) and not pieza.cap:
                return pieza
        return None

    def dibujarPosiblesMov(self, win, tablero, r):
        xoff, yoff = tablero.rect[0]

        if self.piezaBloqueada is None:
            return
        else:
            pos = self.piezaBloqueada.pos
            for move in self.movPosiblesBloqueados:
                for to_pos in move['a']:
                    w, h = r, r
                    tr, tc = to_pos
                    tx, ty = tc * tablero.cell_w + tablero.cell_w//2 - w//2, tr * tablero.cell_h + tablero.cell_h//2 - h//2
                    rect = pygame.rect.Rect(tx + xoff, ty + yoff, w, h)
                    pygame.draw.rect(win, (53, 150, 80), rect, 0)

    def movLegal(self, to_pos):
        for move in self.movPosiblesBloqueados:
            if move['a'] and to_pos == move['a'][-1]:
                return True, move['comer']
        return False, None

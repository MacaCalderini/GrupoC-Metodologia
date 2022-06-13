import pygame

class Pieza:
    def __init__(self, blanco, is_king, pos, cap=False):
        self.blanco = blanco
        self.is_king = is_king
        self.cap = cap
        self.pos = pos

    def obtImagen(self):
        if self.blanco:
            if self.is_king:
                return 'blancoRey.png'#Intentar cambiar por constantes
            else:
                return 'blanco.png'#Intentar cambiar por constantes
        else:
            if self.is_king:
                return 'negroRey.png'#Intentar cambiar por constantes
            else:
                return 'negro.png'#Intentar cambiar por constantes

    def obtPosiDiagonales(self, tablero):
        r, c = self.pos
        pos = []

        if r > 0:
            if c > 0:
                pos.append((r - 1, c - 1))
            if c < 7:
                pos.append((r - 1, c + 1))
        if self.is_king and r < 7:
            if c > 0:
                pos.append((r + 1, c - 1))
            if c < 7:
                pos.append((r + 1, c + 1))
        return pos

    def obtEliminadas(self, tablero, from_pos, to_pos, vis):
        pieza = tablero.tablero[to_pos]

        if isinstance(pieza, Pieza) and pieza.blanco is not self.blanco and to_pos not in vis:
            vis.add(to_pos)
            skip_pos = (to_pos[0] + (to_pos[0] - from_pos[0]), to_pos[1] + (to_pos[1] - from_pos[1]))
            if skip_pos not in tablero.tablero:
                return [], []
            if (tablero.tablero[skip_pos] is None or tablero.tablero[skip_pos].cap) and skip_pos not in vis:
                vis.add(skip_pos)
                pieza_copy = Pieza(self.blanco, self.is_king, skip_pos)
                diag_moves = pieza_copy.obtPosiDiagonales(tablero)
                possible_paths = []
                possible_kills = []
                for tpos in diag_moves:
                    path, kills = pieza_copy.obtEliminadas(tablero, skip_pos, tpos, vis)
                    possible_paths.append(path)
                    possible_kills.append(kills)
                trace = [skip_pos] + max(possible_paths, key=lambda x: len(x)) if possible_paths else [skip_pos]
                kills = [pieza] + max(possible_kills, key=lambda x: len(x)) if possible_kills else [pieza]
                return trace, kills
            else:
                return [], []
        else:
            return [], []

    def movPosibles(self, tablero):
        b = tablero.tablero
        moves = []
        r, c = self.pos

        for to_pos in self.obtPosiDiagonales(tablero):
            if b[to_pos] is None or b[to_pos].cap:
                moves.append({'a': [to_pos], 'comer': []})
            elif isinstance(b[to_pos], Pieza) and b[(r, c)].blanco is not b[to_pos].blanco:
                path, kills = self.obtEliminadas(tablero, self.pos, to_pos, {self.pos})
                move = {'a': path, 'comer': kills}
                moves.append(move)
        return moves

    def dibujar(self, win, cell_w, cell_h, xoff, yoff):
        if not self.cap:
            path = self.obtImagen()
            img = pygame.image.load(path)
            r, c = self.pos
            x, y = c * cell_w + 1, r * cell_h + 1
            w, h = cell_w - 2, cell_h - 2
            win.blit(img, (x + xoff, y + yoff))


class Tablero:
    IMG_PATH = "tablero.png"#Intentar cambiar por constantes!
    NUM_PLAYER_PIECES = 8

    def __init__(self, sw, sh, w, h, tablero=None, piezas=None, piezaBlanca=0, piezaNegra=0):
        self.sw, self.sh = sw, sh
        self.w, self.h = w, h
        self.cell_w, self.cell_h = w // 8, h // 8
        self.piezas = set() if piezas is None else piezas
        self.tablero = self.initTablero() if tablero is None else tablero
        self.piezaBlanca, self.piezaNegra = piezaBlanca, piezaNegra
        self.rect = self.obtTablero()

    def initTablero(self):
        if self.piezas:
            raise("Error con el tablero, revise la configuracion")
        tablero = {}
        for r in range(8):
            for c in range(8):
                if r == 0 and c % 2 == 0 or r == 1 and c % 2 == 1:
                    pieza = Pieza(False, False, (r, c))
                    tablero[(r, c)] = pieza
                    self.piezas.add(pieza)
                elif r == 6 and c % 2 == 0 or r == 7 and c % 2 == 1:
                    pieza = Pieza(True, False, (r, c))
                    tablero[(r, c)] = pieza
                    self.piezas.add(pieza)
                else:
                    tablero[(r, c)] = None
        return tablero

    def numComidas(self):
        rct, bct = 0, 0

        for pieza in self.piezas:
            if pieza.blanco and pieza.cap:
                rct += 1
            if not pieza.blanco and pieza.cap:
                bct += 1

    def obtTablero(self):
        topleft = ((self.sw - self.w) // 2, (self.sh - self.h) // 2)
        topright = (topleft[0] + self.w, (self.sh - self.h) // 2)
        botleft = (topleft[0], topright[0] + self.h)
        botright = (topright[0], botleft[1])
        return (topleft, topright, botleft, botright)

    def obtCompPosicion(self, pos):
        return (7 - pos[0], 7 - pos[1])

    def reversa(self):
        tablero = {}
        piezas = set()

        for r, c in self.tablero:
            comp_pos = (7-r, 7-c)
            pieza = self.tablero[(r, c)]
            if isinstance(pieza, Pieza):
                comp_pieza = Pieza(pieza.blanco, pieza.is_king, comp_pos, pieza.cap)
                tablero[comp_pos] = comp_pieza
                piezas.add(comp_pieza)
            else:
                tablero[comp_pos] = None
        return Tablero(self.sw, self.sh, self.w, self.h, tablero, piezas, self.piezaBlanca, self.piezaNegra)

    def moverPieza(self, from_pos, to_pos, comp=False):
        if comp:
            actual_from = self.obtCompPosicion(from_pos)
            actual_to = self.obtCompPosicion(to_pos)
            pieza = self.tablero[actual_from]
            self.tablero[actual_from] = None
            pieza.pos = actual_to
            self.tablero[actual_to] = pieza
        else:
            pieza = self.tablero[from_pos]
            self.tablero[from_pos] = None
            pieza.pos = to_pos
            self.tablero[to_pos] = pieza

    def dibujarPanel(self, win):
        frame_img = pygame.image.load('borde.png')#Intentar cambiar por constantes
        fw = 12
        bxoff, byoff = self.rect[0]
        win.blit(frame_img, (bxoff - fw, byoff - fw))

    def dibujar(self, win):
        self.dibujarPanel(win)

        img = pygame.image.load(self.IMG_PATH)
        topleft = self.rect[0]
        xoff, yoff = topleft
        win.blit(img, (xoff, yoff))

        for pieza in self.piezas:
            pieza.dibujar(win, self.cell_w, self.cell_h, xoff, yoff)

    def piezaComida(self, pos, comp=False):
        if comp:
            actual_pos = self.obtCompPosicion(pos)
            pieza = self.tablero[actual_pos]
            if pieza.blanco:
                self.piezaBlanca += 1
            else:
                self.piezaNegra += 1
            self.tablero[actual_pos] = None
            pieza.cap = True
        else:
            pieza = self.tablero[pos]
            if pieza.blanco:
                self.piezaBlanca += 1
            else:
                self.piezaNegra += 1
            self.tablero[pos] = None
            pieza.cap = True

    def esFin(self):
        return self.piezaBlanca >= self.NUM_PLAYER_PIECES or self.piezaNegra >= self.NUM_PLAYER_PIECES

    def obtGanador(self):
        return 'blanco' if self.piezaNegra >= self.NUM_PLAYER_PIECES else 'negro'

def actualizarRey(tablero):
    for pos in tablero.tablero:
        pieza = tablero.tablero[pos]
        if isinstance(pieza, Pieza):
            if pieza.blanco and pieza.pos[0] == 0:
                pieza.is_king = True
            elif not pieza.blanco and pieza.pos[0] == 7:
                pieza.is_king = True

def revisarGanador(tablero):
    if tablero.esFin():
        return tablero.obtGanador()

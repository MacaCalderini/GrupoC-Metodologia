import pygame
from constantes import FILAS, COLUMNAS, TAMANIOCUADRADOTOTAL, NEGRO, VIOLETA, BLANCO
from piezas import Piezas


class Tablero:
    def init(self):
        self.tablero = []
        self.violetaIzq = self.blancoIzq = 12
        self.violetaRey = self.blancoRey = 0
        self.crearTablero()

    def crearCuadrado(self, ganar):
        ganar.fill(NEGRO)

        for fil in range(FILAS):
            for col in range(fil % 2, COLUMNAS, 2):
                pygame.draw.rect(ganar, VIOLETA, (
                    fil * TAMANIOCUADRADOTOTAL, col * TAMANIOCUADRADOTOTAL, TAMANIOCUADRADOTOTAL,
                    TAMANIOCUADRADOTOTAL))


    def crearTablero(self):
        for fil in range(FILAS):
            self.tablero.append([])

            for col in range(COLUMNAS):
                if col % 2 == ((fil + 1) % 2):
                    if fil < 3:
                        self.tablero[fil].append(Piezas(fil, col, BLANCO))
                    elif fil > 4:
                        self.tablero[fil].append(Piezas(fil, col, VIOLETA))
                    else:
                        self.tablero[fil].append(0)
                else:
                    self.tablero[fil].append(0)

    def moverFicha(self, pieza, fil, col):
        self.tablero[pieza.fil][pieza.col], self.tablero[fil][col] = self.tablero[fil][col], \
                                                                     self.tablero[pieza.fil][
                                                                         pieza.col]
        pieza.moverFicha(fil, col)

        if fil == FILAS - 1 or fil == 0:
            if pieza.color == BLANCO:
                self.blancoRey += 1
            else:
                self.violetaRey += 1

    def obtenerPiezas(self, fil, col):
        return self.tablero[fil][col]

    def dibujar(self, ganar):
        self.crearCuadrado(ganar)
        for fil in range(FILAS):
            for col in range(COLUMNAS):
                piezas = self.tablero[fil][col]
                if piezas != 0:
                    piezas.dibujo(ganar)

    def movimientosValidos(self, piezas):
        movimientos = {}

        izquierda = piezas.col - 1
        derecha = piezas.col + 1

        fil = piezas.fil

        if piezas.color == VIOLETA or piezas.rey:
            movimientos.update(self.atraIzq(fil - 1, max(fil - 3, -1), -1, piezas.color, izquierda))
            movimientos.update(self.atraDer(fil - 1, max(fil - 3, -1), -1, piezas.color, derecha))

        if piezas.color == BLANCO or piezas.king:
            movimientos.update(self.atraIzq(fil + 1, min(fil + 3, FILAS), 1, piezas.color, izquierda))
            movimientos.update(self.atraDer(fil + 1, min(fil + 3, FILAS), 1, piezas.color, derecha))
            return movimientos

    def atraIzq(self, empezar, parar, paso, color, izquierda, skipped=[]):
        movimientos = {}
        ultimo = []
        for i in range(empezar, parar, paso):
            if izquierda < 0:
                break

            actual = self.tablero[i][izquierda]
            if actual == 0:
                if skipped and not ultimo:
                    break
                elif skipped:
                    movimientos[(i, izquierda)] = ultimo + skipped
                else:
                    movimientos[(i, izquierda)] = ultimo
                if ultimo:
                    if paso == -1:
                        fil = max(i - 3, 0)
                    else:
                        fil = min(i + 3, FILAS)
                    movimientos.update(self.atraIzq(i + paso, fil, paso, color, izquierda - 1, skipped=ultimo))
                    movimientos.update(self.atraDer(i + paso, fil, paso, color, izquierda + 1, skipped=ultimo))
                break
            elif actual.color == color:
                break
            else:
                ultimo = [actual]
            izquierda -= 1
        return movimientos

    def atraDer(self, empezar, parar, paso, color, derecha, skipped=[]):
        movimientos = {}
        ultimo = []
        for i in range(empezar, parar, paso):
            if derecha >= COLUMNAS:
                break

            actual = self.tablero[i][derecha]
            if actual == 0:
                if skipped and not ultimo:
                    break
                elif skipped:
                    movimientos[(i, derecha)] = ultimo + skipped
                else:
                    movimientos[(i, derecha)] = ultimo
                if ultimo:
                    if paso == -1:
                        fil = max(i - 3, 0)
                    else:
                        fil = min(i + 3, FILAS)
                    movimientos.update(self.atraIzq(i + paso, fil, paso, color, derecha - 1, skipped=ultimo))
                    movimientos.update(self.atraDer(i + paso, fil, paso, color, derecha + 1, skipped=ultimo))
                break
            elif actual.color == color:
                break
            else:
                ultimo = [actual]
            derecha += 1

        return movimientos

    def eliminar(self, piezass):
        for pieza in piezass:
            self.tablero[pieza.fil][pieza.col] = 0
            if pieza != 0:
                if pieza != 0:
                    if pieza.color == VIOLETA:
                        self.violetaIzq -= 1
                    else:
                        self.blancoIzq -= 1

    def ganador(self):
        if self.violetaIzq <= 0:
            return BLANCO
        elif self.blancoIzq <= 0:
            return VIOLETA
        return None

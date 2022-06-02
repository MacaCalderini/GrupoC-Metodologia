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

        for filas in range(FILAS):
            for columnas in range(filas % 2, COLUMNAS, 2):
                pygame.draw.rect(ganar, VIOLETA, (
                    filas * TAMANIOCUADRADOTOTAL, columnas * TAMANIOCUADRADOTOTAL, TAMANIOCUADRADOTOTAL,
                    TAMANIOCUADRADOTOTAL))


    def crearTablero(self):
        for filas in range(FILAS):
            self.tablero.append([])

            for columnas in range(COLUMNAS):
                if columnas % 2 == ((filas + 1) % 2):
                    if filas < 3:
                        self.tablero[filas].append(Piezas(filas, columnas, BLANCO))
                    elif filas > 4:
                        self.tablero[filas].append(Piezas(filas, columnas, VIOLETA))
                    else:
                        self.tablero[filas].append(0)
                else:
                    self.tablero[filas].append(0)

    def moverFicha(self, pieza, filas, columnas):
        self.tablero[pieza.filas][pieza.columnas], self.tablero[filas][columnas] = self.tablero[filas][columnas], \
                                                                                   self.tablero[pieza.filas][
                                                                                       pieza.columnas]
        pieza.moverFicha(filas, columnas)

        if filas == FILAS - 1 or filas == 0:
            if pieza.color == BLANCO:
                self.blancoRey += 1
            else:
                self.violetaRey += 1

    def obtenerPiezas(self, filas, columnas):
        return self.tablero[filas][columnas]

    def dibujar(self, ganar):
        self.crearCuadrado(ganar)
        for filas in range(FILAS):
            for columnas in range(COLUMNAS):
                piezas = self.tablero[filas][columnas]
                if piezas != 0:
                    piezas.dibujo(ganar)

    def movimientosValidos(self, piezas):
        movimientos = {}

        izquierda = piezas.columnas - 1
        derecha = piezas.columnas + 1

        filas = piezas.filas

        if piezas.color == VIOLETA or piezas.rey:
            movimientos.update(self.atraIzq(filas - 1, max(filas - 3, -1), -1, piezas.color, izquierda))
            movimientos.update(self.atraDer(filas - 1, max(filas - 3, -1), -1, piezas.color, derecha))

        if piezas.color == BLANCO or piezas.king:
            movimientos.update(self.atraIzq(filas + 1, min(filas + 3, FILAS), 1, piezas.color, izquierda))
            movimientos.update(self.atraDer(filas + 1, min(filas + 3, FILAS), 1, piezas.color, derecha))
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
                        filas = max(i - 3, 0)
                    else:
                        filas = min(i + 3, FILAS)
                    movimientos.update(self.atraIzq(i + paso, filas, paso, color, izquierda - 1, skipped=ultimo))
                    movimientos.update(self.atraDer(i + paso, filas, paso, color, izquierda + 1, skipped=ultimo))
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
                        filas = max(i - 3, 0)
                    else:
                        filas = min(i + 3, FILAS)
                    movimientos.update(self.atraIzq(i + paso, filas, paso, color, derecha - 1, skipped=ultimo))
                    movimientos.update(self.atraDer(i + paso, filas, paso, color, derecha + 1, skipped=ultimo))
                break
            elif actual.color == color:
                break
            else:
                ultimo = [actual]
            derecha += 1

        return movimientos

    def eliminar(self, piezass):
        for pieza in piezass:
            self.tablero[pieza.filas][pieza.columnas] = 0
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

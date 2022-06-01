import pygame
from tablero import Tablero
from constantes import ROJO, BLANCO, AZUL, TAMANIOCUADRADOTOTAL


class Juego:
    def __init__(self, ganar):
        self._init()
        self.ganar = ganar
        
    def _init(self):
        self.selected = None
        self.tablero = Tablero()
        self.turn = ROJO
        self.movimientosValidos = {}

    def dibujarMovimientos(self, movimientos):
        for mover in movimientos:
            filas, columnas = mover
            pygame.draw.circle(self.win, AZUL, (columnas * TAMANIOCUADRADOTOTAL +
                                                TAMANIOCUADRADOTOTAL//2, filas * TAMANIOCUADRADOTOTAL +
                                                TAMANIOCUADRADOTOTAL//2), 15)

    def _mover(self, filas, columnas):
        pieza = self.tablero.get_pieza(filas, columnas)
        if self.selected and pieza == 0 and (filas, columnas) in self.movimientosValidos:
            self.tablero.mover(self.selected, filas, columnas)
            skipped = self.movimientosValidos[(filas, columnas)]
            if skipped:
                self.tablero.eliminar(skipped)
            self.cambioTurno()
        else:
            return False
        return True

    def seleccionar(self, filas, columnas):
        if self.selected:
            result = self._move(filas, columnas)
            if not result:
                self.selected = None
                self.seleccionar(filas, columnas)

        pieza = self.tablero.ObtPiezas(filas, columnas)
        if pieza != 0 and pieza.color == self.turn:
            self.selected = pieza
            self.movimientosValidos = self.tablero.obtMovimientosValidos(pieza)
            return True
        return False

    def cambioTurno(self):
        self.movimientosValidos = {}
        if self.turn == ROJO:
            self.turn = BLANCO
        else:
            self.turn = ROJO

    def actualizar(self):
        self.tablero.dibujar(self.ganar)
        self.dibujarMovimientos(self.movimientosValidos)
        pygame.display.update()

    def ganador(self):
        return self.tablero.ganador()

    def reiniciar(self):
        self._init()

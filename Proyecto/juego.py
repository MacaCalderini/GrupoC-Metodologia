import pygame
from tablero import Tablero
from Proyecto.constantes import VIOLETA, BLANCO, AZUL, TAMANIOCUADRADOTOTAL


class Juego: #Aca se maneja el juego, la seleccion de piezas, a donde me puedo mover, de quien es el turno
    def __init__(self, ganar):
        self._init() #Sirve para el metodo de reinicio
        self.ganar = ganar

    def _init(self):
        self.selected = None
        self.tablero = Tablero()
        self.turn = VIOLETA #De quien es el turno
        self.movimientosValidos = {}

    def dibujarMovimientos(self, movimientos):
        for mover in movimientos: #Dibuja movimientos posibles
            fil, col = mover
            pygame.draw.circle(self.ganar, AZUL, (col * TAMANIOCUADRADOTOTAL +
                                                  TAMANIOCUADRADOTOTAL//2, fil * TAMANIOCUADRADOTOTAL +
                                                  TAMANIOCUADRADOTOTAL//2), 15)

    def _mover(self, fil, col): #Movimiento de las fichas y se llama al metodo cambioTurno una vez realizado el movimiento
        pieza = self.tablero.obtenerPiezas(fil, col)
        if self.selected and pieza == 0 and (fil, col) in self.movimientosValidos:
            self.tablero.mover(self.selected, fil, col)
            skipped = self.movimientosValidos[(fil, col)]
            if skipped:
                self.tablero.eliminar(skipped)
            self.cambioTurno()
        else:
            return False

        return True

    def seleccionar(self, fil, col):
        if self.selected:
            result = self._mover(fil, col) #Se mueve lo que se seleccione
            if not result:
                self.selected = None
                self.seleccionar(fil, col)

        pieza = self.tablero.obtenerPiezas(fil, col)
        if pieza != 0 and pieza.color == self.turn:
            self.selected = pieza
            self.movimientosValidos = self.tablero.movimientosValidos(pieza)
            return True
        return False

    def cambioTurno(self): #Cambia el turnp
        self.movimientosValidos = {}
        if self.turn == VIOLETA:
            self.turn = BLANCO
        else:
            self.turn = VIOLETA

    def actualizar(self): #Actualiza la pantalla
        self.tablero.dibujar(self.ganar)
        self.dibujarMovimientos(self.movimientosValidos)
        pygame.display.update()

    def ganador(self): #Elige ganador de la partida
        return self.tablero.ganador()

    def reiniciar(self): #Se reinicia el juego
        self._init()

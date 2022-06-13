import sys
import socket
import pickle
import _thread
from jugador import *
from piezatablero import *

SWIDTH, SHEIGHT = 720, 640
WIDTH, HEIGHT = 496, 496

def actualizarInfoJugador(server, player, uplayer):
    player.piezaBloqueada = uplayer.piezaBloqueada
    player.movPosiblesBloqueados = uplayer.movPosiblesBloqueados
    player.anim_move_ri = uplayer.anim_move_ri
    player.anim_move_ri_built = uplayer.anim_move_ri_built
    if server.game_winner is not None:
        player.revancha = uplayer.revancha

class Server:
    NUM_PLAYERS = 2
    ADDR = "localhost"
    PORT = 5555

    def __init__(self):
        self.tablero = self.crearNuevoTablero()
        self.game_winner = None
        self.players = self.crearJugadores()

        self.id_locked = [False, False]

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.bind((self.ADDR, self.PORT))
        except socket.error as e:
            print(e)

    def crearNuevoTablero(self):
        return Tablero(SWIDTH, SHEIGHT, WIDTH, HEIGHT)

    def crearJugadores(self):
        return [Jugador(True), Jugador(False)]

    def recibirEstadoJuego(self, conn):
        data = conn.recv(4096)
        if not data:
            return None
        state = pickle.loads(data)
        return state

    def compartirEstadoJuego(self, conn, state):
        encoded = pickle.dumps(state)
        conn.sendall(encoded)

    def listen(self):
        self.sock.listen(self.NUM_PLAYERS)
        id = None
        while True:
            conn, addr = self.sock.accept()
            if not self.id_locked[0]:
                self.id_locked[0] = True
                id = 0
            elif not self.id_locked[1]:
                self.id_locked[1] = True
                id = 1
            self.players[id].connected = True
            _thread.start_new_thread(self.client_thread, (conn, id))

    def client_thread(self, conn, id):
        start_info = {
            'yo': self.players[id],
            'otro': self.players[0] if id == 1 else self.players[1],
            'tablero': self.tablero if id == 0 else self.tablero.reversa()
        }
        self.compartirEstadoJuego(conn, start_info)
        while True:
            try:
                player_self = self.recibirEstadoJuego(conn)
                if player_self:
                    actualizarInfoJugador(self, self.players[id], player_self)
                    if isinstance(player_self.piezasMovidas, Pieza) and player_self.esTurno:
                        if id == 0:
                            self.tablero.moverPieza(player_self.piezasMovidas.pos, player_self.posMovida)
                            for pieza in player_self.piezaComida:
                                self.tablero.piezaComida(pieza.pos)
                            self.players[0].esTurno = False
                            self.players[1].esTurno = True
                            self.players[0].piezasMovidas = None
                            self.players[0].piezaComida = []
                            self.players[0].posMovida = None

                        elif id == 1:
                            self.tablero.moverPieza(player_self.piezasMovidas.pos, player_self.posMovida, comp=True)
                            for pieza in player_self.piezaComida:
                                self.tablero.piezaComida(pieza.pos, comp=True)
                            self.players[0].esTurno = True
                            self.players[1].esTurno = False
                            self.players[1].piezasMovidas\
                                = None
                            self.players[1].piezaComida = []
                            self.players[1].posMovida = None

                    actualizarRey(self.tablero)

                    self.game_winner = revisarGanador(self.tablero)

                    if self.game_winner is not None and self.players[0].revancha and self.players[1].revancha:
                        self.players = self.crearJugadores()
                        self.players[0].connected = True
                        self.players[1].connected = True
                        self.tablero = self.crearNuevoTablero()
                        self.game_winner = None

                    game_state = {
                        'yo': self.players[id],
                        'otro': self.players[0] if id == 1 else self.players[1],
                        'tablero': self.tablero if id == 0 else self.tablero.reversa(),
                        'ganador': self.game_winner
                    }
                    self.compartirEstadoJuego(conn, game_state)

                else:
                    print(f"Conexion con = {id} terminada.")
                    self.players[id].connected = False
                    self.id_locked[id] = False
                    break
            except:
                break

if __name__ == "__main__":
    server = Server()
    server.listen()



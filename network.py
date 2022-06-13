import socket
import pickle

class ConexionLAN:
    ADDR = "localhost"
    PORT = 5555
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = self.conectar()

    def infoInicial(self):
        return self.info

    def conectar(self):
        try:
            self.socket.connect((self.ADDR, self.PORT))
            return self.recibirEstadoJuego()
        except:
            print("Error en la conexion")

    def enviarEstadoJuego(self, state):
        encoded = pickle.dumps(state)

        try:
            self.socket.send(encoded)
            return self.recibirEstadoJuego()
        except socket.error as e:
            print(e)

    def recibirEstadoJuego(self):
        data = self.socket.recv(4096)
        return pickle.loads(data)

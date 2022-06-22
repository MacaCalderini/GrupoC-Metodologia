import pygame, sys
from piezatablero import *
from jugador import *
from server import Server
from network import *
from hud import *

ADDR, PORT = Server.ADDR, Server.PORT
def obtPosicionMouse(tablero_rect, posMouse):
    xoff, yoff = tablero_rect[0]
    mx, my = posMouse
    actx, acty = mx - xoff, my - yoff
    return actx, acty

def enviarAServer(network, player):
    try:
        reply = network.enviarEstadoJuego(player)
        return reply
    except socket.error as e:
        print(e)


def main():
    WIDTH, HEIGHT = 720, 640
    BOARDWIDTH, BOARDHEIGHT = 496, 496
    BACKGROUND_COLOR = (48, 29, 0)
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    net = ConexionLAN()
    start_info = net.infoInicial()
    player_self, player_other, tablero = start_info['yo'], start_info['otro'], start_info['tablero']
    hud = Hud(WIDTH, HEIGHT, BOARDWIDTH, BOARDHEIGHT, player_self)
    tablero_rect = tablero.obtTablero()

    while True:
        game_state = enviarAServer(net, player_self)
        player_self, player_other, tablero, game_winner = game_state['yo'], game_state['otro'], game_state['tablero'], game_state['ganador']

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posMouse = pygame.mouse.get_pos()
                act_pos = obtPosicionMouse(tablero_rect, posMouse)
                player_self.controlClicks(tablero, act_pos)
            if game_winner is not None and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_self.revancha = True

        if player_self.connected and player_other.connected and game_winner is None:
            win.fill(BACKGROUND_COLOR)
            hud.dibujar(win, tablero)
            tablero.dibujar(win)
            player_self.bloqDibujar(win, tablero)
        elif game_winner is not None:
            win.fill(BACKGROUND_COLOR)
            tablero.dibujar(win)
            win_font = pygame.font.SysFont(None, 36)
            text = win_font.render(f'{game_winner} gano', True, (255, 0, 0))
            text_revancha = win_font.render('Presiona [Enter] para jugar la revancha', True, (255, 0, 0))
            text_wait = win_font.render('Esperando a otro jugador', True, (255, 0, 0))
            fw, fh = text.get_width(), text.get_height()

            rw, rh = 400, fh * 2 + 30
            rx, ry = WIDTH//2 - rw//2, HEIGHT//2 - rh//2
            pygame.draw.rect(win, BACKGROUND_COLOR, pygame.rect.Rect(rx, ry, rw, rh), 0)
            pygame.draw.rect(win, (0, 0, 0), pygame.rect.Rect(rx - 1, ry - 1, rw + 2, rh + 2), 1)

            tx, ty = WIDTH // 2 - fw // 2, HEIGHT // 2 - fh // 2 - 15

            win.blit(text, (tx, ty))

            if not player_self.revancha:
                win.blit(text_revancha, (WIDTH//2 - text_revancha.get_width()//2, ty + fh + 2))
            else:
                win.blit(text_wait, (WIDTH//2 - text_wait.get_width()//2, ty + fh + 2))
        else:
            win.fill(BACKGROUND_COLOR)
            tablero.dibujar(win)
            wait_font = pygame.font.SysFont(None, 36)

            text = wait_font.render('Esperando a otro jugador...', True, (255, 0, 0))
            fw, fh = text.get_width(), text.get_height()

            rw, rh = 350, fh + 30
            rx, ry = WIDTH//2 - rw//2, HEIGHT//2 - rh//2
            pygame.draw.rect(win, BACKGROUND_COLOR, pygame.rect.Rect(rx, ry, rw, rh), 0)
            pygame.draw.rect(win, (0, 0, 0), pygame.rect.Rect(rx - 1, ry - 1, rw + 2, rh + 2), 1)
            win.blit(text, (WIDTH//2 - fw//2, HEIGHT//2 - fh//2))

        pygame.display.update()
        clock.tick(40)

if __name__ == "__main__":
    main()
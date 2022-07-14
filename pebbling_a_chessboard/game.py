import pygame
import sys
from .board import Board


class Game:
    def __init__(
        self,
        screen_size=(800, 800),
        square_size=100,
        dark_square_colour=(0, 0, 0),
        light_square_colour=(255, 255, 255),
    ):

        pygame.init()

        self.screen_size = screen_size
        self.square_size = square_size
        self.dark_square_colour = dark_square_colour
        self.light_square_colour = light_square_colour

        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Pebbling a Chessboard")

        self.board = Board()
        self._draw_board()

    def _draw_board(self):
        # draw the squares
        for row in range(8):
            for col in range(4):
                if row % 2 == 0:
                    pygame.draw.rect(
                        self.screen,
                        self.light_square_colour,
                        (
                            2 * col * self.square_size,
                            row * self.square_size,
                            self.square_size,
                            self.square_size,
                        ),
                    )

                    pygame.draw.rect(
                        self.screen,
                        self.dark_square_colour,
                        (
                            (2 * col + 1) * self.square_size,
                            row * self.square_size,
                            self.square_size,
                            self.square_size,
                        ),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        self.dark_square_colour,
                        (
                            2 * col * self.square_size,
                            row * self.square_size,
                            self.square_size,
                            self.square_size,
                        ),
                    )

                    pygame.draw.rect(
                        self.screen,
                        self.light_square_colour,
                        (
                            (2 * col + 1) * self.square_size,
                            row * self.square_size,
                            self.square_size,
                            self.square_size,
                        ),
                    )

        for row in range(8):
            for col in range(8):
                if self.board.board[row][col]:
                    posx = col * self.square_size + self.square_size / 2
                    posy = self.screen_size[0] - (
                        row * self.square_size + self.square_size / 2
                    )
                    pygame.draw.circle(self.screen, (255, 0, 0), (posx, posy), 40)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                row = int((self.screen_size[0] - event.pos[1]) / self.square_size)
                col = int(event.pos[0] / self.square_size)
                if self.board.board[row][col]:
                    self.board.play(row, col)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.board = Board()

    def play(self):
        while True:
            self.handle_events()
            self._draw_board()

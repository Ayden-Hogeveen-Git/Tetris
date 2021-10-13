# board.py
from loader import Colour
import pygame


class Board:
    def __init__(self, screen, screen_height, align_offset, border_colour):
        # Imported Stuff
        self.screen = screen
        self.colour = Colour()

        # Board Dimensions
        self.width = 10
        self.height = 20

        # Cell Image
        self.cell_size = screen_height // self.height
        self.cell_border = 1
        self.align_offset = align_offset
        self.border_colour = border_colour

        # Gamestate
        self.board_state = [
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
        ]

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                if not self.board_state[x][y]:
                    pygame.draw.rect(self.screen, self.border_colour,
                                     (self.align_offset + x * self.cell_size, (y * self.cell_size) + 0.5,
                                      self.cell_size, self.cell_size), self.cell_border)
                else:
                    # Draw the tetrominoes
                    pass

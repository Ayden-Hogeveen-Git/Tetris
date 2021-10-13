# board.py
from loader import Colour
from tiles import Tile
import pygame
import random


class Board:
    """
    Creates the grid
    Keeps track of tiles and pieces on the board
    Determines legal moves, valid coordinates, [y, x]
    Line clears
    """
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

        # Tiles
        self.tile = Tile(self.screen, screen_height, self.align_offset)

        # Gamestate
        self.board_state = [
            [False, False, False, "i", False, False, False, False, False, False],
            [False, False, False, "i", False, False, False, False, False, False],
            [False, False, False, "i", False, False, False, False, False, False],
            [False, False, False, "i", False, False, False, False, False, False],
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
            [False, "i", False, False, False, False, False, False, False, False],
            [False, "i", False, "t", False, False, False, False, False, False],
            ["lr", "i", "ll", "t", "t", False, "lr", False, False, False],
            ["lr", "i", "ll", "t", "o", "o", "lr", "zl", "zl", False],
            ["lr", "lr", "ll", "ll", "o", "o", "lr", "lr", "zl", "zl"]
        ]

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                """
                i = line piece
                o = square piece
                t = t-piece
                zr = right z-piece
                zl = left z-piece
                lr = right l-piece
                ll = left l-piece
                """
                if self.board_state[y][x] == "i":
                    self.tile.draw(x, y, self.colour.line_piece_colour, self.colour.line_piece_accent)
                elif self.board_state[y][x] == "o":
                    self.tile.draw(x, y, self.colour.square_piece_colour, self.colour.square_piece_accent)
                elif self.board_state[y][x] == "t":
                    self.tile.draw(x, y, self.colour.t_piece_colour, self.colour.t_piece_accent)
                elif self.board_state[y][x] == "zr":
                    self.tile.draw(x, y, self.colour.right_z_piece_colour, self.colour.right_z_piece_accent)
                elif self.board_state[y][x] == "zl":
                    self.tile.draw(x, y, self.colour.left_z_piece_colour, self.colour.left_z_piece_accent)
                elif self.board_state[y][x] == "lr":
                    self.tile.draw(x, y, self.colour.right_l_piece_colour, self.colour.right_l_piece_accent)
                elif self.board_state[y][x] == "ll":
                    self.tile.draw(x, y, self.colour.left_l_piece_colour, self.colour.left_l_piece_accent)
                else:
                    if not self.board_state[y][x]:
                        pygame.draw.rect(self.screen, self.border_colour,
                                         (self.align_offset + x * self.cell_size, (y * self.cell_size) + 0.5,
                                          self.cell_size, self.cell_size), self.cell_border)


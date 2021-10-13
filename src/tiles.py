# tiles.py
import pygame


class Tile:
    """
    Contains the calculations for movement and rotation
    """
    def __init__(self, screen, screen_height, align_offset):
        self.screen = screen
        self.tile_size = screen_height // 20
        self.align_offset = align_offset
        self.border_size = self.tile_size // 6

    def draw(self, x, y, colour1, colour2):
        pygame.draw.rect(self.screen, colour2,
                         (self.align_offset + x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
        pygame.draw.rect(self.screen, colour1, (self.align_offset + x * self.tile_size + self.border_size // 2,
                         y * self.tile_size + self.border_size // 2, self.tile_size - self.border_size,
                         self.tile_size - self.border_size))

    def fall(self):
        pass


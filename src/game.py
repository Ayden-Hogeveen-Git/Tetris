# game.py
from loader import Colour
import pygame
pygame.init()

# Window Variables
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")
# pygame.display.set_icon(pygame.image.load("assets/"))

# Globals and Initializations
colour = Colour()


class Game:
    def __init__(self):
        self.running = True

    def draw(self):
        """
        Displays the graphics to the screen, and updates the display.
        """
        screen.fill(colour.grey)
        pygame.display.update()

    def run(self):
        while self.running:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

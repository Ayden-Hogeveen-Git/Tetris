# main.py
"""
title: Tetris
author: Ayden Hogeveen
date-created: 2021-10-09
"""
import pygame
from game import Game

if __name__ == '__main__':
    print("Ready for Tetris!")
    game = Game()
    game.run()
    pygame.quit()
    quit()
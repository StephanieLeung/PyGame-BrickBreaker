'''
title: box sprite
author: Stephanie Leung
date-created: 2022-12-13
'''

from window import Window
from sprite import MySprite
import pygame

class Box(MySprite):
    def __init__(self, WIDTH=1, HEIGHT=1):
        super().__init__()
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__DIM = (self.__WIDTH, self.__HEIGHT)
        self._SCREEN = pygame.Surface(self.__DIM, pygame.SRCALPHA, 32)
        self._SCREEN.fill(self._COLOUR)

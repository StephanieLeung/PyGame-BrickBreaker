'''
title: Paddle Class
author: Stpehanie Leung
date-created: 2023-02-06
'''

from box import Box
import pygame

# inheritance
class Paddle(Box):
    def __init__(self, WIDTH=1, HEIGHT=1):
        super().__init__(WIDTH, HEIGHT)

    # -- Modifier Methods
    # polymorphism
    def moveWASD(self, PRESSED_KEYS):
        if PRESSED_KEYS[pygame.K_d] == 1 or PRESSED_KEYS[pygame.K_RIGHT] == 1:
            self.setX(self.getX() + self.getSpeed())
        if PRESSED_KEYS[pygame.K_a] == 1 or PRESSED_KEYS[pygame.K_LEFT] == 1:
            self.setX(self.getX() - self.getSpeed())

    # polymorphism
    def isCollision(self, SCREEN, POS):
        WIDTH = SCREEN.get_width()
        HEIGHT = SCREEN.get_height()
        X = POS[0]
        Y = POS[1]

        if self.getX() - WIDTH <= X <= self.getX() + self.getWidth():
            if self.getY() - HEIGHT <= Y <= self.getY():
                return True
        return False

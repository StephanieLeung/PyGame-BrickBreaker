'''
title: Brick Class
author: Stephanie Leung
date-created: 2023-02-06
'''

from box import Box

# inheritance
class Brick(Box):
    def __init__(self, WIDTH=100, HEIGHT=40):
        super().__init__(WIDTH, HEIGHT)
        self.__HP = 2

    # Modifier Methods
    def setHP(self, HP):
        self.__HP = HP

    # Accessor Methods
    def getHP(self):
        return self.__HP

    def checkSide(self, SCREEN, POS):
        '''
        checks which side of the brick that the given object has collided with
        :param SCREEN: Surface -> Object
        :param POS: tuple (int)
        :return: int
        '''
        WIDTH = SCREEN.get_width()
        HEIGHT = SCREEN.get_height()
        X = POS[0]
        Y = POS[1]

        if (Y != self.getY() - HEIGHT and Y != self.getY() + self.getHeight()) and (X != self.getX() - WIDTH or X != self.getX() + self.getWidth()):
            if X < self.getX() + (self.getWidth() // 2):
                X = self.getX() - WIDTH
            else:
                X = self.getX() + self.getWidth()

        if self.getX() - WIDTH < X < self.getX() + self.getWidth():
            return 0
        elif self.getX() - WIDTH == X or self.getX() + self.getWidth() == X:
            return 1


    def checkCorner(self, SCREEN, POS):
        '''
        checks if given object is at each corner of brick
        :param SCREEN: Surface -> obj
        :param POS: tuple (int)
        :return: int
        '''
        WIDTH = SCREEN.get_width()
        HEIGHT = SCREEN.get_height()
        X = POS[0]
        Y = POS[1]

        if self.getX() - WIDTH == X and self.getY() - HEIGHT == Y:
            return 0
        elif self.getX() + self.getWidth() == X and self.getY() - HEIGHT == Y:
            return 1
        elif self.getX() - WIDTH == X and self.getY() + self.getHeight() == Y:
            return 2
        elif self.getX() + self.getWidth() == X and self.getY() + self.getHeight() == Y:
            return 3
        else:
            return 4

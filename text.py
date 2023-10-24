'''
title: Text class
author: Stephanie Leung
date-created: 2023-02-14
'''

import pygame
from sprite import MySprite

class Text(MySprite):
    # Creating a text class that inherits from MySprite
    def __init__(self, TEXT):
        super().__init__()
        self.__TEXT = TEXT
        self.__FONT = pygame.font.SysFont("Arial", 25)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self._COLOUR)

    # Modifier Method
    def updateText(self, TEXT):
        '''
        updates text
        :param TEXT: str
        :return: None
        '''
        self.__TEXT = TEXT
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self._COLOUR)

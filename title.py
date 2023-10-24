'''
title: Title Class
author: Stephanie Leung
date-created: 2023-02-14
'''

from box import Box
from text import Text

class Title(Box):
    def __init__(self, TITLE, LEFT_TEXT, RIGHT_TEXT, MAX_WIDTH):
        super().__init__(MAX_WIDTH, 50)
        self.__LTEXT = Text(LEFT_TEXT)
        self.__RTEXT = Text(RIGHT_TEXT)
        self.__TITLE = Text(TITLE)
        self.__LTEXT.setPOS(10, self.getHeight()//2 - self.__LTEXT.getHeight()//2)
        self.__RTEXT.setPOS(MAX_WIDTH - self.__RTEXT.getWidth() - 10, self.getHeight()//2 - self.__RTEXT.getHeight()//2)
        self.__TITLE.setPOS(MAX_WIDTH//2 - self.__TITLE.getWidth()//2, self.getHeight()//2 - self.__TITLE.getHeight()//2)
        self.setColour((0, 0, 0))

    # Accessor Method
    def getLText(self):
        return self.__LTEXT

    def getRText(self):
        return self.__RTEXT

    def blitOntoScreen(self, SCREEN):
        '''
        blits components of title onto the screen together
        :param SCREEN: Surface -> Object
        :return: None
        '''
        SCREEN.blit(self.getScreen(), self.getPOS())
        SCREEN.blit(self.__LTEXT.getScreen(), self.__LTEXT.getPOS())
        SCREEN.blit(self.__RTEXT.getScreen(), self.__RTEXT.getPOS())
        SCREEN.blit(self.__TITLE.getScreen(), self.__TITLE.getPOS())




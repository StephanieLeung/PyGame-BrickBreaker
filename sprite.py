import pygame
class MySprite:
    '''
    generic sprite class
    '''
    # encapsulation (protected attributes with getter/setter methods)
    def __init__(self, X=0, Y=0):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self._SCREEN = None
        self.__SPEED = 1
        self.__dirX = 1
        self.__dirY = 1
        self._COLOUR = (255, 255, 255)

    # Accessor Method
    def getScreen(self):
        return self._SCREEN

    def getPOS(self):
        return self.__POS

    def getWidth(self):
        return self._SCREEN.get_width()

    def getHeight(self):
        return self._SCREEN.get_height()

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getSpeed(self):
        return self.__SPEED

    def getDirX(self):
        return self.__dirX

    def getDirY(self):
        return self.__dirY

    # Modifier Method
    def setPOS(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setX(self, X):
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setSpeed(self, SPEED):
        if SPEED > 0:
            self.__SPEED = SPEED

    def setDirX(self, DIRX):
        self.__dirX = DIRX

    def setDirY(self, DIRY):
        self.__dirY = DIRY

    def setColour(self, COLOUR):
        self._COLOUR = COLOUR
        self._SCREEN.fill(self._COLOUR)

    def bounceX(self, MAX_WIDTH, MIN_WIDTH=0):
        if self.__X + self.__SPEED > MAX_WIDTH - self._SCREEN.get_width():
            self.__dirX = -1
        elif self.__X < MIN_WIDTH:
            self.__dirX = 1
        self.setX(self.__X + self.__dirX * self.__SPEED)

    def bounceY(self, MAX_HEIGHT, MIN_HEIGHT=0):
        if self.__Y + self.__SPEED > MAX_HEIGHT - self._SCREEN.get_height():
            self.__dirY = -1
        elif self.__Y < MIN_HEIGHT:
            self.__dirY = 1
        self.setY(self.__Y + self.__dirY * self.__SPEED)

    def flipDirX(self):
        self.__dirX = self.__dirX * -1

    def flipDirY(self):
        self.__dirY = self.__dirY * -1

    def moveWASD(self, PRESSED_KEYS):
        '''
        move box using WASD
        :param PRESSED_KEYS: list(int) -> key state
        :return:
        '''

        if PRESSED_KEYS[pygame.K_d] == 1:
            self.setX(self.__X + self.__SPEED)
        if PRESSED_KEYS[pygame.K_a] == 1:
            self.setX(self.__X - self.__SPEED)
        if PRESSED_KEYS[pygame.K_w] == 1:
            self.setY(self.__Y - self.__SPEED)  # going up is minus
        if PRESSED_KEYS[pygame.K_s] == 1:
            self.setY(self.__Y + self.__SPEED)

    def stopAtEdges(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        if self.__X > MAX_X - self._SCREEN.get_width():
            self.setX(MAX_X - self._SCREEN.get_width())
        elif self.__X < MIN_X:
            self.setX(MIN_X)

        if self.__Y > MAX_Y - self._SCREEN.get_height():
            self.setY(MAX_Y - self._SCREEN.get_height())
        elif self.__Y < MIN_Y:
            self.setY(MIN_Y)

    def isCollision(self, SCREEN, POS):
        '''
        testing whether the current sprite position is overlapping the given sprite's position
        :param SCREEN: object -> Surface
        :param POS: tuple -> int
        :return: bool
        '''
        WIDTH = SCREEN.get_width()
        HEIGHT = SCREEN.get_height()
        X = POS[0]
        Y = POS[1]

        if self.__X - WIDTH <= X <= self.__X + self.getScreen().get_width():
            if self.__Y - HEIGHT <= Y <= self.__Y + self.getScreen().get_height():
                return True
        return False



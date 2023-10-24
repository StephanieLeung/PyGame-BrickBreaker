import pygame


class Window:
    '''
    creates the window that will load pygame
    return: None
    '''

    def __init__(self, TITLE, WIDTH, HEIGHT, FPS):
        self.__TITLE = TITLE  # text that appears in the title bar
        self.__FPS = FPS  # frames per second the program will run
        self.__WIDTH = WIDTH  # width of the window frame
        self.__HEIGHT = HEIGHT  # height of the window frame
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)  # screen dimensions
        self.__BG_COLOR = (50, 50, 50)
        self.__FRAME = pygame.time.Clock()  # clock object that measures FPS
        self.__SCREEN = pygame.display.set_mode(self.__SCREEN_DIM)
        # SCREEN object. Every item in your program will overlay onto this screen
        self.__SCREEN.fill(self.__BG_COLOR)  # fills the screen with a layer of the color
        pygame.display.set_caption(self.__TITLE)  # sets the title of the window to the title value

    # Modifier Methods
    def updateFrame(self):
        '''
        updates the window object based on the FPS
        :return: None
        '''
        self.__FRAME.tick(self.__FPS)  # program waits for the appropriate time based on FPS
        pygame.display.flip()  # updates the computer display with the new frame

    def clearScreen(self):
        '''
        fill the SCREEN with the background colour
        :return: None
        '''
        self.__SCREEN.fill(self.__BG_COLOR)

    # Accessor Methods
    def getScreen(self):
        return self.__SCREEN

    def getWidth(self):
        return self.__WIDTH
        # return self.__SCREEN.get_width()

    def getHeight(self):
        return self.__SCREEN.get_height()

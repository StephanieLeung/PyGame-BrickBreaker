'''
title: Game class
author: Stephanie Leung
date-created: 2021-02-02
'''

import pygame
from window import Window
from title import Title
from text import Text
from box import Box
from paddle import Paddle
from brick import Brick
from random import randrange

# Abstraction
class Game:
    def __init__(self):
        # Aggregation
        pygame.init()
        # Window
        self.__WINDOW = Window("Brick Breaker", 800, 600, 30)
        # Game Vars
        self.__START = False
        self.__CONTINUE = True
        self.__BUFF = None
        self.__SCORE = 0
        self.__COIN = 0
        # Title Bar
        self.__TITLE = Title("Brick Breaker", f"Score: {self.__SCORE}", f"Coins: {self.__COIN}", self.__WINDOW.getWidth())
        # Start/Continue Message
        self.__TEXT = Text("Press SPACE to start")
        self.__TEXT.setPOS((self.__WINDOW.getWidth() - self.__TEXT.getWidth()) //2, 450)
        # Buff Message
        self.__BUFF_MSG = Text("You have obtained more than 5 coins.")
        self.__BUFF_MSG2 = Text("Press Y/N to choose if you want to use coins for a buff")
        self.__BUFF_MSG.setPOS((self.__WINDOW.getWidth() - self.__BUFF_MSG.getWidth()) //2, 350)
        self.__BUFF_MSG2.setPOS((self.__WINDOW.getWidth() - self.__BUFF_MSG2.getWidth()) //2, 400)
        # Bricks
        self.__BRICKS = []
        self.buildBricks()
        # Coins
        self.__COINS = []
        self.placeCoins()
        # Paddle
        self.initializePaddle(100)
        # Ball
        self.__BALL = Box(20, 20)
        self.__BALL.setPOS((self.__WINDOW.getWidth() - self.__BALL.getWidth()) // 2, 500)
        self.__BALL.setSpeed(10)
        self.__BALL.setDirY(-1)

    def buildBricks(self):
        '''
        builds bricks and sets each position
        :return: None
        '''
        Y = 100
        INDEX = 0

        for i in range(5):
            PAIR = 1
            DIR = 1
            X = self.__WINDOW.getWidth() // 2 - 50
            self.__BRICKS.append(Brick())
            self.__BRICKS[INDEX].setPOS(X, Y)
            INDEX += 1
            RANDOM = randrange(0, 3) * 2
            for j in range(RANDOM):
                self.__BRICKS.append(Brick())
                self.__BRICKS[INDEX].setPOS(self.__BRICKS[INDEX - 1].getX() + ((PAIR * 115) * DIR), Y)
                INDEX += 1
                PAIR += 1
                DIR *= -1
            Y += 50

    def placeCoins(self):
        '''
        places coins under bricks
        :return: None
        '''
        SAVE = []
        i = 0
        while i <= 5:
            RAND = randrange(len(self.__BRICKS))
            if self.__BRICKS[RAND].getPOS() not in SAVE:
                SAVE.append(self.__BRICKS[RAND].getPOS())
                self.__COINS.append(Box(10, 10))
                self.__COINS[i].setPOS(self.__BRICKS[RAND].getX() + self.__BRICKS[RAND].getWidth() // 2 - 5,
                                       self.__BRICKS[RAND].getY() + self.__BRICKS[RAND].getHeight() // 2 - 5)
                self.__COINS[i].setColour((92, 247, 164))
                i += 1

    def initializePaddle(self, WIDTH):
        '''
        initializes the paddle with given width
        :param WIDTH: int
        :return: None
        '''
        self.__PADDLE = Paddle(WIDTH, 20)
        self.__PADDLE.setSpeed(17)
        self.__PADDLE.setPOS((self.__WINDOW.getWidth() - self.__PADDLE.getWidth()) // 2, 550)


    def run(self):
        '''
        runs the game
        :return: None
        '''
        pygame.init()
        while True:
            # --- inputs
            PRESSED_KEYS = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or PRESSED_KEYS[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()

            # --- processing
            if self.__START is False:
                # game starts after user presses space
                if PRESSED_KEYS[pygame.K_SPACE]:
                    self.__START = True
            elif self.__CONTINUE is False:
                # if user wants to continue game, reset all variables and objects to start position
                if PRESSED_KEYS[pygame.K_c]:
                    self.__CONTINUE = True
                    self.__START = False
                    self.__TEXT.updateText("Press SPACE to start")
                    self.__TITLE.getRText().updateText(f"Coins: {self.__COIN}")
                    if self.__BRICKS:
                        self.__SCORE = 0
                        self.__TITLE.getLText().updateText(f"Score: {self.__SCORE}")
                    if self.__BUFF:
                        self.initializePaddle(130)
                    else:
                        self.__BUFF = None
                        self.initializePaddle(100)
                    self.__PADDLE.setPOS((self.__WINDOW.getWidth() - self.__PADDLE.getWidth()) // 2, 550)
                    self.__BALL.setPOS((self.__WINDOW.getWidth() - self.__BALL.getWidth()) // 2, 500)
                    self.__BALL.setDirX(1)
                    self.__BALL.setDirY(-1)
                    self.__BRICKS = []
                    self.buildBricks()
                    self.__COINS = []
                    self.placeCoins()
                # if user accepts buff, decrease coins and activate buff
                elif PRESSED_KEYS[pygame.K_y] and self.__BUFF is False:
                    if self.__COIN - 5 < 0:
                        self.__COIN = 0
                    else:
                        self.__COIN -= 5
                    self.__BUFF = True
                # if user declines buff, stop displaying message
                elif PRESSED_KEYS[pygame.K_n] and self.__BUFF is False:
                    self.__BUFF = None
            else:
                # move paddle according to user input and bounces ball
                self.__PADDLE.moveWASD(PRESSED_KEYS)
                self.__PADDLE.stopAtEdges(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                if self.__BALL.getY() + self.__BALL.getHeight() != self.__WINDOW.getHeight():
                    self.__BALL.bounceX(self.__WINDOW.getWidth())
                    self.__BALL.bounceY(self.__WINDOW.getHeight(), self.__TITLE.getY()+ self.__TITLE.getHeight())

            # checks collision between paddle and ball and bounces ball in opposite direction
            if self.__PADDLE.isCollision(self.__BALL.getScreen(), self.__BALL.getPOS()):
                self.__BALL.flipDirY()
                self.__BALL.setY(self.__PADDLE.getY() - self.__BALL.getHeight())

            # check collision with coins
            for i in range(len(self.__COINS)):
                if self.__COINS[i].isCollision(self.__BALL.getScreen(), self.__BALL.getPOS()):
                    self.__COIN += 1
                    self.__TITLE.getRText().updateText(f"Coins: {self.__COIN}")
                    self.__COINS.pop(i)
                    break

            # checks collision for each brick
            for i in range(len(self.__BRICKS)):
                if self.__BRICKS[i].isCollision(self.__BALL.getScreen(), self.__BALL.getPOS()):
                    # checks which side/corner the ball collided with and bounces back in the opposite direction
                    COLLISION = False
                    CORNER = self.__BRICKS[i].checkCorner(self.__BALL.getScreen(), self.__BALL.getPOS())
                    if ((CORNER == 0 or CORNER == 3) and self.__BALL.getDirX() == self.__BALL.getDirY()) or ((CORNER == 1 or CORNER == 2) and self.__BALL.getDirX() == self.__BALL.getDirY() * -1):
                        self.__BALL.flipDirX()
                        self.__BALL.flipDirY()
                        COLLISION = True
                    elif CORNER == 4:
                        SIDE = self.__BRICKS[i].checkSide(self.__BALL.getScreen(), self.__BALL.getPOS())
                        if SIDE == 0:
                            self.__BALL.flipDirY()
                        else:
                            self.__BALL.flipDirX()
                        COLLISION = True

                    # checks for collision before game vars
                    if COLLISION:
                        # updates score
                        self.__SCORE += 1
                        self.__TITLE.getLText().updateText(f"Score: {self.__SCORE}")
                        # decrease HP of brick
                        HP = self.__BRICKS[i].getHP() - 1
                        self.__BRICKS[i].setHP(HP)
                        # delete brick if HP is 0
                        if HP == 0:
                            self.__BRICKS.pop(i)
                        # update colour of brick to indicate half health
                        elif HP == 1:
                            self.__BRICKS[i].setColour((115, 147, 179))
                        break

            # check for reset conditions (if ball touches bottom or no bricks left)
            if self.__BALL.getY() == self.__WINDOW.getHeight() - self.__BALL.getHeight() or not self.__BRICKS:
                if self.__CONTINUE is True:
                    if self.__BUFF is True:
                        self.__BUFF = None
                    if self.__COIN >= 5:
                        self.__BUFF = False

                # displays continue message
                self.__CONTINUE = False
                self.__TEXT.updateText("Press C to continue")

            # --- output
            # display all objects (bricks, paddle, ball) onto the window
            self.__WINDOW.clearScreen()
            for coin in self.__COINS:
                self.__WINDOW.getScreen().blit(coin.getScreen(), coin.getPOS())
            for brick in self.__BRICKS:
                self.__WINDOW.getScreen().blit(brick.getScreen(), brick.getPOS())
            self.__WINDOW.getScreen().blit(self.__BALL.getScreen(), self.__BALL.getPOS())
            self.__WINDOW.getScreen().blit(self.__PADDLE.getScreen(), self.__PADDLE.getPOS())
            self.__TITLE.blitOntoScreen(self.__WINDOW.getScreen())
            # display start/continue message if game has not started yet
            if not self.__START or not self.__CONTINUE:
                self.__WINDOW.getScreen().blit(self.__TEXT.getScreen(), self.__TEXT.getPOS())
            # if waiting for user response, display buff message
            if self.__BUFF is False:
                self.__WINDOW.getScreen().blit(self.__BUFF_MSG.getScreen(), self.__BUFF_MSG.getPOS())
                self.__WINDOW.getScreen().blit(self.__BUFF_MSG2.getScreen(), self.__BUFF_MSG2.getPOS())

            self.__WINDOW.updateFrame()

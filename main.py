'''
title: Main class
author: Stephanie Leung
date-created: 2023-02-26
'''

from game import Game


class Main:
    def __init__(self):
        GAME = Game()
        GAME.run()

# -- Main Program Code -- #
if __name__ == "__main__":
    MAIN = Main()

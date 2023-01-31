from Game import *
import threading

if __name__ == '__main__':
    game = Game()
    game.logo()
    game.init_map()
    game.init()
    game.loop()

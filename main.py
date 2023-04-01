from Game import *


if __name__ == '__main__':
    game = Game()
    # game.logo()
    game.init_map()
    game.init()
    game.start_screen()
    game.loop()
    game.end_screen()

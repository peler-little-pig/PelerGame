from pygame.locals import *
from Actor.GoodActor import *
from Coin.EnergyCoin import EnergyCoin
from Lib.MapLoader.MapLoader import *
import sys
from Lib.Logo.logo import *
from Group.CoinGroup import *
from Lib.Creator import MapCreator


class Game(object):
    def __init__(self):
        pygame.init()

        GameData.fps_clock = pygame.time.Clock()
        GameData.surface = pygame.display.set_mode((GameData.WINDOW_WIDTH, GameData.WINDOW_HEIGHT))

        pygame.display.set_caption(GameData.NAME)

    def init(self):
        self.coin_gruop = CoinGroup()
        ShareData.coin_group = self.coin_gruop
        self.good_actor = GoodActor()
        ShareData.good_actor = self.good_actor
        self.map = map_loader()
        self.map_index = 0
        ShareData.world = self.map[self.map_index][0]
        ShareData.bad_actor_group = self.map[self.map_index][1]
        ShareData.game = self

        self.nexted = False

    def init_map(self):
        MapCreator.clean()
        MapCreator.map(3)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    EventData.is_key_w_down = True
                if event.key == K_s:
                    EventData.is_key_s_down = True
                if event.key == K_a:
                    EventData.is_key_a_down = True
                if event.key == K_d:
                    EventData.is_key_d_down = True

            elif event.type == KEYUP:
                if event.key == K_w:
                    EventData.is_key_w_down = False
                if event.key == K_s:
                    EventData.is_key_s_down = False
                if event.key == K_a:
                    EventData.is_key_a_down = False
                if event.key == K_d:
                    EventData.is_key_d_down = False

            elif event.type == MOUSEWHEEL:
                if event.y == 1:
                    ShareData.good_actor.thing_index_after()
                else:
                    ShareData.good_actor.thing_index_next()

            EventData.is_mouse_move = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == BUTTON_LEFT:
                    EventData.is_left_mouse_down = True
                elif event.button == BUTTON_RIGHT:
                    EventData.is_right_mouse_down = True
            if event.type == MOUSEBUTTONUP:
                if event.button == BUTTON_LEFT:
                    EventData.is_left_mouse_down = False
                elif event.button == BUTTON_RIGHT:
                    EventData.is_right_mouse_down = False
            if event.type == MOUSEMOTION:
                EventData.is_mouse_move = True
                EventData.mouse_x, EventData.mouse_y = event.pos

    def process(self):
        self.map[self.map_index][0].process()
        self.map[self.map_index][1].process()
        self.good_actor.process()
        self.coin_gruop.process()

    def draw(self):
        self.map[self.map_index][0].draw()
        self.map[self.map_index][1].draw()
        self.good_actor.draw()
        self.coin_gruop.draw()

    def loop(self):
        while True:
            GameData.surface.fill((200, 255, 255))

            self.event()
            self.process()
            self.draw()

            print(GameData.fps_clock.get_fps())

            pygame.display.update()
            GameData.fps_clock.tick(GameData.FPS)

            self.nexted = False

    def next_world(self):
        if not self.nexted:
            self.map_index += 1
            ShareData.world = self.map[self.map_index][0]
            ShareData.bad_actor_group = self.map[self.map_index][1]
            self.nexted = True

    def logo(self):
        fs = FSLogo('./Res/Picture/image/logo/logo.png')
        while fs.alphaIndex < 254:
            GameData.surface.fill((255, 255, 255))

            self.event()

            fs.pack()
            fs.update()

            pygame.display.update()

    def exit(self):
        pygame.quit()
        sys.exit()

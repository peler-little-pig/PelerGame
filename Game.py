from pygame.locals import *
from Actor.GoodActor import *
from Lib.MapLoader.MapLoader import *
import sys
from Lib.Logo.logo import *


class Game(object):
    def __init__(self):
        self.init()

        self.good_actor = GoodActor()
        ShareData.good_actor = self.good_actor
        self.map = map_loader()
        self.map_index = 0
        ShareData.world = self.map[self.map_index][0]
        ShareData.bad_actor_group = self.map[self.map_index][1]

        ShareData.game = self

        self.nexted = False

    def init(self):
        pygame.init()

        ConstData.fps_clock = pygame.time.Clock()
        ConstData.surface = pygame.display.set_mode((ConstData.WINDOW_WIDTH, ConstData.WINDOW_HEIGHT))

        pygame.display.set_caption(ConstData.GAME_NAME)

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

            EventData.is_mouse_move = False
            if event.type == MOUSEBUTTONDOWN:
                EventData.is_mouse_down = True
            if event.type == MOUSEBUTTONUP:
                EventData.is_mouse_down = False
            if event.type == MOUSEMOTION:
                EventData.is_mouse_move = True
                EventData.mouse_x, EventData.mouse_y = event.pos

    def process(self):
        self.map[self.map_index][0].process()
        self.map[self.map_index][1].process()
        self.good_actor.process()

    def draw(self):
        self.map[self.map_index][0].draw()
        self.map[self.map_index][1].draw()
        self.good_actor.draw()

    def loop(self):
        while True:
            ConstData.surface.fill((200, 255, 255))

            self.event()
            self.draw()
            self.process()

            pygame.display.update()
            ConstData.fps_clock.tick(ConstData.FPS)

            self.nexted = False

    def next_world(self):
        if not self.nexted:
            self.map_index += 1
            print(self.map_index)
            ShareData.world = self.map[self.map_index][0]
            ShareData.bad_actor_group = self.map[self.map_index][1]
            self.nexted = True

    def logo(self):
        fs = FSLogo('./Res/image/logo/logo.png')
        while fs.alphaIndex < 254:
            ConstData.surface.fill((255, 255, 255))

            self.event()

            fs.pack()
            fs.update()

            pygame.display.update()

    def exit(self):
        pygame.quit()
        sys.exit()

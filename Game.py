import sys
from pygame.locals import *
from Space.SpaceLoader import *
from Value import *


class Game(object):
    def __init__(self):
        self.init()

        self.good_actor = GoodActor()
        self.room = world_loader('./map/test.pworld')

    def init(self):
        pygame.init()

        Value.fps_clock = pygame.time.Clock()
        Value.surface = pygame.display.set_mode((Value.WINDOW_WIDTH, Value.WINDOW_HEIGHT))

        pygame.display.set_caption(Value.GAME_NAME)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    Value.is_key_w_down = True
                if event.key == K_s:
                    Value.is_key_s_down = True
                if event.key == K_a:
                    Value.is_key_a_down = True
                if event.key == K_d:
                    Value.is_key_d_down = True

            elif event.type == KEYUP:
                if event.key == K_w:
                    Value.is_key_w_down = False
                if event.key == K_s:
                    Value.is_key_s_down = False
                if event.key == K_a:
                    Value.is_key_a_down = False
                if event.key == K_d:
                    Value.is_key_d_down = False

            elif event.type == MOUSEBUTTONDOWN:
                Value.is_mouse_down = True
            elif event.type == MOUSEBUTTONUP:
                Value.is_mouse_down = False
            elif event.type == MOUSEMOTION:
                Value.mouse_down_x, Value.mouse_down_y = event.pos

    def process(self):
        self.room.process(self.good_actor)
        self.good_actor.process()

    def draw(self):
        self.room.draw()
        self.good_actor.draw()

    def loop(self):
        while True:
            Value.surface.fill((0, 0, 0))

            self.event()
            self.draw()
            self.process()

            pygame.display.update()
            Value.fps_clock.tick(Value.FPS)

    def exit(self):
        pygame.quit()
        sys.exit()

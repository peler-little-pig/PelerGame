import sys
from pygame.locals import *
from Actor.GoodActor import *
from Thing.BaseThing import *
from Space.PMapLoader import *


class Game(object):
    def __init__(self):
        self.init()

        self.actor = GoodActor()
        self.room = world_loader('./map/test.pindex')

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

        if Value.is_key_w_down:
            self.room.move_up(self.actor)
        if Value.is_key_s_down:
            self.room.move_down(self.actor)
        if Value.is_key_a_down:
            self.room.move_left(self.actor)
        if Value.is_key_d_down:
            self.room.move_right(self.actor)

    def draw(self):
        self.room.draw()
        self.actor.draw()

    def loop(self):
        while True:
            Value.surface.fill((0, 0, 0))

            self.event()
            self.draw()

            pygame.display.update()
            Value.fps_clock.tick(Value.FPS)

    def exit(self):
        pygame.quit()
        sys.exit()

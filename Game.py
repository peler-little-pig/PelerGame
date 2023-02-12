from Actor.GoodActor.BaseGoodActor import *
from Actor.HireActor.BaseHireActor import BaseHireActor
from Group.HireActorGroup import HireActorGroup
from MapLoader.MapLoader import *
import sys
from Logo.logo import *
from Group.CoinGroup import *
from Creator import MapCreator
from GUI.Manager import Manager
from Screen.EndSceen import EndScreen
from Screen.PauseSceen import PauseScreen
from Screen.StartSceen import *
from Screen.SystemInfoScreen import SystemInfoScreen
from Thing.BloodDrinkThing import BloodDrinkThing


class Game(object):
    def __init__(self):
        pygame.init()

        GameData.fps_clock = pygame.time.Clock()
        GameData.surface = pygame.display.set_mode((GameData.WINDOW_WIDTH, GameData.WINDOW_HEIGHT))

        pygame.display.set_caption(GameData.NAME)

    def init(self):
        self.coin_gruop = CoinGroup()
        ShareData.coin_group = self.coin_gruop
        # self.hire_group = HireActorGroup()
        # ShareData.hire_group = self.hire_group
        self.good_actor = BaseGoodActor()
        ShareData.good_actor = self.good_actor
        self.map = map_loader()
        ShareData.world = self.map.world()
        ShareData.bad_actor_group = self.map.bad_actor_group()
        ShareData.drop_thing_group = self.map.drop_thing_group()
        ShareData.game = self

        self.nexted = False
        self.is_game_running = True
        self.is_restart = False
        self.is_pause_screen = False
        self.is_system_info_screen = False

        self._system_info_screen = SystemInfoScreen()

        # self.hire_group.append(BaseHireActor(*ShareData.good_actor.center))
        ShareData.drop_thing_group.append(BloodDrinkThing(*self.good_actor.center))

    def init_map(self):
        MapCreator.clean()
        MapCreator.map(5)

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
                if event.key == K_q:
                    EventData.is_key_q_down = True
                if event.key == K_e:
                    EventData.is_key_e_down = True
                if event.key == K_f:
                    EventData.is_key_f_down = True
                if event.key == K_SPACE:
                    self.is_pause_screen = True
                if event.key == K_F1:
                    self.is_system_info_screen = not self.is_system_info_screen

            elif event.type == KEYUP:
                if event.key == K_w:
                    EventData.is_key_w_down = False
                if event.key == K_s:
                    EventData.is_key_s_down = False
                if event.key == K_a:
                    EventData.is_key_a_down = False
                if event.key == K_d:
                    EventData.is_key_d_down = False
                if event.key == K_q:
                    EventData.is_key_q_down = False
                if event.key == K_e:
                    EventData.is_key_e_down = False
                if event.key == K_f:
                    EventData.is_key_f_down = False

            elif event.type == MOUSEWHEEL:
                if event.y == 1:
                    ShareData.good_actor.thing_index_after()
                else:
                    ShareData.good_actor.thing_index_next()

            EventData.is_mouse_move = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == BUTTON_LEFT:
                    EventData.is_left_mouse_down = True
                if event.button == BUTTON_RIGHT:
                    EventData.is_right_mouse_down = True
                if event.button == BUTTON_MIDDLE:
                    EventData.is_middle_mouse_down = True
            if event.type == MOUSEBUTTONUP:
                if event.button == BUTTON_LEFT:
                    EventData.is_left_mouse_down = False
                if event.button == BUTTON_RIGHT:
                    EventData.is_right_mouse_down = False
                if event.button == BUTTON_MIDDLE:
                    EventData.is_middle_mouse_down = False
            if event.type == MOUSEMOTION:
                EventData.is_mouse_move = True
                EventData.mouse_x, EventData.mouse_y = event.pos

            if event.type == WINDOWLEAVE:
                EventData.is_left_mouse_down = False
                EventData.is_right_mouse_down = False
            if event.type == WINDOWFOCUSLOST or event.type == WINDOWMOVED:
                self.is_pause_screen = True

    def start_screen(self):
        screen = StartScreen()
        while screen.is_running:
            GameData.surface.fill((0, 0, 0))
            screen.manager.draw()
            for event in pygame.event.get():
                screen.manager.event(event)
                if event.type == QUIT:
                    self.exit()
                if event.type == KEYDOWN:
                    screen.start_game()
            screen.manager.process()
            pygame.display.update()

    def pause_screen(self):
        if self.is_pause_screen:
            screen = PauseScreen()
            while screen.is_running:
                self.draw()
                screen.manager.draw()
                for event in pygame.event.get():
                    screen.manager.event(event)
                    if event.type == QUIT:
                        self.exit()
                    if event.type == KEYDOWN:
                        screen.continue_game()
                screen.manager.process()
                pygame.display.update()
        self.is_pause_screen = False

    def end_screen(self):
        screen = EndScreen()
        while screen.is_running:
            GameData.surface.fill((0, 0, 0))
            screen.manager.draw()
            for event in pygame.event.get():
                screen.manager.event(event)
                if event.type == QUIT:
                    self.exit()
                if event.type == KEYDOWN:
                    screen.restart_game()
            screen.manager.process()
            pygame.display.update()

    def system_info_screen(self):
        if self.is_system_info_screen:
            self._system_info_screen.manager.draw()
            self._system_info_screen.manager.update(0)

    def process(self):
        self.map.world().process()
        self.map.bad_actor_group().process()
        self.good_actor.process()
        self.map.drop_thing_group().process()
        self.coin_gruop.process()
        # self.hire_group.process()

    def draw(self):
        self.map.world().draw()
        self.map.bad_actor_group().draw()
        # self.hire_group.draw()
        self.good_actor.draw()
        self.map.drop_thing_group().draw()
        self.coin_gruop.draw()

    def loop(self):
        while self.is_game_running:
            GameData.surface.fill((100, 155, 155))

            self.event()
            self.draw()
            self.process()

            self.pause_screen()
            self.system_info_screen()

            pygame.display.update()
            GameData.fps_clock.tick(GameData.FPS)

            self.nexted = False

    def next_world(self):
        if not self.nexted:
            self.map.next()
            ShareData.world = self.map.world()
            ShareData.bad_actor_group = self.map.bad_actor_group()
            ShareData.drop_thing_group = self.map.drop_thing_group()
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

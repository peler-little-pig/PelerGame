import pygame
import pygame_gui
import random


class HealthySprite(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.health_capacity = 100
        self.current_health = 75
        self.rect = pygame.Rect(150, 150, 50, 75)


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))
manager = pygame_gui.UIManager((800, 600), 'data/themes/quick_theme.json')

background = pygame.Surface((800, 600))
background.fill(manager.ui_theme.get_colour('dark_bg'))


healthy_sprite = HealthySprite()

ss_health_bar = pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect(100, 500,
                                                                                     150, 30),
                                                           sprite_to_monitor=healthy_sprite,
                                                           manager=manager)


clock = pygame.time.Clock()
is_running = True
debug_mode = False

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                debug_mode = False if debug_mode else True
                manager.set_visual_debug_mode(debug_mode)

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

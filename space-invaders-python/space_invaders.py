import pygame
from pygame.sprite import Group

from settings import Settings, Background
from game_stats import GameStats
from inscription import Inscription
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init
    si_settings = Settings()
    screen = pygame.display.set_mode(
        (si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    play_button = Inscription(si_settings, screen, "Press space to play")
    stats = GameStats(si_settings)
    bg = Background('bg.png', [0, 0])
    ship = Ship(si_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(si_settings, screen, ship, aliens)
    pygame.mouse.set_visible(False)

    while True:
        gf.check_events(si_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(si_settings, screen, ship, aliens, bullets)
            gf.update_aliens(si_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(screen, stats, bg, ship, aliens, bullets, play_button)


run_game()

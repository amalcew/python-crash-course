import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, si_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, si_settings.bullet_width, si_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = si_settings.bullet_color
        self.speed_factor = si_settings.bullet_speed_factor

    def update(self):
        """Bullet movement up the screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

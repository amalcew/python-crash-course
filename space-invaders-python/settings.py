import pygame

class Background:

    def __init__(self, image_file, location):
        """Background settings initialization"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Settings:

    def __init__(self):
        """Statistic data settings initialization"""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 800

        #ship settings
        self.ship_limit = 1

        #ship's laser settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 1

        #aliens settings
        self.fleet_drop_speed = 20

        #game speed settings
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 9
        self.bullet_speed_factor = 22
        self.alien_speed_factor = 1.1

        self.fleet_direction = 1  # 1 - right / -1 - left

    def increase_speed(self):
        """Change of dynamic settings"""
        #self.ship_speed_factor *= self.speedup_scale
        #self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


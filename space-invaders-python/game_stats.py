class GameStats():
    """Statistic data monitoring"""

    def __init__(self, si_settings):
        """Statistic data initialization"""
        self.si_settings = si_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.si_settings.ship_limit

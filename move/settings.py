class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship moving speed settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        self.bullet_speed = 3
        self.bullet_width = 6
        self.bullet_height = 60
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.cone1_speed = 1.2
        self.cone1_frequency = 0.003
        self.cone2_speed = 1.2
        self.cone2_frequency = 0.0035
        self.cone3_speed = 1.2
        self.cone3_frequency = 0.003

        self.road_speed = 1.2
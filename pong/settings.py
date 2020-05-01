class Settings:
    """A class to store all settings for Pong."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 205, 50)

        # Racket settings
        self.racket_speed = 1.5

        # Bullet settings
        self.ball_speed = 1.0
        self.balls_allowed = 1
        self.ball_color = ( 255,255,255)

        # Scoring
        self.alien_points = 50
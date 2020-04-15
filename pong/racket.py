import os, sys
import pygame

class Racket:
    """A Class to manage the left racket."""

    def __init__(self, ai_game,img, position):
        """Initialize the racket and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the ship image and get its rect.      
        APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
        full_path = os.path.join(APP_FOLDER, img)    
        self.image = pygame.image.load(full_path)        
        self.rect = self.image.get_rect()

        # Start each new racket at the left or right  depending on position
        if position == "left":
            self.rect.topleft = self.screen_rect.topleft
        if position == "right":
            self.rect.bottomright = self.screen_rect.bottomright

        # Store a decimal value for the rackets's vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the racket's position based on the movement flag."""
        if self.moving_up  and self.rect.top > 0:
            self.y -= self.settings.racket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.racket_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the racket at its current location."""
        self.screen.blit(self.image, self.rect)

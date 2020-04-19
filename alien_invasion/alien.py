import os, sys
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its rect attribute
        APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
        full_path = os.path.join(APP_FOLDER,"images/alien.bmp")    
        self.image = pygame.image.load(full_path)
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
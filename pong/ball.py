import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """ A class to manage balls fired from a racket"""

    def __init__(self, ai_game):
        """ Create a ball object at the racket's current position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        
        # Load the ball image and get its rect.      
        APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
        full_path = os.path.join(APP_FOLDER, "images/ball.bmp")    
        self.image = pygame.image.load(full_path)        
        self.rect = self.image.get_rect()

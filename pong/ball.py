import os, sys
import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """ A class to manage balls fired from a racket"""

    def __init__(self, ai_game):
        """ Create a ball object at the racket's current position"""
        
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.ball_color
        
        
        # Load the ball image and get its rect.      
        APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
        full_path = os.path.join(APP_FOLDER, "images/ball.bmp")    
        self.image = pygame.image.load(full_path)        
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.left_racket.rect.midtop

        # Store the balls's position as a decimal value
        self.x = float(self.rect.x)

    
    def update(self):
        """Move the ball horizontally the screen"""
        # Update the decimal position of the ball
        self.x += self.settings.ball_speed

        # Update the rect position.
        self.rect.x = self.x

    def draw_ball(self):
        """Draw the ball to the screen."""
        #pygame.draw.rect(self.screen, self.rect)
        self.screen.blit(self.image, self.rect)
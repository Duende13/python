import sys

import pygame
# py -m pip install -U pygame --user

from settings import Settings
from racket import Racket
from ball import Ball

class Pong:
    """Overall class to manage game assets and behavior. """

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # To set the FULLSCREEN mode, not interested right now
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height


        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("Pong")

        self.left_racket = Racket(self, "images/red_racket.bmp","left")
        self.right_racket = Racket(self, "images/blue_racket.bmp","right")
        self.balls = pygame.sprite.Group()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.right_racket.update()
            self.left_racket.update()
            self._update_balls()
            # Make the most recently drawn sreen visible
            self._update_screen()

    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):        
        if event.key == pygame.K_UP:
            self.right_racket.moving_up = False
        if event.key == pygame.K_q:
            self.left_racket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.right_racket.moving_down = False
        if event.key == pygame.K_a:
            self.left_racket.moving_down = False

    def _check_keydown_events(self, event):
        """ Respond to keypresses"""
        if event.key == pygame.K_UP:
            # Move the right racket up
            self.right_racket.moving_up = True
        elif event.key == pygame.K_q:
            # Move the left racket up
            self.left_racket.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the right racket down
            self.right_racket.moving_down = True
        elif event.key == pygame.K_a:
            # Move the left racket down
            self.left_racket.moving_down = True
        elif event.key == pygame.K_x:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._shoot_ball()

    def _shoot_ball(self):
        """ Create a new ball and add it to the balls group"""
        if len(self.balls) < self.settings.balls_allowed:
            new_ball =  Ball(self)
            self.balls.add(new_ball)

    def _update_balls(self):
        """Update position of balls and get rid of the old balls"""
        # Update ball position
        self.balls.update()

        # Get rid of balls that have disappeared
        for ball in self.balls.copy():
            if ball.rect.right >= self.screen.get_rect().right:
                self.balls.remove(ball)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.left_racket.blitme()
        self.right_racket.blitme()

        for ball in self.balls.sprites():
            ball.draw_ball()

        # Make the most recently drawn sreen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Pong()
    ai.run_game()

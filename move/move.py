import sys
import pygame
from pygame.locals import *
from Bullet import Bullet
from settings import Settings
from car import Car

class FinalGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # # set the screen, upload, display the picture
        # screen = pygame.display.set_mode((screen_width, screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        # pic = pygame.image.load("images/forest.png")
        # screen.blit(pygame.transform.scale(pic, (screen_width, screen_height)), (0, 0))
        # pygame.display.flip()


        # self.screen = pygame.display.set_mode((1200, 600))#, pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200, 600), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.pic = pygame.image.load("images/route.png")

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("FinalGame")

        self.car = Car(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.car.update()
            self._update_screen()
            self._update_bullets()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        # to move the ship left and right
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = True
        #insert lines of codes to move the ship up and down
        if event.key == pygame.K_UP:
             self.car.moving_up = True
        elif event.key == pygame.K_DOWN:
             self.car.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = False
        #insert lines of codes to handle response to key up and down releases
        if event.key == pygame.K_UP:
             self.car.moving_up = False
        elif event.key == pygame.K_DOWN:
             self.car.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(pygame.transform.scale(self.pic, (self.settings.screen_width, self.settings.screen_height)), (0, 0))
        self.car.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = FinalGame()
    ai.run_game()

import sys
import pygame

from Bullet import Bullet
from settings import Settings
from car import Car
from cone import Cone1
from cone import Cone2
from cone import Cone3
from random import random
import Sound as se


class FinalGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()


        # self.screen = pygame.display.set_mode((1200, 600))#, pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.pic = pygame.image.load("images/route.png")


        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.pic = pygame.transform.scale(self.pic, (self.settings.screen_width, self.settings.screen_height))
        self.i = self.settings.screen_height
        pygame.display.set_caption("FinalGame")

        self.car = Car(self)
        self.bullets = pygame.sprite.Group()
        self.cone1 = pygame.sprite.Group()
        self.cone2 = pygame.sprite.Group()
        self.cone3 = pygame.sprite.Group()
        self.WIDTH = self.settings.screen_width
        self.HEIGHT = self.settings.screen_height
        se.background_sound.play()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.car.update()
            self._update_screen()
            self._update_bullets()
            self._update_cone1s()
            self._update_cone2s()
            self._update_cone3s()
            self._createcone1_fleet()
            self._createcone2_fleet()
            self._createcone3_fleet()

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
            se.bullet_sound.play()
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

    def _createcone1_fleet(self):
        if random() < self.settings.cone1_frequency:
            cone = Cone1(self)
            self.cone1.add(cone)

    def _createcone2_fleet(self):
        if random() < self.settings.cone2_frequency:
            cone = Cone2(self)
            self.cone2.add(cone)

    def _createcone3_fleet(self):
        if random() < self.settings.cone3_frequency:
            cone = Cone3(self)
            self.cone3.add(cone)


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.cone1, True, True)
        collisions = pygame.sprite.groupcollide(self.bullets, self.cone2, True, True)
        collisions = pygame.sprite.groupcollide(self.bullets, self.cone3, True, True)

    def _update_cone1s(self):
        self.cone1.update()
        if pygame.sprite.spritecollideany(self.car, self.cone1):
            print("Crash!")
            collisions = pygame.sprite.groupcollide(self.car, self.cone1, True, True)

    def _update_cone2s(self):
        self.cone2.update()
        if pygame.sprite.spritecollideany(self.car, self.cone2):
            print("Crash!")
            collisions = pygame.sprite.groupcollide(self.car, self.cone2, True, True)

    def _update_cone3s(self):
        self.cone3.update()
        if pygame.sprite.spritecollideany(self.car, self.cone3):
            print("Crash!")
            collisions = pygame.sprite.groupcollide(self.car, self.cone3, True, True)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill(self.settings.bg_color)
        self.screen.fill((0,0,0))
        # self.i -= self.settings.cone1_speed
        self.i -= self.settings.road_speed

        val = self.settings.screen_height - self.i
        val = val % self.settings.screen_height
        val2 = val - int(1 * self.settings.screen_height)
        self.screen.blit(self.pic, (0,  val))
        self.screen.blit(self.pic, (0, val2))
        self.car.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # self.cone.create_cone()
        self.cone1.draw(self.screen)
        self.cone2.draw(self.screen)
        self.cone3.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = FinalGame()
    ai.run_game()

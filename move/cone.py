import pygame
from pygame.sprite import Sprite
from random import randint
from settings import Settings
import sys

class Cone1(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/cone.bmp')
        self.image = pygame.transform.scale(self.image, (120, 120))
        # cone_width = 120
        # cone_height = 120
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,500)
        self.rect.y = 0
        # self.rect.bottomleft = self.screen_rect.topleft

    #     self.x, self.y = self.screen.get_size()
    #
    #     self.image_x = 0
    #     self.image_y = 100
    #
    # def create_cone(self):
    #     self.screen.blit(self.image, (self.image_x, self.image_y))

        # self.rect.midtop = self.screen_rect.midtop

        self.x = float(self.rect.x)

        self.y = float(self.rect.y)

        self.settings = ai_game.settings

    def update(self):
        self.y += self.settings.cone1_speed
        self.rect.y = self.y

class Cone2(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/cone.bmp')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = randint(500, 1000)
        self.rect.y = 0
        # self.rect.midbottom = self.screen_rect.midtop
        self.x = float(self.rect.x)

        self.y = float(self.rect.y)

        self.settings = ai_game.settings

    def update(self):
        self.y += self.settings.cone2_speed
        self.rect.y = self.y

class Cone3(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/cone.bmp')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = randint(1000, 1500)
        self.rect.y = 0
        # self.rect.bottomright = self.screen_rect.topright
        self.x = float(self.rect.x)

        self.y = float(self.rect.y)

        self.settings = ai_game.settings

    def update(self):
        self.y += self.settings.cone3_speed
        self.rect.y = self.y


        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        #
        # self.x = float(self.rect.x)

# pygame.init()
# ai_settings = Settings()
# screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
# pygame.display.set_caption("FinalGame")
#
# image = pygame.image.load('images/cone.bmp')
# rect = image.get_rect()
# screen_rect = screen.get_rect()
#
# rect.centerx = screen_rect.centerx
# rect.bottom = screen_rect.centery
#
# # screen.fill(ai_settings.bg_color)
#
# screen.blit(image, rect)
#
# pygame.display.flip()
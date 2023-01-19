import pygame
import math
import random
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self.layer = player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x* tile_size
        self.y = y* tile_size
        self.width = tile_size
        self.height = tile_size

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(colour_orange)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass

import pygame
from randomcode import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path):
        super().__init__(groups)
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect(topleft = pos)

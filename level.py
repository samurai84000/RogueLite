import pygame
from randomcode import *
from tile import Tile
from Player import Player

class Level:
    def __init__(self):
        #function to get display surface
        self.display_surface = pygame.display.get_surface()
        self.visable_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.createMap()

    def createMap(self):
        for row_index, row in enumerate(ROOM1_MAP):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                if col == 'w':
                    Tile((x,y), [self.visable_sprites, self.obstacle_sprites], 'Graphics/wall.png')
                if col == 'c':
                    self.player = Player((x,y), [self.visable_sprites], self.obstacle_sprites)
                if col == 'p':
                    Tile((x,y), [self.visable_sprites, self.obstacle_sprites], 'Graphics/water1.png')

    def run(self):
        self.visable_sprites.custom_draw()
        self.visable_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)

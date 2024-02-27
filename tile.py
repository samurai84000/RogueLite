import pygame
from randomcode import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path, priority):
        super().__init__(groups)
        self.obstaclesprites = groups[1]
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-20, -20)
        self.priority = priority


class door(Tile):
    def __init__(self, enemycounter, pos, groups, path, priority):
        super().__init__(pos, groups, path, priority)
        self.pos = pos
        self.enemycounter = enemycounter
        self.isopen = True
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)
        self.priority = priority


    def checkEnemies(self):
        if self.enemycounter >= 1:
            self.isopen = False
            self.image = pygame.image.load('Graphics/closeddoor.png')
        else:
            self.isopen = True
            self.obstaclesprites.remove(self.rect)
            self.image = pygame.image.load('Graphics/opendoor.png')
    def updateImage(self, path):
        self.image = pygame.image.load(path).convert()


class SpawnTile(Tile):
    def __init__(self, pos, groups, path, roomNumber, doornumber, priority):
        super().__init__(pos, groups, path,priority)
        self.visableSprites = groups[0]
        self.nonObstacleTiles = groups[1]
        self.path = path
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.roomNumber = roomNumber
        self.doornumber = doornumber
        self.hitbox = self.rect.inflate(-20, -20)
        self.priority = priority


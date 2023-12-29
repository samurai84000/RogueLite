import pygame
import math

class projectile(pygame.sprite.Sprite):
    def __init__(self, bulletStartPosition, cursorPosition, speed, damage, bulletImage, bulletID):
        super().__init__()
        self.cursorPosition = cursorPosition
        self.bulletStartPosition = bulletStartPosition
        self.speed = speed
        self.damage = damage
        self.bulletID = bulletID


        self.window = pygame.display.get_surface()

        #attempt 2
        self.angle = math.atan2(self.cursorPosition[1] - self.bulletStartPosition[1], self.cursorPosition[0] - self.bulletStartPosition[0])
        self.dx = math.cos(self.angle) * speed
        self.dy = math.sin(self.angle) * speed
        self.tempx = bulletStartPosition[0]
        self.tempy = bulletStartPosition[1]

        self.image = pygame.image.load(bulletImage).convert_alpha()
        self.image = pygame.transform.rotate(self.image, -  (self.angle * 180 / math.pi))
        self.rect = self.image.get_rect(center=(bulletStartPosition[0], bulletStartPosition[1]))


    def calculatetrajectory(self):
        #calculate the slope/vector of the bullet
        self.normvector.calculateNormMagnitude()
        
    def move(self):
        self.tempx = self.tempx + int(self.dx)
        self.tempy = self.tempy + int(self.dy)

        self.rect.x = int(self.tempx)
        self.rect.y = int(self.tempy)

    def draw(self):
        self.window.blit(self.image, self.rect)
        
    def update(self):
        self.move()
        self.draw()

    def getDamage(self):
        return self.damage
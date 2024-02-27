import pygame
import math

class projectile(pygame.sprite.Sprite):
    def __init__(self, bulletStartPosition, target, speed, damage, bulletImage):
        super().__init__()
        self.cursorPosition = target
        self.bulletStartPosition = bulletStartPosition
        self.speed = speed
        self.damage = damage

        self.captured_startposx = bulletStartPosition[0]
        self.captured_startposy = bulletStartPosition[1]

        self.captured_targetx = target[0]
        self.captured_targety = target[1]

        self.saved_startposx = self.captured_startposx
        self.saved_startposy = self.captured_startposy

        self.saved_targetx = self.captured_targetx
        self.saved_targety = self.captured_targety


        self.window = pygame.display.get_surface()

        #attempt 2
        self.angle = math.atan2(self.saved_targety - self.saved_startposy, self.saved_targetx - self.saved_startposx)
        self.dx = math.cos(self.angle) * speed
        self.dy = math.sin(self.angle) * speed
        self.tempx = self.saved_startposx
        self.tempy = self.saved_startposy

        self.image = pygame.image.load(bulletImage).convert_alpha()
        self.image = pygame.transform.rotate(self.image, -  (self.angle * 180 / math.pi))
        self.rect = self.image.get_rect(center=(self.saved_startposx, self.saved_startposy))


    def calculatetrajectory(self):
        #calculate the slope/vector of the bullet
        self.normvector.calculateNormMagnitude()

    def move(self):
        self.tempx = self.tempx + int(self.dx)
        self.tempy = self.tempy + int(self.dy)
        self.rect.x += int(self.dx)
        self.rect.y += int(self.dy)

    def draw(self):
        self.window.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()

    def getDamage(self):
        return self.damage
    def getrect(self):
        return self.rect
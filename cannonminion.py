import pygame
from enemy import enemy
from projectile import projectile

class cannon(enemy):
    def __init__(self, startposition, health, damage, imagepath, groups,obstacle_sprites, playercoords, priority):
        super().__init__(startposition, health, damage, imagepath, groups,obstacle_sprites, playercoords, priority)

        self.window = pygame.display.get_surface()
        self.image = pygame.image.load(imagepath).convert_alpha()
        self.rect = self.image.get_rect(topleft=startposition)
        self.obstacle_sprites = obstacle_sprites
        self.priority = priority

        self.health = health
        self.damage = damage

        self.projectiles = []

        self.playercoords = playercoords
        self.attackcounter = 0
        self.framecounter = 0

        self.canmove = False


    def move(self):
        if self.playercoords[0] < self.rect.x:
            self.rect.x = self.rect.x - 1
        elif self.playercoords[0] > self.rect.x:
            self.rect.x = self.rect.x + 1
        else:
            pass

        if self.playercoords[1] < self.rect.y:
            self.rect.y = self.rect.y - 1
        elif self.playercoords[1] > self.rect.y:
            self.rect.y = self.rect.y + 1
        else:
            pass


    def attack(self):
        attack = projectile((self.rect.centerx, self.rect.centery),
                            (self.playercoords), 8, 1,
                            "Graphics/blueminionauto.png")
        self.projectiles.append(attack)
        self.attackcounter = 0


    def update(self):
        self.togglemovement()
        if self.canmove:
            self.move()
        if self.attackcounter >= 120:
            self.attack()
        self.drawProjectiles()
        self.updateframecounters()


    def drawProjectiles(self):
        projectiles_to_remove = []

        for projectile in self.projectiles:
            projectile.update()

            for obstacle in self.obstacle_sprites:
                if projectile.rect.colliderect(obstacle.rect):
                    projectiles_to_remove.append(projectile)

        # Create a new list without the projectiles to be removed
        self.projectiles = [projectile for projectile in self.projectiles if projectile not in projectiles_to_remove]


    def setPlayerCoords(self, newplayercoords):
        self.playercoords = newplayercoords


    def updateframecounters(self):
        self.framecounter += 1
        self.attackcounter += 1


    def togglemovement(self):
        if self.framecounter >= 60:
            self.canmove = not self.canmove
            self.framecounter = 0



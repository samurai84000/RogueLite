import pygame, Player
from projectile import projectile



class enemy(pygame.sprite.Sprite):
    def __init__(self, startposition, health, damage, imagepath, groups,obstacle_sprites, playercoords, priority):
        super().__init__(groups)
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
            self.rect.x = self.rect.x -1
        elif self.playercoords[0] > self.rect.x:
            self.rect.x = self.rect.x +1
        else:
            pass

        if self.playercoords[1] < self.rect.y:
            self.rect.y = self.rect.y-1
        elif self.playercoords[1] > self.rect.y:
            self.rect.y = self.rect.y +1
        else:
            pass

    def attack(self):

        captured_targetx = self.playercoords[0]
        captured_targety = self.playercoords[1]

        saved_targetx = captured_targetx
        saved_targety = captured_targety
        attack = projectile((self.rect.centerx, self.rect.centery),
                            (saved_targetx, saved_targety), 8, 1,
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

    def checkCollision(self):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.moveleft:
                        self.rect.left = sprite.rect.right
                    if self.moveRight:
                        self.rect.right = sprite.rect.left

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.moveUp:
                        self.rect.top = sprite.rect.bottom
                    if self.moveDown:
                        self.rect.bottom = sprite.rect.top


    def drawProjectiles(self):
        projectiles_to_remove = []
        for projectile in self.projectiles:
            projectile.update()
            for obstacle in self.obstacle_sprites:
                if projectile.rect.colliderect(obstacle.rect):
                    projectiles_to_remove.append(projectile)

                # Draw projectile directly on the main display surface
            self.window.blit(projectile.image, projectile.rect.topleft)

            # Create a new list without the projectiles to be removed
        self.projectiles = [projectile for projectile in self.projectiles if projectile not in projectiles_to_remove]

    def setPlayerCoords(self, newplayercoords):
        self.playercoords = newplayercoords

    def updateframecounters(self):
        self.framecounter+=1
        self.attackcounter+=1

    def togglemovement(self):
        if self.framecounter >= 60:
            self.canmove = not self.canmove
            self.framecounter = 0







import pygame
from projectile import projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, startpos, groups, obstacle_sprites):
        super().__init__(groups)
        self.window = pygame.display.get_surface()
        self.image = pygame.image.load('Graphics/biggerGravesIdle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = startpos)
        self.obstacle_sprites = obstacle_sprites




        self.mouseImage = pygame.image.load('Graphics/crosshair.png').convert_alpha()
        self.mouseImage = pygame.transform.scale(self.mouseImage, self.mouseImage.get_size())
        pygame.mouse.set_visible(False)

        self.bulletImage = pygame.image.load('Graphics/bullet.png').convert_alpha()
        self.bulletImage = pygame.transform.scale(self.bulletImage, self.bulletImage.get_size())


        self.projectiles = []
        self.capturedMouseCoordinates = 0

        self.bulletID = 0


        #Movement Variables
        self.moveleft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        self.fireable = 0
        
        self.velocityX = 0
        self.velocityY = 0

        self.direction = pygame.math.Vector2()
        self.baseSpeed = 3

        self.framecounter = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * self.baseSpeed
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.baseSpeed
        self.collision('vertical')


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.moveUp = True
            self.moveDown = False
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.moveUp = False
            self.moveDown = True
        else:
            self.direction.y = 0
            self.moveUp = False
            self.moveDown = False

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.moveRight = True
            self.moveleft = False
            self.image = self.image = pygame.image.load('Graphics/GravesStartRightFacing.png').convert_alpha()
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.moveleft = True
            self.moveRight = False
            self.image = self.image = pygame.image.load('Graphics/GravesStartLeftFacing.png').convert_alpha()
        else:
            self.direction.x = 0
            self.moveleft = False
            self.moveRight = False

        if keys[pygame.K_SPACE]:
            if self.fireable >= 20:
                self.capturedMouseCoordinates = pygame.mouse.get_pos()
                self.attack()
                self.fireable = 0




    def getCursorLocation(self):
        mousepos = pygame.mouse.get_pos()
        self.window.blit(self.mouseImage, mousepos)
        self.cursorPositionInstance = mousepos

    def update(self):
        self.input()
        self.updateBullets()
        self.move()
        self.getCursorLocation()


        if self.framecounter >= 120:
            self.framecounter = 0
        if self.fireable < 20:
            self.fireable += 1

    def collision(self, direction):
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

    def attack(self):
        bullet = projectile((self.rect.centerx, self.rect.centery), (self.capturedMouseCoordinates[0], self.capturedMouseCoordinates[1]), 20, 10, "Graphics/bullet.png", self.bulletID)
        self.bulletID += 1
        self.projectiles.append(bullet)

    def updateBullets(self):
        projectiles_to_remove = []

        for projectile in self.projectiles:
            projectile.update()

            for obstacle in self.obstacle_sprites:
                if projectile.rect.colliderect(obstacle.rect):
                    projectiles_to_remove.append(projectile)

        # Create a new list without the projectiles to be removed
        self.projectiles = [projectile for projectile in self.projectiles if projectile not in projectiles_to_remove]





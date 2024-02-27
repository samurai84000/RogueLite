import math
from tile import SpawnTile
import pygame
from projectile import projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, startpos, health, groups, obstacle_sprites, priority):
        super().__init__(groups)
        self.window = pygame.display.get_surface()
        self.image = pygame.image.load('Graphics/biggerGravesIdle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = startpos)
        self.obstacle_sprites = obstacle_sprites
        self.priority = priority


        self.mouseImage = pygame.image.load('Graphics/crosshair.png').convert_alpha()
        self.mouseImage = pygame.transform.scale(self.mouseImage, self.mouseImage.get_size())
        pygame.mouse.set_visible(False)


        self.bulletImage = pygame.image.load('Graphics/bullet.png').convert_alpha()
        self.bulletImage = pygame.transform.scale(self.bulletImage, self.bulletImage.get_size())


        self.projectiles = []
        self.capturedMouseCoordinates = []

        self.health = health




        #Movement Variables
        self.moveleft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.isRolling = False

        self.facingRight = False
        self.facingLeft = False
        self.facingDown = False
        self.facingUp = False

        self.velocityX = 0
        self.velocityY = 0
        self.baseSpeed = 3
        self.direction = pygame.math.Vector2()

        self.fireable = 0

        self.rolldelayframes = 30
        self.rollFrameCounter = 0
        self.framecounter = 0

        self.initalx = 0
        self.initaly = 0

    #'Graphics/biggerGravesIdle.png' 'Graphics/GravesDodgeRollRight.png'
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        if self.isRolling:
            # Set individual components based on movement keys
            horizontal_movement = 0
            vertical_movement = 0

            if self.moveUp:
                vertical_movement = -2 * self.baseSpeed
                self.image = pygame.image.load('Graphics/GravesDodgeRollUp.png')
            elif self.moveDown:
                vertical_movement = 2 * self.baseSpeed
                self.image = pygame.image.load('Graphics/GravesDodgeRollDown.png')

            if self.moveRight:
                horizontal_movement = 2 * self.baseSpeed
                self.image = pygame.image.load('Graphics/GravesDodgeRollRight.png')
            elif self.moveleft:
                horizontal_movement = -2 * self.baseSpeed
                self.image = pygame.image.load('Graphics/GravesDodgeRollLeft.png')

            self.direction.x = horizontal_movement
            self.direction.y = vertical_movement

            #check for diagonal movement, which means the magnitude must be normalized [] vs o
            if self.direction.x != 0 and self.direction.y != 0:
                self.direction = self.direction.normalize() * 2 * self.baseSpeed


            # Set the direction vector based on individual component
            self.rect.centerx += self.direction.x
            self.collision('horizontal')
            self.rect.centery += self.direction.y
            self.collision('vertical')
            self.rollFrameCounter += 1

            if self.rollFrameCounter >= 25:
                self.rollFrameCounter = 0
                if self.moveRight:
                    self.image = pygame.image.load('Graphics/GravesStartRightFacing.png')

                elif self.moveleft:
                    self.image = pygame.image.load('Graphics/GravesStartLeftFacing.png')

                elif self.moveUp:
                    self.image = pygame.image.load('Graphics/biggerGravesIdle.png')

                elif self.moveDown:
                    self.image = pygame.image.load('Graphics/biggerGravesIdle.png')
                else:
                    self.image = pygame.image.load('Graphics/biggerGravesIdle.png')
                self.rolldelayframes = 0
                self.isRolling = False
        else:
            # Update position based on direction
            self.rect.centerx += self.direction.x * self.baseSpeed
            self.collision('horizontal')
            self.rect.centery += self.direction.y * self.baseSpeed
            self.collision('vertical')


    def input(self):
        keys = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[2] and not self.isRolling and self.rolldelayframes >= 30:
            self.isRolling = True
        elif not self.isRolling:
            self.initalx = self.rect.centerx
            self.initaly = self.rect.centery
            if self.rolldelayframes >= 30:
                self.rolldelayframes = 30
            else:
                self.rolldelayframes +=1
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
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.moveleft = True
                self.moveRight = False
                self.image = self.image = pygame.image.load('Graphics/GravesStartLeftFacing.png').convert_alpha()

            else:
                self.moveleft =False
                self.moveRight = False
                self.direction.x = 0

            if pygame.mouse.get_pressed()[0]:
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
        if not self.isRolling:
            self.setImageDirection()
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
        bullet = projectile((self.rect.centerx, self.rect.centery),
                            (self.capturedMouseCoordinates[0], self.capturedMouseCoordinates[1]), 20, 1,
                            "Graphics/bullet.png")
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

    def setImageDirection(self):
        if pygame.mouse.get_pos()[0] < self.rect.centerx:
            self.facingLeft = True
            self.facingRight = False
            self.image = pygame.image.load('Graphics/GravesStartLeftFacing.png')
        elif pygame.mouse.get_pos()[0] > self.rect.centerx:
            self.facingRight = True
            self.facingLeft = False
            self.image = pygame.image.load('Graphics/GravesStartRightFacing.png')

    def playerTeleport(self, x, y):
        self.rect.topleft = (x,y)





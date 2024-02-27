import pygame
from randomcode import *
from tile import *
from Player import Player
from enemy import enemy
from projectile import projectile
from cannonminion import cannon
from LevelCreator import LevelCreator

class Level:
    def __init__(self):
        #function to get display surface
        self.enemys = []
        self.doors = []
        self.enemyprojectiles = []
        self.playerprojectiles = []
        self.deadenemyprojectiles = []
        self.display_surface = pygame.display.get_surface()

        self.obstacle_sprites = pygame.sprite.Group()
        self.entity_sprites = pygame.sprite.Group()
        self.non_obstacle_floor_sprites = pygame.sprite.Group()
        self.visable_sprites = YSortCameraGroup(self.entity_sprites, self.obstacle_sprites,  self.non_obstacle_floor_sprites)


        self.player = Player((7744,7744), 10, [self.visable_sprites], self.obstacle_sprites, 2)
        self.LevelCreator = LevelCreator(3)
        self.firstrunthroughlevelcreator = True
        self.temp = 1
        self.enemys = []

    def run(self):
        if self.firstrunthroughlevelcreator:
            self.firstrunthroughlevelcreator = False
            self.createmap()
        self.visable_sprites.custom_draw(self.player, self.enemys)
        self.visable_sprites.update()
        self.checkCollisions()
        self.checkDoorStatus(self.doors, self.enemys, self.obstacle_sprites)
        self.checkSpawning()

        if len(self.enemys) !=0:
            for enemy in self.enemys:
                enemy.setPlayerCoords(self.player.rect.center)

        removeenemy = []
        if len(self.enemys) != 0:
        
            for enemy in self.enemys:
                if enemy.health <= 0:
                    removeenemy.append(enemy)
                    self.visable_sprites.remove(enemy)
                self.enemys = [enemy for enemy in self.enemys if enemy not in removeenemy]

        if len(removeenemy) !=0:
            for enemy in removeenemy:
                for projectile in enemy.projectiles:
                    self.enemyprojectiles.append(projectile)
        removeenemy.clear()
            

    def checkCollisions(self):
        self.projectileCollisionAndRemovalForEnemys(self.player, self.enemys)
        self.projectileCollisionAndRemovalForPlayer(self.player, self.enemys)


    def checkSpawning(self):

        for sprite in self.non_obstacle_floor_sprites:
            if sprite.rect.colliderect(self.player.rect):
                spawnroomnumber = sprite.roomNumber
                if not self.LevelCreator.rooms[int(spawnroomnumber) - 1].hasSpawned:
                    print("SPAWNTILE TOP LEFT", sprite.rect.topleft, "Door counter = ", sprite.doornumber)
                    self.spawnEnemys(self.LevelCreator.rooms[int(spawnroomnumber) - 1],
                                     self.visable_sprites, self.obstacle_sprites, self.player, self.enemys, sprite.doornumber)



    def spawnEnemys(self, room, visable_sprites, obstacle_sprites, player, enemys, doornumber):
        room.hasSpawned = True
        x = 0
        y = 0
        if doornumber <= 2:
            x = player.rect.topleft[0] - 384
            y = player.rect.topleft[1] + 64
        elif (doornumber == 3) or (doornumber == 5) or (doornumber == 7):
            x = player.rect.topleft[0] + 64
            y = player.rect.topleft[1] - 310
        elif (doornumber == 4) or (doornumber == 6) or (doornumber == 8):
            print("ELIF 2")
            x = player.rect.topleft[0] - 768
            y = player.rect.topleft[1] - 310
        else:
            print("here")
            x = player.rect.topleft[0] - 256
            y = player.rect.topleft[1] - 640



        for row_index, row in enumerate(room.enemyspawns):
            for col_index, col in enumerate(row):
                i = x + (col_index * 64)
                j = y + (row_index * 64)

                if col == 'm':
                    temp = enemy((i,j), 3, 1, 'Graphics/minion.png', visable_sprites, obstacle_sprites,
                                 player.rect.center, 2)
                    enemys.append(temp)

                elif col == 'l':
                    temp = cannon((i, j), 6, 1, 'Graphics/cannonminion.png', visable_sprites,
                                  obstacle_sprites,
                                  player.rect.center, 2)
                    enemys.append(temp)




    def checkDoorStatus(self, doors, enemys, obstacle_sprites):
        for door in doors:
            door.enemycounter = len(enemys)
        if len(enemys) <= 0:
            for door in doors:
                door.updateImage('Graphics/opendoor.png')
                self.display_surface.blit(door.image, door.rect.topleft)
                obstacle_sprites.remove(door)

        else:
            for door in doors:
                door.updateImage('Graphics/closeddoor.png')
                self.display_surface.blit(door.image, door.rect.topleft)
                obstacle_sprites.add(door)


    def projectileCollisionAndRemovalForEnemys(self, player, enemys):
        removeprojectile = []
        if not player.isRolling:
            for enemy in enemys:
                if len(enemy.projectiles) != 0:
                    for projectile in enemy.projectiles:
                        if player.rect.colliderect(projectile.getrect()):
                            player.health -= projectile.damage
                            removeprojectile.append(projectile)
                enemy.projectiles = [projectile for projectile in enemy.projectiles if
                                     projectile not in removeprojectile]

    def projectileCollisionAndRemovalForPlayer(self, player, enemys):
        removeprojectile = []
        if len(player.projectiles) != 0:
            for enemy in enemys:
                for projectile in player.projectiles:
                    if enemy.rect.colliderect(projectile.getrect()):
                        enemy.health -= projectile.damage
                        removeprojectile.append(projectile)
        player.projectiles = [projectile for projectile in player.projectiles if projectile not in removeprojectile]



    def createmap(self):
        for room in self.LevelCreator.rooms:
            self.createRoom(room.topleft[0], room.topleft[1], room, self.visable_sprites, self.obstacle_sprites, self.player, self.enemys)
    
    def createRoom(self, startX, startY, room, visable_sprites, obstacle_sprites, player, enemys):
        startx = startX * 64
        starty = startY * 64
        doorcounter = 0
        for row_index, row in enumerate(room.layout):
            for col_index, col in enumerate(row):
                x = startx + (col_index * 64) + room.topleft[0] * 64 *4
                y = starty + (row_index * 64) + room.topleft[1] * 64 *4
                if col == 'd':
                    temp = door(enemycounter=len(self.enemys), pos=(x, y),
                                groups=[visable_sprites, obstacle_sprites],
                                path='Graphics/closeddoor.png', priority=1)
                    self.doors.append(temp)
                    self.temp = (x, y)

                elif col == 'w':
                    Tile((x, y), [visable_sprites, obstacle_sprites], 'Graphics/wall.png', 1)

                elif col == 'c':
                    print("player", x, y)
                    self.player.rect.topleft = (7744, 7744)


                elif col == 'p':
                    Tile((x, y), [visable_sprites, obstacle_sprites], 'Graphics/water1.png', 2)


                elif col == 'f':
                    pass

                elif col == 'm':
                    temp = enemy((x, y), 1, 1, 'Graphics/minion.png', visable_sprites, obstacle_sprites,
                                 player.rect.center, 2)
                    enemys.append(temp)
                elif col == 'l':
                    temp = cannon((x, y), 1, 1, 'Graphics/cannonminion.png', visable_sprites,
                                  obstacle_sprites,
                                  player.rect.center, 2)
                    self.enemys.append(temp)
                elif col == 's':
                    SpawnTile((x,y), [visable_sprites, self.non_obstacle_floor_sprites], 'Graphics/spawntile.png', room.value, doorcounter, 1)
                    doorcounter+=1
  




class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, visablesprites, obstaclesprites, non_obstacle_floor_sprites):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.obstaclesprites = obstaclesprites
        self.visablesprites = visablesprites
        self.non_obstacle_floor_sprites = non_obstacle_floor_sprites


        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        self.offset = pygame.math.Vector2()


    def custom_draw(self, player, enemy):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for projectile in player.projectiles:
            projectile.rect.topleft = projectile.rect.topleft - self.offset
            self.display_surface.blit(projectile.image, projectile.rect.topleft)

        enemystoremove = []
        if len(enemy) != 0:
            for enemy in enemy:
                for projectile in enemy.projectiles:
                    projectile.rect.topleft = projectile.rect.topleft - self.offset
                    self.display_surface.blit(projectile.image, projectile.rect.topleft)

        spritestoremovep = []
        for sprite in sorted(self.sprites(), key = lambda sprite:sprite.priority):
            sprite.rect.topleft = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, sprite.rect.topleft)





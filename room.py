import pygame

class Room:
    def __init__(self, width, height, doorways, tilemap, enemyspawnmap):
        self.width = width
        self.height = height
        self.doorways = doorways
        self.roomlayout = tilemap
        self.enemyspawnmap = enemyspawnmap
        self.spawnedEnemys = False
        self.doorlocations = []
        self.enemyspawnpplatforms = []
        
    def spawnEnemys(self, startx, starty, enemys):
        if not self.spawnedEnemys:
            for row_index, row in enumerate(self.enemyspawnmap):
                for col_index, col in enumerate(row):
                    x = startX + (col_index * 64) + room.topleftcoordinates[0] * 64 * 5
                    y = starty + (row_index * 64) + room.topleftcoordinates[1] * 64 * 5
                    if col == 'm':
                        temp = enemy((x, y), 10, 1, 'Graphics/minion.png', self.visable_sprites, self.obstacle_sprites,
                                     self.player.rect.center)
                        enemys.append(temp)
                    elif col == 'l':
                        temp = cannon((x, y), 10, 1, 'Graphics/cannonminion.png', self.visable_sprites,
                                      self.obstacle_sprites,
                                      self.player.rect.center)
                        enemys.append(temp)
        self.spawnedEnemys = True
            
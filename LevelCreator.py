import copy
import random
TESTROOM_MAP1 = [
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'd', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 's', 'f', 's', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 's', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],

    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 's', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 's', 'w'],
    ['d', 'f', 's', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 's', 'f', 'd'],
    ['w', 's', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 's', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],

    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 's', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 's', 'f', 's', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'd', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
]

defaultSpawnMap = [
    ['l', 'f', 'f', 'f', 'f', 'f', 's', 'f', 'f', 'f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'l', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],

    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'm', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
    ['s', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 's'],
    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'w', 'f', 'f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],

    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f', 'f', 'f', 's', 'f', 'f', 'f', 'f', 'f', 'f']

]

TESTROOM_MAP_SPAWN = [
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'd', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'c', 'f', 'f', 'f', 'f', 'f', 's', 'm', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],

    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['d', 's', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'l', 'l'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],

    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'l', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'l', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
]


boss_text_layout = [
    [0, 0, 'd', 0, 0],
    [0, 0,  0,  0, 0],
    ['d',   0,  0, 0, 'd'],
    [0, 0,  0,  0, 0],
    [0, 0, 'd', 0, 0]
]


class Door:
    def __init__(self, coords, isConnected, type):
        self.coords = coords
        self.isConnected = isConnected
        self.isOpen = True
        # note 0 = top 1 = left, 2 = right, 3 = bottom
        self.type = type
        self.char = 'd'


class Room:
    def __init__(self, roomtype, value, topleft, layout, enemyspawns, player):
        self.roomtype = roomtype
        self.value = value
        self.topleft = topleft
        self.layout = copy.deepcopy(layout)
        self.enemyspawns = enemyspawns
        self.player = player
        self.hasSpawned = False

        self.doors = [Door((self.topleft[0] + 0, self.topleft[1] + 1), False, 0),
                      Door((self.topleft[0] + 1, self.topleft[1] + 0), False, 1),
                      Door((self.topleft[0] + 1, self.topleft[1] + 2), False, 2),
                      Door((self.topleft[0] + 2,self.topleft[1] + 1), False, 3)]
        self.enemys = []

        self.textlayout = [
            [value, self.doors[0].char, value],
            [self.doors[1].char, value, self.doors[2].char],
            [value, self.doors[3].char, value]
        ]

    def printSpawnMap(self):
        for row in self.enemyspawns:
            print(row)



    def printdoors(self):
        for door in self.doors:
            print(door.type, door.char, door.isConnected)

    def updateLayout(self):
        for door in self.doors:
            if door.char == 'w':
                if door.type == 0:
                    self.layout[7][0] = 'w'

                elif door.type == 1:
                    self.layout[0][7] = 'w'


                elif door.type == 2:
                    self.layout[14][7] = 'w'


                elif door.type == 3:
                    self.layout[7][14] = 'w'
            else:
                if door.type == 0:

                    self.layout[0][7] = 'd'

                elif door.type == 1:
                    self.layout[7][0] = 'd'

                elif door.type == 2:
                    self.layout[14][7] = 'd'

                elif door.type == 3:
                    self.layout[7][14] = 'd'







class LevelCreator:
    def __init__(self, roomCount):
        self.width = 50
        self.height = 50

        self.originallayout = [['-'] * self.width for _ in range(50)]
        self.layout = self.originallayout

        self.startingRoom = Room(1, '1', (round(self.width / 2) - 1, round(self.height / 2) - 1), TESTROOM_MAP_SPAWN, TESTROOM_MAP1, 1)
        self.rooms = [self.startingRoom]
        self.doors = []
        self.counter = 1
        self.toplefts = []
        for door in self.startingRoom.doors:
            self.doors.append(door)

        self.createLevelMacro()


    def createLevelMacro(self):
        self.addRoom(2, 3)
        self.addRoom(3, 3)
        self.addRoom(4, 3)
        self.addRoom(5, 3)
        self.addRoom(6, 3)
        self.addRoom(7, 3)
        self.addRoom(8, 3)
        self.addRoom(9, 3)
        self.addRoom(0, 5)

        self.placeRooms()
        self.checkViableDoors()
        self.updateRoomLayouts()
        self.printmap()


    def updateMap(self):
        for room in self.rooms:
            print(room.value)
            for door in room.doors:
                print(door.type, door.isConnected, door.char)

    def printroomdoors(self):
        for room in self.rooms:
            room.printdoors()
    def updateRoomLayouts(self):
        for room in self.rooms:
            room.updateLayout()

    def placeRooms(self):
        for room in self.rooms:
            for row in range(len(room.textlayout)):
                for col in range(len(room.textlayout[row])):
                    self.layout[room.topleft[0] + row][room.topleft[1] + col] = room.textlayout[row][col]

    def checkViableDoors(self):
        for room in self.rooms:
            for door in room.doors:
                if self.layout[door.coords[0] - 1][door.coords[1]] != 'd' and self.layout[door.coords[0] + 1][door.coords[1]] != 'd' \
                        and self.layout[door.coords[0]][door.coords[1] + 1] != 'd' and self.layout[door.coords[0]][door.coords[1] - 1] != 'd':
                    door.isConnected = False
                    door.char = 'w'
                    self.layout[door.coords[0]][door.coords[1]] = door.char
                else:
                    door.isConnected = True
                    door.char = 'd'
                    self.layout[door.coords[0]][door.coords[1]] = door.char




    def addRoom(self, roomNumber, roomsize):
        validAttempt = False
        randint = -1


        for door in self.doors:
            print(door.isConnected)


        while not validAttempt:
            randint = random.randrange(0, len(self.doors))
            if not self.doors[randint].isConnected:
                validAttempt = True
        door = self.doors[randint]

        # update the doors status in the room it belongs to
        #meaning we switch the door status to connected
        #and switch its textcharacter to letter O
        for room in self.rooms:
            if room.doors.__contains__(door):
                room.doors[door.type].isConnected = True

        self.doors[randint].isConnected = True
        door.isConnected = True

        self.counter += 1
        print(door.type, self.counter)

        if door.type == 0:
                newRoom = Room(2, str(roomNumber), (door.coords[0] - 3, door.coords[1] - 1), TESTROOM_MAP1, defaultSpawnMap, 1)
                newRoom.doors[3].isConnected = True
                newRoom.doors[3].char = 'd'

                self.rooms[len(self.rooms) - 1].doors[0].isConnected = True
                self.create3x3Room(newRoom.topleft[0], newRoom.topleft[1], newRoom, 3)

        elif door.type == 1:
                newRoom = Room(2, str(roomNumber), (door.coords[0] - 1, door.coords[1] - 3), TESTROOM_MAP1, defaultSpawnMap, 1)
                newRoom.doors[2].isConnected = True
                newRoom.doors[2].char = 'd'
                self.rooms[len(self.rooms) - 1].doors[1].isConnected = True
                self.create3x3Room(newRoom.topleft[0], newRoom.topleft[1], newRoom, 2)

        elif door.type == 2:
                newRoom = Room(2, str(roomNumber), (door.coords[0] - 1, door.coords[1] + 1), TESTROOM_MAP1, defaultSpawnMap, 1)
                newRoom.doors[1].isConnected = True
                newRoom.doors[1].char = 'd'
                self.rooms[len(self.rooms) - 1].doors[2].isConnected = True
                self.create3x3Room(newRoom.topleft[0], newRoom.topleft[1], newRoom, 1)

        elif door.type == 3:
                newRoom = Room(2, str(roomNumber), (door.coords[0] + 1, door.coords[1] - 1), TESTROOM_MAP1, defaultSpawnMap, 1)
                newRoom.doors[0].isConnected = True
                newRoom.doors[0].char = 'd'
                self.rooms[len(self.rooms) - 1].doors[3].isConnected = True
                self.create3x3Room(newRoom.topleft[0], newRoom.topleft[1], newRoom, 0)

    def create3x3Room(self, x, y, room, removedoorIndex):
        counter = 0

        #if self.toplefts.__contains__((room.topleft[0], room.topleft[1])):
            #print("ERROEBSBEBSEBVSWLUEVBLISWEUBVFLIEWSUBVL")
        self.toplefts.append((room.topleft[0], room.topleft[1]))
        for i in range(0, 3):
            for j in range(0, 3):
                if abs(i - j) == 1:
                    temp = Door((x + i, y + j), False, counter)
                    room.textlayout[i][j] = 'd'
                    self.layout[i + room.topleft[0]][j + room.topleft[1]] = temp.char
                    if counter != removedoorIndex:
                        self.doors.append(temp)
                        counter += 1
                else:
                    room.textlayout[i][j] = room.value
                    self.layout[i + room.topleft[0]][j + room.topleft[1]] = room.value
        room.doors[removedoorIndex].isConnected = True
        self.checkDoorIsConnected()
        self.updateDoorArray()
        self.rooms.append(room)


    def checkDoorIsConnected(self):
        for room in self.rooms:
            for door in room.doors:
                if self.layout[door.coords[0] - 1][door.coords[1]] == 'd' or self.layout[door.coords[0] + 1][
                    door.coords[1]] == 'd' \
                        or self.layout[door.coords[0]][door.coords[1] + 1] == 'd' or self.layout[door.coords[0]][door.coords[1] - 1] == 'd':
                    door.isConnected = True
                    door.char = 'd'
                else:
                    door.char = 'w'

    def updateDoorArray(self):
        temp = []
        for room in self.rooms:
            for door in room.doors:
                temp.append(door)
        self.doors = temp

    def printmap(self):
        for row in self.layout:
            print(row)

    def printTopLefts(self):
        toplefts = []
        for room in self.rooms:
            print(room.topleft, room.value)
            if toplefts.__contains__(room.topleft):
                print("ERROR", room.value)
            toplefts.append(room.topleft)


if __name__ == '__main__':
    levelcreator = LevelCreator(3)
    levelcreator.printmap()
    levelcreator.printTopLefts()
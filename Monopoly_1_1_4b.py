# MONOPOLY Version 1.1.4b

"""
Version Updates:

----- 1.0 Initialization -----

1.0.1 Initialized countries and their corresponding colors

1.0.2 Pygame cell creation (country, color, price)

1.0.3 Framework organization (code visual)

1.0.4 Board Setup

1.0.5 Start Cell

1.0.6 More Cells

1.0.7 Better Visual

1.0.8 Size, Player Input and Jail Adjustment

1.0.9 Cell Picture Insertion

----- 1.1 Game-Play Setup -----

1.1.0 Reorganized Path

1.1.1 Player Name Input

1.1.2a Player Avatar
1.1.2b Player Name Display
1.1.2c Button Display
1.1.2d Player Turn Setup
1.1.2e Spinner Display
1.1.2f Playable Spinner Visualization

1.1.3a Avatar Moving
1.1.3b Avatar Moving Animation
1.1.3c Grid Shining Animation

1.1.4a Money Count Display
1.1.4b Money Input
"""

import pygame, sys, numpy, random, math, time, os

SCREEN_W, SCREEN_H = 1500, 900
fileFlag = False
if os.getcwd()[len(os.getcwd())-os.getcwd().index('\\')+2:]=='OldVersions':
    fileFlag = True

class CLS_player(object):
    '''                 /\
                     /      \
                  /  1     6   \
                 |             |
                 | 2          5|
                 |             |
                 \   3     4  /
                    \      /
                       \/
    '''
    def __init__(self, pIndex, startCell, nameColor, color, dieColor, name, lifeStat, money):
        self.pIndex = pIndex
        self.cell = startCell
        self.crtX, self.crtY = main.size - 1, main.size - 1
        self.X, self.Y = main.board.cells[self.cell].x, main.board.cells[self.cell].y
        self.origX, self.origY = self.X, self.Y
        self.nameColor = nameColor
        self.color=color
        self.dieColor = dieColor
        self.name = name
        self.lifeStat = lifeStat
        self.money = money
        self.moveDir, self.moveDist = 0, 0
        self.moving = False
        self.dirList = [[0, -1], [1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1]]
        self.cellOrg = main.board.cellOrganization
        self.moveI, self.moveJ = 0, 1
        self.recDist = 0
        self.moveDiv = 30
        self.moveList = []
        self.textW = 20
        self.font = pygame.font.Font(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\GlacialIndifference-Regular.otf'), self.textW)

    def move(self):
        if self.moveDist != 0:
            self.moveList = [[self.crtX, self.crtY, self.cell]]
            self.moveI, self.moveJ = 0, 1
            self.recDist = self.moveDist
            self.moving = True
            while self.moveDist != 0:
                self.moveX, self.moveY = self.dirList[self.moveDir][0], self.dirList[self.moveDir][1]
                try:
                    newX, newY = self.crtX + self.moveX, self.crtY + self.moveY
                    kCell = self.cellOrg[newY][newX]
                    if newY < 0 or newX < 0:
                        b = 1 / 0
                    a = 1 / (kCell + 1) # testing if the cell is -1
                except:
                    if self.moveDir == 0:
                        if self.crtX == 0:
                            self.moveDir = 1
                        elif self.crtX == main.size - 1:
                            self.moveDir = 3
                        elif self.crtX == 2 * main.size - 2:
                            self.moveDir = 5
                        elif self.crtX < main.size - 1:
                            self.moveDir = 2
                        else:
                            self.moveDir = 4
                    elif self.moveDir == 1:
                        if self.crtY == 0:
                            self.moveDir = 2
                        elif self.crtY == main.size - 1:
                            self.moveDir = 4
                        elif self.crtY == 2 * main.size - 2:
                            self.moveDir = 0
                        elif self.crtY < main.size - 1:
                            self.moveDir = 3
                        else:
                            self.moveDir = 5
                    elif self.moveDir == 2:
                        if self.crtY == main.size - 1:
                            self.moveDir = 3
                        elif self.crtY == 2 * main.size - 2 and self.crtX == 2 * main.size - 2:
                            self.moveDir = 5
                        elif self.crtX == main.size - 1:
                            self.moveDir = 1
                        elif self.crtY < 2 * main.size - 2:
                            self.moveDir = 4
                        else:
                            self.moveDir = 0
                    elif self.moveDir == 3:
                        if self.crtX == 0:
                            self.moveDir = 2
                        elif self.crtX == main.size - 1:
                            self.moveDir = 0
                        elif self.crtX == 2 * main.size - 2:
                            self.moveDir = 4
                        elif self.crtX < main.size - 1:
                            self.moveDir = 1
                        else:
                            self.moveDir = 5
                    elif self.moveDir == 4:
                        if self.crtY == 0:
                            self.moveDir = 3
                        elif self.crtY == main.size - 1:
                            self.moveDir = 1
                        elif self.crtY == 2 * main.size - 2:
                            self.moveDir = 5
                        elif self.crtY < main.size - 1:
                            self.moveDir = 2
                        else:
                            self.moveDir = 0
                    elif self.moveDir == 5:
                        if self.crtY == main.size - 1:
                            self.moveDir = 0
                        elif self.crtY == 0 and self.crtX == 0:
                            self.moveDir = 2
                        elif self.crtX == main.size - 1:
                            self.moveDir = 4
                        elif self.crtY > 0:
                            self.moveDir = 1
                        else:
                            self.moveDir = 3
                    continue
                self.crtX, self.crtY = newX, newY
                self.cell = self.cellOrg[self.crtY][self.crtX]
                self.moveList.append([main.board.cells[self.cell].x, main.board.cells[self.cell].y])
                self.moveDist -= 1
        if self.moving:
            self.X = self.origX + self.moveJ * (self.moveList[self.moveI + 1][0] - self.origX) // self.moveDiv
            self.Y = self.origY + self.moveJ * (self.moveList[self.moveI + 1][1] - self.origY) // self.moveDiv
            self.moveJ += 1
            if self.moveJ > self.moveDiv:
                self.moveI += 1
                self.moveJ = 1
                self.origX, self.origY = self.moveList[self.moveI][0], self.moveList[self.moveI][1]
            if self.moveI >= self.recDist:
                self.moving = False
            
    def draw(self, scr, position, turn):
        size = main.board.cSize
        margin=size//6
        pointList=[((self.X-margin//2,self.Y-margin//(3**0.5/2+0.5)),
                        (self.X - size * 3 ** 0.5 // 2 +margin//1.2,self.Y - size // 2),
                        (self.X-margin//2, self.Y - size+margin//(3**0.5/2+0.5))),
                   ((self.X-margin//1.1,self.Y),
                        (self.X-size * 3 ** 0.5 // 2 + margin//2, self.Y+size // 2-margin//(3**0.5/2+0.5)),
                        ((self.X-size * 3 ** 0.5 // 2+margin//2, self.Y-size // 2+margin//(3**0.5/2+0.5)))),
                   ((self.X-margin//2,self.Y + margin//(3**0.5/2+0.5)),
                        (self.X - size * 3 ** 0.5 // 2 +margin//1.2,self.Y + size // 2),
                        (self.X-margin//2, self.Y + size - margin//(3**0.5/2+0.5))),
                   ((self.X + margin//2,self.Y + margin//(3**0.5/2+0.5)),
                        (self.X + size * 3 ** 0.5 // 2 - margin//1.2,self.Y + size // 2),
                        (self.X + margin//2, self.Y + size - margin//(3**0.5/2+0.5))),
                   ((self.X + margin//1.1,self.Y),
                        (self.X + size * 3 ** 0.5 // 2 - margin//2, self.Y+size // 2-margin//(3**0.5/2+0.5)),
                        ((self.X + size * 3 ** 0.5 // 2 - margin//2, self.Y-size // 2+margin//(3**0.5/2+0.5)))),
                   ((self.X + margin//2,self.Y-margin//(3**0.5/2+0.5)),
                        (self.X + size * 3 ** 0.5 // 2 - margin//1.2,self.Y - size // 2),
                        (self.X + margin//2, self.Y - size+margin//(3**0.5/2+0.5)))
                   ]
        triSurface = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        pygame.draw.polygon(triSurface, self.color,pointList[position-1])
        scr.blit(triSurface, (0, 0))

        if self.lifeStat == 0:
            pygame.draw.rect(scr, self.dieColor, pygame.Rect(10, SCREEN_H - (6 - self.pIndex) * (self.textW + 10), 50, self.textW))
            scr.blit(self.font.render(self.name, True, (122, 112, 128)), (70, SCREEN_H - (6 - self.pIndex) * (self.textW + 10)))
            scr.blit(self.font.render('$' + str(self.money), True, (160, 96, 96)), (80 + self.font.size(self.name)[0], SCREEN_H - (6 - self.pIndex) * (self.textW + 10)))
        else:
            if turn == self.pIndex:
                pygame.draw.rect(scr, (255, 255, 255), pygame.Rect(10, SCREEN_H - (6 - self.pIndex) * (self.textW + 10), 50, self.textW))
                pygame.draw.rect(scr, self.nameColor, pygame.Rect(13, SCREEN_H - (6 - self.pIndex) * (self.textW + 10) + 3, 44, self.textW - 6))
            else:
                pygame.draw.rect(scr, self.nameColor, pygame.Rect(10, SCREEN_H - (6 - self.pIndex) * (self.textW + 10), 50, self.textW))
            scr.blit(self.font.render(self.name, True, (245, 225, 255)), (70, SCREEN_H - (6 - self.pIndex) * (self.textW + 10)))
            scr.blit(self.font.render('$' + str(self.money), True, (150, 215, 150)), (80 + self.font.size(self.name)[0], SCREEN_H - (6 - self.pIndex) * (self.textW + 10)))
            
# Class of Cells:
class CLS_Cell(object):
    def __init__(self, x, y, cIndex, cSize, cellType, name, price, cColor, bColor, stType, img, tColor):
        self.x, self.y = x, y
        self.cIndex = cIndex
        self.cSize = cSize
        self.cellType = cellType
        self.name, self.price, self.cColor, self.bColor = name, price, cColor, bColor
        self.font = pygame.font.Font(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\GlacialIndifference-Regular.otf'), self.cSize * 3 // 11)
        self.font2 = pygame.font.Font(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\GlacialIndifference-Regular.otf'), self.cSize // 3)
        self.tColor = tColor
        self.stType = stType
        self.img = img
        self.shining = False
        self.colorDiv = 20
        self.current_color = self.cColor
        self.orig_color = self.cColor
        self.aim_color = self.cColor
        self.transI = 1
        self.crtK = 0

    def draw(self, scr):
        if main.playerList[main.current_player].cell == self.cIndex:
            if not self.shining:
                self.crtK = main.current_player
                self.current_color = self.cColor
                self.aim_color = main.playerList[main.current_player].nameColor
                self.orig_color = self.cColor
                self.transI = 1
                self.shining = True
        if self.shining:
            if main.current_player != self.crtK:
                self.crtK = main.current_player
                self.current_color = self.cColor
                self.aim_color = main.playerList[main.current_player].nameColor
                self.orig_color = self.cColor
                self.transI = 1
            self.current_color = (self.orig_color[0] + self.transI * (self.aim_color[0] - self.orig_color[0]) // self.colorDiv, \
                                  self.orig_color[1] + self.transI * (self.aim_color[1] - self.orig_color[1]) // self.colorDiv, \
                                  self.orig_color[2] + self.transI * (self.aim_color[2] - self.orig_color[2]) // self.colorDiv)
            self.transI += 1
            if self.transI > self.colorDiv:
                self.transI = 1
                self.current_color, self.aim_color = self.aim_color, self.orig_color
                self.orig_color = self.current_color
        if main.playerList[main.current_player].cell != self.cIndex and self.shining:
            self.shining = False
            self.current_color = self.cColor
            self.aim_color = self.cColor
            
        if self.stType == 1:
            pygame.draw.polygon(scr, self.current_color, ((self.x, self.y + self.cSize), #Bottom
                                                   (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), #Lower Left
                                                   (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), #Upper Left
                                                   (self.x, self.y - self.cSize), #Top
                                                   (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), #Upper Right
                                                   (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2))) #Lower Right
            pygame.draw.polygon(scr, self.bColor, ((self.x, self.y + self.cSize - 4),
                                                   (self.x - self.cSize * 3 ** 0.5 // 2 + 4,
                                                    self.y + self.cSize // 2 - 2),
                                                   (self.x - self.cSize * 3 ** 0.5 // 2 + 4,
                                                    self.y - self.cSize // 2 + 2), (self.x, self.y - self.cSize + 4),
                                                   (self.x + self.cSize * 3 ** 0.5 // 2 - 4,
                                                    self.y - self.cSize // 2 + 2),
                                                   (self.x + self.cSize * 3 ** 0.5 // 2 - 4,
                                                    self.y + self.cSize // 2 - 2)))
            if self.img != -1:
                scr.blit(self.img,
                         (self.x - self.img.get_width() // 2, self.y - self.cSize // 3 - self.img.get_height() // 2))
            scr.blit(self.font.render(self.name, True, self.cColor),
                     (self.x - self.font.size(self.name)[0] // 2, self.y))
            if self.price != -1:
                scr.blit(self.font.render('$' + str(self.price), True, self.cColor),
                         (self.x - self.font.size('$' + str(self.price))[0] // 2, self.y + self.cSize // 3))
        elif self.stType == 2:
            pygame.draw.polygon(scr, self.current_color, ((self.x, self.y + self.cSize),
                                                   (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2),
                                                   (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2),
                                                   (self.x, self.y - self.cSize),
                                                   (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2),
                                                   (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, self.bColor, ((self.x, self.y + self.cSize - 2),
                                                   (self.x - self.cSize * 3 ** 0.5 // 2 + 2,
                                                    self.y + self.cSize // 2 - 1),
                                                   (self.x - self.cSize * 3 ** 0.5 // 2 + 2,
                                                    self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2),
                                                   (self.x + self.cSize * 3 ** 0.5 // 2 - 2,
                                                    self.y - self.cSize // 2 + 1),
                                                   (self.x + self.cSize * 3 ** 0.5 // 2 - 2,
                                                    self.y + self.cSize // 2 - 1)))
            if self.img != -1:
                scr.blit(self.img, (self.x - self.img.get_width() // 2, self.y - self.img.get_height() // 2))
            scr.blit(self.font2.render(self.name, True, self.tColor),
                     (self.x - self.font2.size(self.name)[0] // 2, self.y - self.font2.size(self.name)[1] // 2))


class CLS_Board(object):

    def __init__(self, size, countries, prices, colors):
        self.size = size
        self.countries = countries
        self.prices = prices
        self.colors = colors
        self.cellNum = self.size * (self.size - 1) * 3 + 1
        self.cSize = (SCREEN_H - 60) // (self.size * 3 - 1)
        self.indices = list(range(self.cellNum))
        self.distribution = [0] * self.cellNum
        self.cellOrganization = []
        cCell = 0
        for i in range(self.size):
            cellLine = []
            for j in range(self.size + i):
                cellLine.append(cCell)
                cCell += 1
            self.cellOrganization.append(cellLine)
        for i in range(self.size - 1):
            cellLine = []
            for j in range(i + 1):
                cellLine.append(-1)
            for j in range(self.size * 2 - i - 2):
                cellLine.append(cCell)
                cCell += 1
            self.cellOrganization.append(cellLine)

        self.elec_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\elec_company.png'))
        self.elec_pic = pygame.transform.scale(self.elec_pic, (self.cSize, self.cSize))
        self.elec_pic.set_colorkey((255, 255, 255))
        self.water_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\water_company.png'))
        self.water_pic = pygame.transform.scale(self.water_pic, (self.cSize, self.cSize))
        self.water_pic.set_colorkey((255, 255, 255))
        self.oil_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\oil_company.png'))
        self.oil_pic = pygame.transform.scale(self.oil_pic, (self.cSize, self.cSize * 3 // 4))
        self.oil_pic.set_colorkey((255, 255, 255))
        self.jail_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\jail_pic.png'))
        self.jail_pic = pygame.transform.scale(self.jail_pic, (self.cSize, self.cSize * 4 // 3))
        self.jail_pic.set_colorkey((255, 255, 255))
        self.auschwitz_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\auschwitz_pic.png'))
        self.auschwitz_pic = pygame.transform.scale(self.auschwitz_pic, (self.cSize, self.cSize * 5 // 4))
        self.auschwitz_pic.set_colorkey((255, 255, 255))
        self.casino_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\casino_pic.png'))
        self.casino_pic = pygame.transform.scale(self.casino_pic, (self.cSize * 7 // 5, self.cSize * 7 // 5))
        self.casino_pic.set_colorkey((255, 255, 255))
        self.treasure_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\treasure_pic.png'))
        self.treasure_pic = pygame.transform.scale(self.treasure_pic, (self.cSize, self.cSize * 4 // 3))
        self.treasure_pic.set_colorkey((255, 255, 255))
        self.surprise_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\surprise_pic.png'))
        self.surprise_pic = pygame.transform.scale(self.surprise_pic, (self.cSize, self.cSize * 4 // 3))
        self.surprise_pic.set_colorkey((255, 255, 255))
        self.punishment_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\punishment_pic.png'))
        self.punishment_pic = pygame.transform.scale(self.punishment_pic, (self.cSize, self.cSize * 4 // 3))
        self.punishment_pic.set_colorkey((255, 255, 255))

        self.flags = []
        for i in range(28):
            row = []
            for j in range(7):
                flag = pygame.image.load(os.path.relpath('..\\'*fileFlag+f'Data\\country_flags\\{i}{chr(j + 97)}.jpg'))
                flag = pygame.transform.scale(flag, (self.cSize * 4 // 5, self.cSize // 2))
                if countries[i][j] == 'Nepal':
                    flag.set_colorkey((255, 255, 255))
                row.append(flag)
            self.flags.append(row)

        self.infoDic = {'country': [1, -1, (40, 5, 77), -1, -1, -1, -1],
                        'start': [2, (67, 125, 85), (103, 150, 111), 'START', -1, -1, (255, 255, 255)],
                        'jail': [2, (30, 30, 30), (170, 170, 170), 'JAIL', -1, self.jail_pic, (30, 30, 30)],
                        'surprise': [2, (150, 100, 54), (210, 190, 170), 'Surprise!', -1, self.surprise_pic,
                                     (150, 100, 54)],
                        'punishment': [2, (0, 0, 0), (190, 190, 190), 'Punishment', -1, self.punishment_pic, (0, 0, 0)],
                        'treasure': [2, (110, 75, 40), (230, 209, 200), 'Treasure', -1, self.treasure_pic,
                                     (110, 75, 40)],
                        'water company': [1, (60, 55, 120), (185, 194, 220), 'Water Co.', 124, self.water_pic, -1],
                        'oil company': [1, (110, 75, 60), (225, 210, 188), 'Oil Co.', 114, self.oil_pic, -1],
                        'electric company': [1, (110, 100, 80), (230, 220, 200), 'Electric Co.', 144, self.elec_pic,
                                             -1],
                        'casino': [2, (110, 50, 50), (230, 180, 180), 'CASINO', -1, self.casino_pic, (110, 50, 50)],
                        'auschwitz': [2, (0, 0, 0), (150, 150, 150), 'Auschwitz', -1, self.auschwitz_pic, (0, 0, 0)]}

        # Start Cell
        self.distribution[self.cellNum // 2] = 'start'
        self.indices.remove(self.cellNum // 2)

        # Jail Cell
        jailNum = random.randint(1, self.cellNum // 50 + 1)
        for i in range(jailNum):
            newI = random.choice(self.indices)
            self.indices.remove(newI)
            if i == 0 and random.randint(1, 4) == 1:
                self.distribution[newI] = 'auschwitz'
            else:
                self.distribution[newI] = 'jail'

        # Country Cell
        iLen = len(self.indices)
        if self.size < 5:
            setCells = random.randint(2, 4)
        elif self.size < 7:
            setCells = random.randint(4, 6)
        else:
            setCells = random.randint(6, 7)
        setNum = min(random.randint(int((iLen * 3 / 4) // setCells), int((iLen * 7 / 8) // setCells)), 28)
        cSets = random.sample(list(range(28)), setNum)
        for i in range(setNum):
            cLeft = random.sample(list(range(7)), setCells)
            for j in range(setCells):
                k = random.choice(self.indices)
                self.distribution[k] = [cSets[i], cLeft[j]]
                self.indices.remove(k)

        # Surprise / Treasure / Punishment Cells
        for i in self.indices:
            self.distribution[i] = random.choice(
                ['surprise', 'treasure', 'punishment', 'electric company', 'water company', 'oil company', 'casino'])

        self.cells = []
        self.cInd, self.cLayer, self.maxInd = 0, 0, self.size
        self.rev = True
        for i in range(self.cellNum):
            if self.rev:
                self.cX = SCREEN_W // 2 - (self.cSize + 1) * (
                            self.size + self.cLayer - 1 - 2 * self.cInd) * 3 ** 0.5 // 2
                self.cY = SCREEN_H // 2 - 3 * (self.size - self.cLayer - 1) * (self.cSize + 1) // 2
            else:
                self.cX = SCREEN_W // 2 - (self.cSize + 1) * (
                            self.size + (2 * self.size - self.cLayer - 2) - 1 - 2 * self.cInd) * 3 ** 0.5 // 2
                self.cY = SCREEN_H // 2 + 3 * (self.cLayer - self.size + 1) * (self.cSize + 1) // 2
            info = self.distribution[i]
            if type(info) == type([114, 124]):
                newCell = CLS_Cell(self.cX, self.cY, i, self.cSize, 'country', self.countries[info[0]][info[1]],
                                   self.prices[info[0]][info[1]], self.colors[info[0]], self.infoDic['country'][2], 1,
                                   self.flags[info[0]][info[1]], -1)
            else:
                newCell = CLS_Cell(self.cX, self.cY, i, self.cSize, info, self.infoDic[info][3], self.infoDic[info][4],
                                   self.infoDic[info][1], self.infoDic[info][2], self.infoDic[info][0],
                                   self.infoDic[info][5], self.infoDic[info][6])

            self.cells.append(newCell)
            self.cInd += 1
            if self.rev and i >= self.cellNum // 2 + self.size - 1:
                self.rev = False
            if self.cInd >= self.maxInd:
                if self.rev:
                    self.maxInd += 1
                else:
                    self.maxInd -= 1
                self.cInd = 0
                self.cLayer += 1

    def draw(self, scr):
        for cell in self.cells:
            cell.draw(scr)


class CLS_Button(object):
    def __init__(self, img, pressed_img, posX, posY, showStat, w, h, doneStat):
        self.img = img
        self.pressed_img = pressed_img
        self.posX, self.posY = posX, posY
        self.showStat = showStat
        self.pressedStat = 0
        self.w, self.h = w, h
        self.doneStat = doneStat

    def draw(self, scr):
        mPosX, mPosY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        if mPosX <= self.posX + self.w and mPosX >= self.posX:
            if mPosY <= self.posY + self.h and mPosY >= self.posY:
                self.pressedStat = 1
            else:
                self.pressedStat = 0
        else:
            self.pressedStat = 0
        if self.doneStat == 1:
            scr.blit(self.pressed_img, (self.posX, self.posY))
        elif self.showStat == 1:
            if self.pressedStat == 1:
                crtPic = self.pressed_img
            else:
                crtPic = self.img
            
            scr.blit(crtPic, (self.posX, self.posY))


class CLS_Spinner(object):
    def __init__(self, posX, posY, size, borderColor, innerColor, lineColor, divisions, tList, spinnerId, handStat):
        self.posX, self.posY = posX, posY
        self.size = size
        self.borderColor, self.innerColor, self.lineColor = borderColor, innerColor, lineColor
        self.divisions = divisions
        self.tList = tList
        self.spinnerId = spinnerId
        self.font = pygame.font.Font(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\GlacialIndifference-Regular.otf'), self.size // 4)

        self.handStat = 0
        self.handAngle = 0
        self.speed = random.random() / 5 + 1 / 2
        self.deceleration = random.random() / 240 + 1 / 120
        self.dir, self.dist = 0, 0

    def draw(self, scr):
        pygame.draw.circle(scr, self.borderColor, (self.posX, self.posY), self.size)
        pygame.draw.circle(scr, self.innerColor, (self.posX, self.posY), self.size * 19 // 20)
        for i in range(self.divisions):
            pygame.draw.line(scr, self.lineColor, (self.posX, self.posY), \
                             (self.posX + self.size * 19 * math.sin(2 * math.pi * i / self.divisions) // 20, \
                              self.posY - self.size * 19 * math.cos(2 * math.pi * i / self.divisions) // 20))
        if self.spinnerId == 0:
            for i in range(self.divisions):
                pygame.draw.polygon(scr, self.lineColor, \
                                    ((self.posX + self.size * math.sin(2 * math.pi * (i + 0.5) / self.divisions) // 4, \
                                     self.posY - self.size * math.cos(2 * math.pi * (i + 0.5) / self.divisions) // 4), \
                                    (self.posX + 2 * self.size * math.sin(2 * math.pi * (i + 0.55) / self.divisions) // 3, \
                                     self.posY - 2 * self.size * math.cos(2 * math.pi * (i + 0.55) / self.divisions) // 3), \
                                    (self.posX + 2 * self.size * math.sin(2 * math.pi * (i + 0.45) / self.divisions) // 3, \
                                     self.posY - 2 * self.size * math.cos(2 * math.pi * (i + 0.45) / self.divisions) // 3)))
                pygame.draw.polygon(scr, self.lineColor, \
                                    ((self.posX + 4 * self.size * math.sin(2 * math.pi * (i + 0.5) / self.divisions) // 5, \
                                     self.posY - 4 * self.size * math.cos(2 * math.pi * (i + 0.5) / self.divisions) // 5), \
                                    (self.posX + 2 * self.size * math.sin(2 * math.pi * (i + 0.6) / self.divisions) // 3, \
                                     self.posY - 2 * self.size * math.cos(2 * math.pi * (i + 0.6) / self.divisions) // 3), \
                                    (self.posX + 2 * self.size * math.sin(2 * math.pi * (i + 0.4) / self.divisions) // 3, \
                                     self.posY - 2 * self.size * math.cos(2 * math.pi * (i + 0.4) / self.divisions) // 3)))                
        elif self.spinnerId == 1:
            for i in range(self.divisions):
                scr.blit(self.font.render(self.tList[i], True, self.lineColor), \
                         (self.posX + 2 * self.size * math.sin(2 * math.pi * (i + 0.5) / self.divisions) // 3 - self.font.size(self.tList[i])[0] // 2, \
                          self.posY - 2 * self.size * math.cos(2 * math.pi * (i + 0.5) / self.divisions) // 3 - self.font.size(self.tList[i])[1] // 2))
        if self.handStat == 1 and self.speed < 0:
            self.speed = random.random() / 5 + 1 / 2
            self.deceleration = random.random() / 240 + 1 / 120
            self.handStat = 0
            if self.spinnerId == 0:
                self.dir = round(((self.handAngle + math.pi / 2) % (2 * math.pi)) // (2 * math.pi / self.divisions))
            if self.spinnerId == 1:
                self.dist = eval(self.tList[round(((self.handAngle + math.pi / 2) % (2 * math.pi)) // (2 * math.pi / self.divisions))])
        if self.handStat == 1:
            self.handAngle += self.speed
            self.speed -= self.deceleration
        pygame.draw.polygon(scr, self.borderColor, \
                            ((self.posX - self.size * math.cos(-self.handAngle) // 8, self.posY + self.size * math.sin(-self.handAngle) // 8), \
                             (self.posX - self.size * math.sin(-self.handAngle) // 8, self.posY - self.size * math.cos(-self.handAngle) // 8), \
                             (self.posX + self.size * math.cos(-self.handAngle + math.pi / 16) // 8, self.posY - self.size * math.sin(-self.handAngle + math.pi / 16) // 8), \
                             (self.posX + self.size * math.cos(-self.handAngle + math.pi / 16) // 2, self.posY - self.size * math.sin(-self.handAngle + math.pi / 16) // 2), \
                             (self.posX + 2 * self.size * math.cos(-self.handAngle) // 3, self.posY - 2 * self.size * math.sin(-self.handAngle) // 3), \
                             (self.posX + self.size * math.cos(-self.handAngle - math.pi / 16) // 2, self.posY - self.size * math.sin(-self.handAngle - math.pi / 16) // 2), \
                             (self.posX + self.size * math.cos(-self.handAngle - math.pi / 16) // 8, self.posY - self.size * math.sin(-self.handAngle - math.pi / 16) // 8), \
                             (self.posX + self.size * math.sin(-self.handAngle) // 8, self.posY + self.size * math.cos(-self.handAngle) // 8)))
        pygame.draw.polygon(scr, self.lineColor, \
                            ((self.posX - self.size * math.cos(-self.handAngle) // 12, self.posY + self.size * math.sin(-self.handAngle) // 12), \
                             (self.posX - self.size * math.sin(-self.handAngle) // 12, self.posY - self.size * math.cos(-self.handAngle) // 12), \
                             (self.posX + self.size * math.cos(-self.handAngle + math.pi / 22) // 12, self.posY - self.size * math.sin(-self.handAngle + math.pi / 22) // 12), \
                             (self.posX + self.size * math.cos(-self.handAngle + math.pi / 22) // 2, self.posY - self.size * math.sin(-self.handAngle + math.pi / 22) // 2), \
                             (self.posX + 3 * self.size * math.cos(-self.handAngle) // 5, self.posY - 3 * self.size * math.sin(-self.handAngle) // 5), \
                             (self.posX + self.size * math.cos(-self.handAngle - math.pi / 22) // 2, self.posY - self.size * math.sin(-self.handAngle - math.pi / 22) // 2), \
                             (self.posX + self.size * math.cos(-self.handAngle - math.pi / 22) // 12, self.posY - self.size * math.sin(-self.handAngle - math.pi / 22) // 12), \
                             (self.posX + self.size * math.sin(-self.handAngle) // 12, self.posY + self.size * math.cos(-self.handAngle) // 12)))
        pygame.draw.polygon(scr, (250, 245, 255), \
                            ((self.posX - self.size * math.cos(-self.handAngle) // 12, self.posY + self.size * math.sin(-self.handAngle) // 12), \
                             (self.posX - self.size * math.sin(-self.handAngle) // 12, self.posY - self.size * math.cos(-self.handAngle) // 12), \
                             (self.posX + self.size * math.cos(-self.handAngle) // 12, self.posY - self.size * math.sin(-self.handAngle) // 12), \
                             (self.posX + self.size * math.sin(-self.handAngle) // 12, self.posY + self.size * math.cos(-self.handAngle) // 12)))
        pygame.draw.polygon(scr, (250, 215, 255), \
                            ((self.posX + self.size * math.cos(-self.handAngle) // 6, self.posY - self.size * math.sin(-self.handAngle) // 6), \
                             (self.posX + self.size * math.cos(-self.handAngle + math.pi / 30) // 2, self.posY - self.size * math.sin(-self.handAngle + math.pi / 30) // 2), \
                             (self.posX + 4 * self.size * math.cos(-self.handAngle) // 7, self.posY - 4 * self.size * math.sin(-self.handAngle) // 7), \
                             (self.posX + self.size * math.cos(-self.handAngle - math.pi / 30) // 2, self.posY - self.size * math.sin(-self.handAngle - math.pi / 30) // 2)))

class FW_Main(object):
    # Status:
    # 0: Entering board size
    # 1: Entering Starting Money
    # 2: Entering number of players
    # 3: Entering names of players
    # 4: Game starts

    def __init__(self):
        # Initialization of Players
        self.playerList = []
        self.plyTransparentColorList=[(255, 0, 0, 176), (255, 128, 0, 176), (255, 255, 0, 176), (0, 255, 0, 176), (0, 0, 255, 176), (200, 0, 255, 176)]
        self.plyColorList = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (200, 0, 255)]
        self.plyDieColorList = [(128, 0, 0), (128, 64, 0), (128, 128, 0), (0, 128, 0), (0, 0, 128), (100, 0, 128)]
        # Initialization of countries
        cFile = open(os.path.relpath('..\\'*fileFlag+"Data\\Resources\\countries.txt"), 'r')
        cList = cFile.readlines()
        cFile.close()
        self.countries = []
        for group in cList:
            self.countries.append(group.strip().split(', '))

        # Initialization of prices
        pFile = open(os.path.relpath('..\\'*fileFlag+"Data\\Resources\\prices.txt"), 'r')
        pList = pFile.readlines()
        pFile.close()
        self.prices = []
        for price in pList:
            self.prices.append(list(map(int, price.strip().split(', '))))

        # Initialization of colors
        rFile = open(os.path.relpath('..\\'*fileFlag+"Data\\Resources\\colors.txt"), 'r')
        rList = rFile.readlines()
        rFile.close()
        self.colors = []
        for color in rList:
            nC = color[:-1]
            a, b, c = list(map(int, nC.strip('()').split(', ')))
            self.colors.append((a, b, c))

        pygame.init()
        
        self.font = pygame.font.Font(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\GlacialIndifference-Regular.otf'), 50)
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()

        self.spin_button_w, self.spin_button_h = 75, 30
        self.end_turn_button_w, self.end_turn_button_h = 100, 30
        self.spinner_r = 70
        self.spinner_border_color, self.spinner_color, self.spinner_line_color = (81, 44, 102), (214, 189, 222), (124, 59, 144)
        self.spinner_hand_w, self.spinner_hand_h = 12, 114

        self.spin_button_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\spin_button_2.png'))
        self.spin_button_pic = pygame.transform.scale(self.spin_button_pic, (self.spin_button_w, self.spin_button_h))
        self.spin_button_pic.set_colorkey((255, 255, 255))
        self.spin_button_pressed_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\spin_button_1.png'))
        self.spin_button_pressed_pic = pygame.transform.scale(self.spin_button_pressed_pic, (self.spin_button_w, self.spin_button_h))
        self.spin_button_pressed_pic.set_colorkey((255, 255, 255))
        self.end_turn_button_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\end_turn_button_2.png'))
        self.end_turn_button_pic = pygame.transform.scale(self.end_turn_button_pic, (self.end_turn_button_w, self.end_turn_button_h))
        self.end_turn_button_pic.set_colorkey((255, 255, 255))
        self.end_turn_button_pressed_pic = pygame.image.load(os.path.relpath('..\\'*fileFlag+'Data\\Resources\\end_turn_button_1.png'))
        self.end_turn_button_pressed_pic = pygame.transform.scale(self.end_turn_button_pressed_pic, (self.end_turn_button_w, self.end_turn_button_h))
        self.end_turn_button_pressed_pic.set_colorkey((255, 255, 255))
        
        self.spin_button_1 = CLS_Button(self.spin_button_pic, self.spin_button_pressed_pic, \
                                        SCREEN_W - 3 * self.spinner_r - 20 - self.spin_button_w // 2, 30 + 2 * self.spinner_r, 1, \
                                        self.spin_button_w, self.spin_button_h, 0)
        self.spin_button_2 = CLS_Button(self.spin_button_pic, self.spin_button_pressed_pic, \
                                        SCREEN_W - self.spinner_r - 10 - self.spin_button_w // 2, 30 + 2 * self.spinner_r, 1, \
                                        self.spin_button_w, self.spin_button_h, 0)
        self.end_turn_button = CLS_Button(self.end_turn_button_pic, self.end_turn_button_pressed_pic, \
                                          SCREEN_W - 2 * self.spinner_r - 15 - self.end_turn_button_w // 2, 50 + self.spin_button_h + 2 * self.spinner_r, 1, \
                                          self.end_turn_button_w, self.end_turn_button_h, 1)
        self.spinner_1 = CLS_Spinner(SCREEN_W - 3 * self.spinner_r - 20, 20 + self.spinner_r, \
                                     self.spinner_r, self.spinner_border_color, self.spinner_color, self.spinner_line_color, \
                                     6, [], 0, 0)
        
        self.stat = 0
        self.nameLen = 20
        self.moneyLen = 5
        self.sizeChar, self.moneyChar, self.pChar, self.nameChar = '_', ['_'] * self.moneyLen, '_', list('_' * self.nameLen)
        self.pNum = 0
        self.origMoney = 5000
        self.neStat = 0
        self.names = []

        self.current_player = 0

    def play(self):
        self.screen.fill((22, 8, 36))
        if self.stat == 0:
            self.screen.blit(self.font.render('Enter Board Size (3 ~ 9)', True, (250, 230, 210)),
                             ((SCREEN_W - self.font.size('Enter Board Size (3 ~ 9)')[0]) // 2, 30))
            self.screen.blit(self.font.render(self.sizeChar, True, (220, 210, 250)),
                             ((SCREEN_W - self.font.size(self.sizeChar)[0]) // 2,
                              (SCREEN_H - self.font.size(self.sizeChar)[1]) // 2))
        if self.stat == 1:
            self.screen.blit(self.font.render('Enter Starting Money (2000 ~ 20000)', True, (250, 230, 210)),
                             ((SCREEN_W - self.font.size('Enter Starting Money (2000 ~ 20000)')[0]) // 2, 30))
            self.screen.blit(self.font.render(''.join(self.moneyChar), True, (220, 210, 250)),
                             ((SCREEN_W - self.font.size(''.join(self.moneyChar))[0]) // 2,
                              (SCREEN_H - self.font.size(''.join(self.moneyChar))[1]) // 2))
        if self.stat == 2:
            self.screen.blit(self.font.render('Enter Number of Players (2 ~ 6)', True, (250, 230, 210)),
                             ((SCREEN_W - self.font.size('Enter Number of Players (2 ~ 9)')[0]) // 2, 30))
            self.screen.blit(self.font.render(self.pChar, True, (220, 210, 250)),
                             ((SCREEN_W - self.font.size(self.pChar)[0]) // 2,
                              (SCREEN_H - self.font.size(self.pChar)[1]) // 2))
        if self.stat == 3:
            self.screen.blit(self.font.render(f'Enter Name of Player {self.neStat + 1}', True, (250, 230, 210)),
                             ((SCREEN_W - self.font.size(f'Enter Name of Player {self.neStat + 1}')[0]) // 2, 30))
            self.screen.blit(self.font.render(''.join(self.nameChar), True, (220, 210, 250)),
                             ((SCREEN_W - self.font.size(''.join(self.nameChar))[0]) // 2,
                              (SCREEN_H - self.font.size(''.join(self.nameChar))[1]) // 2))
        if self.stat == 4:
            self.board.draw(self.screen)
            for player in self.playerList:
                player.move()
                player.draw(self.screen, player.pIndex + 1, self.current_player)

        if self.stat == 4:
            self.spin_button_1.draw(self.screen)
            self.spin_button_2.draw(self.screen)
            self.end_turn_button.draw(self.screen)

        if self.stat == 4:
            self.spinner_1.draw(self.screen)
            self.spinner_2.draw(self.screen)

        if self.stat == 4 and self.end_turn_button.doneStat == 1:
            if self.spin_button_1.doneStat == 1 and self.spinner_1.handStat == 0:
                if self.spin_button_2.doneStat == 1 and self.spinner_2.handStat == 0:
                    self.playerList[self.current_player].moveDir, self.playerList[self.current_player].moveDist = self.spinner_1.dir, self.spinner_2.dist
                    self.end_turn_button.doneStat = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.stat == 0:
                        if self.sizeChar == '_':
                            continue
                        self.stat = 1
                        self.size = int(self.sizeChar)
                        self.board = CLS_Board(self.size, self.countries, self.prices, self.colors)
                        integerList = []
                        for i in range(self.size):
                            integerList.append(str(i + 1))
                        integerList = random.sample(integerList, self.size)
                        self.spinner_2 = CLS_Spinner(SCREEN_W - self.spinner_r - 10, 20 + self.spinner_r, \
                                                     self.spinner_r, self.spinner_border_color, self.spinner_color, self.spinner_line_color, \
                                                     self.size, integerList, 1, 0)
                    if self.stat == 1:
                        if self.moneyChar[-1] == '_' or int(''.join(self.moneyChar).strip('_')) > 20000 or int(''.join(self.moneyChar).strip('_')) < 2000:
                            continue
                        self.stat = 2
                        self.origMoney = int(''.join(self.moneyChar).strip('_'))
                    if self.stat == 2:
                        if self.pChar == '_' or int(self.pChar) > 6:
                            continue
                        self.stat = 3
                        self.pNum = int(self.pChar)
                        self.current_player = random.randint(0, self.pNum - 1)
                    if self.stat == 3:
                        if self.neStat != self.pNum - 1:
                            if self.nameChar[-1] == '_':
                                continue
                            if ''.join(self.nameChar).strip('_') in self.names:
                                continue
                            self.names.append(''.join(self.nameChar).strip('_'))
                        else:
                            if self.nameChar[-1] == '_':
                                continue
                            if ''.join(self.nameChar).strip('_') in self.names:
                                continue
                            self.stat = 4
                            self.names.append(''.join(self.nameChar).strip('_'))
                        self.playerList.append(CLS_player(self.neStat, self.board.cellNum//2, \
                                                          self.plyColorList[self.neStat], self.plyTransparentColorList[self.neStat], self.plyDieColorList[self.neStat], \
                                                          ' '.join(''.join(self.nameChar).strip('_').split('_')), 1, 5000))
                        self.nameChar = list('_' * self.nameLen)
                        self.neStat += 1
                if event.key <= pygame.K_9 and event.key >= pygame.K_3 and self.stat == 0:
                    if self.sizeChar == '_':
                        self.sizeChar = str(event.key - ord('1') + 1)
                if event.key == pygame.K_BACKSPACE and self.stat == 0:
                    self.sizeChar = '_'
                if event.key <= pygame.K_9 and event.key >= pygame.K_0 and self.stat == 1:
                    if event.key == pygame.K_0 and self.moneyChar[-1] == '_':
                        continue
                    if self.moneyChar[0] != '_':
                        continue
                    self.moneyChar = self.moneyChar[1:] + [str(event.key - ord('0'))]
                if event.key == pygame.K_BACKSPACE and self.stat == 1:
                    self.moneyChar = ['_'] + self.moneyChar[:-1]
                if event.key <= pygame.K_6 and event.key >= pygame.K_2 and self.stat == 2:
                    if self.pChar == '_':
                        self.pChar = str(event.key - ord('1') + 1)
                if event.key == pygame.K_BACKSPACE and self.stat == 2:
                    self.pChar = '_'
                if (event.key >= ord('0') and event.key <= ord('9') or event.key >= ord('a') and event.key <= ord('z')) and self.stat == 3:
                    if self.nameChar[0] != '_':
                        continue
                    self.nameChar = self.nameChar[1:] + [chr(event.key)]
                if event.key == pygame.K_BACKSPACE and self.stat == 3:
                    if self.nameChar == '_' * self.nameLen:
                        continue
                    self.nameChar = ['_'] + self.nameChar[:-1]
                if event.key == pygame.K_SPACE and self.stat == 3:
                    if self.nameChar[0] != '_':
                        continue
                    self.nameChar = self.nameChar[1:] + ['_']
            if event.type == pygame.MOUSEBUTTONDOWN and self.stat == 4:
                if self.spin_button_1.doneStat == 0 and self.spin_button_1.pressedStat == 1:
                    self.spin_button_1.doneStat = 1
                    self.spinner_1.handStat = 1
                if self.spin_button_2.doneStat == 0 and self.spin_button_2.pressedStat == 1:
                    self.spin_button_2.doneStat = 1
                    self.spinner_2.handStat = 1
                if self.end_turn_button.doneStat == 0 and self.end_turn_button.pressedStat == 1:
                    self.current_player = (self.current_player + 1) % self.pNum
                    self.end_turn_button.doneStat = 1
                    self.spin_button_1.doneStat = 0
                    self.spin_button_2.doneStat = 0

        pygame.display.update()
        self.clock.tick(60)


# --------------- MAIN ---------------
main = FW_Main()
while True:
    main.play()


# MONOPOLY Version 1.0.8

"""
Version Updates:

1.0.1 Initialized countries and their corresponding colors
1.0.2 Pygame cell creation (country, color, price)
1.0.3 Framework organization (code visual)
1.0.4 Board Setup
1.0.5 Start Cell
1.0.6 More Cells
1.0.7 Better Visual
1.0.8 Size, Player Input and Jail Adjustment

"""

import pygame, sys, numpy, random, math, time

SCREEN_W, SCREEN_H = 1500, 900

# Class of Cells:
class CLS_Cell(object):
    def __init__(self, x, y, cSize, cellType, name, price, cColor, bColor, stType, img, tColor):
        self.x, self.y = x, y
        self.cSize = cSize
        self.cellType = cellType
        self.name, self.price, self.cColor, self.bColor = name, price, cColor, bColor
        self.font = pygame.font.Font('GlacialIndifference-Regular.otf', self.cSize * 3 // 11)
        self.font2 = pygame.font.Font('GlacialIndifference-Regular.otf', self.cSize // 3)
        self.tColor = tColor
        self.stType = stType
        self.img = img

    def draw(self, scr):
        if self.stType == 1:
            pygame.draw.polygon(scr, self.cColor, ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, self.bColor, ((self.x, self.y + self.cSize - 4), (self.x - self.cSize * 3 ** 0.5 // 2 + 4, self.y + self.cSize // 2 - 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 4, self.y - self.cSize // 2 + 2), (self.x, self.y - self.cSize + 4), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 4, self.y - self.cSize // 2 + 2), (self.x + self.cSize * 3 ** 0.5 // 2 - 4, self.y + self.cSize // 2 - 2)))
            scr.blit(self.font.render(self.name, True, self.cColor), (self.x - self.font.size(self.name)[0] // 2, self.y))
            if self.price != -1:
                scr.blit(self.font.render('$' + str(self.price), True, self.cColor), (self.x - self.font.size('$' + str(self.price))[0] // 2, self.y + self.cSize // 3))
        elif self.stType == 2:
            pygame.draw.polygon(scr, self.cColor, ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, self.bColor, ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font2.render(self.name, True, self.tColor), (self.x - self.font2.size(self.name)[0] // 2, self.y - self.font2.size(self.name)[1] // 2))

class CLS_Board(object):

    def __init__(self, size, countries, prices, colors):
        self.size = size
        self.countries = countries
        self.prices = prices
        self.colors = colors
        self.cellNum = self.size * (self.size - 1) * 3 + 1
        self.indices = list(range(self.cellNum))
        self.distribution = [0] * self.cellNum
        self.infoDic = {'country': [1, -1, (40, 5, 77), -1, -1, -1, -1], 'start': [2, (67, 125, 85), (103, 150, 111), 'START', -1, -1, (255, 255, 255)], \
                        'jail': [2, (30, 30, 30), (170, 170, 170), 'JAIL', -1, -1, (30, 30, 30)], 'surprise': [2, (150, 100, 54), (210, 190, 170), 'Surprise!', -1, -1, (150, 100, 54)], \
                        'punishment': [2, (0, 0, 0), (190, 190, 190), 'Punishment', -1, -1, (0, 0, 0)], 'treasure': [2, (150, 140, 70), (230, 219, 200), 'Treasure', -1, -1, (150, 140, 70)], \
                        'water company': [1, (60, 55, 120), (185, 194, 220), 'Water Co.', 124, -1, -1], 'oil company': [1, (110, 75, 60), (225, 210, 188), 'Oil Co.', 114, -1, -1], \
                        'electric company': [1, (110, 100, 80), (230, 220, 200), 'Electric Co.', 144, -1, -1], 'casino': [2, (110, 50, 50), (230, 180, 180), 'CASINO', -1, -1, (110, 50, 50)], \
                        'auschwitz': [2, (0, 0, 0), (150, 150, 150), 'Auschwitz', -1, -1, (0, 0, 0)]}
        
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
        setNum = min(random.randint((iLen * 3 / 4) // setCells, (iLen * 7 / 8) // setCells), 28)
        cSets = random.sample(list(range(28)), setNum)
        for i in range(setNum):
            cLeft = random.sample(list(range(7)), setCells)
            for j in range(setCells):
                k = random.choice(self.indices)
                self.distribution[k] = [cSets[i], cLeft[j]]
                self.indices.remove(k)

        # Surprise / Treasure / Punishment Cells
        for i in self.indices:
            self.distribution[i] = random.choice(['surprise', 'treasure', 'punishment', 'electric company', 'water company', 'oil company', 'casino'])
            
        self.cells = []
        self.cSize = (SCREEN_H - 60) // (self.size * 3 - 1)
        self.cInd, self.cLayer, self.maxInd = 0, 0, self.size
        self.rev = True
        for i in range(self.cellNum):
            if self.rev:
                self.cX = SCREEN_W // 2 - (self.cSize + 1) * (self.size + self.cLayer - 1 - 2 * self.cInd) * 3 ** 0.5 // 2
                self.cY = SCREEN_H // 2 - 3 * (self.size - self.cLayer - 1) * (self.cSize + 1) // 2
            else:
                self.cX = SCREEN_W // 2 - (self.cSize + 1) * (self.size + (2 * self.size - self.cLayer - 2) - 1 - 2 * self.cInd) * 3 ** 0.5 // 2
                self.cY = SCREEN_H // 2 + 3 * (self.cLayer - self.size + 1) * (self.cSize + 1) // 2
            info = self.distribution[i]
            if type(info) == type([114, 124]):
                newCell = CLS_Cell(self.cX, self.cY, self.cSize, 'country', self.countries[info[0]][info[1]], self.prices[info[0]][info[1]], self.colors[info[0]], self.infoDic['country'][2], 1, -1, -1)
            else:
                newCell = CLS_Cell(self.cX, self.cY, self.cSize, info, self.infoDic[info][3], self.infoDic[info][4], self.infoDic[info][1], self.infoDic[info][2], self.infoDic[info][0], self.infoDic[info][5], self.infoDic[info][6])
                
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

class FW_Main(object):
    # Status:
    # 0: Entering board size
    # 1: Entering number of players
    # 2: Game Starts
    
    def __init__(self):
        # Initialization of countries
        cFile = open("countries.txt", 'r')
        cList = cFile.readlines()
        cFile.close()
        self.countries = []
        for group in cList:
            self.countries.append(group.strip().split(', '))

        # Initialization of prices
        pFile = open("prices.txt", 'r')
        pList = pFile.readlines()
        pFile.close()
        self.prices = []
        for price in pList:
            self.prices.append(list(map(int, price.strip().split(', '))))

        # Initialization of colors
        rFile = open("colors.txt", 'r')
        rList = rFile.readlines()
        rFile.close()
        self.colors = []
        for color in rList:
            nC = color[:-1]
            a, b, c = list(map(int, nC.strip('()').split(', ')))
            self.colors.append((a, b, c))

        pygame.init()
        self.font = pygame.font.Font('GlacialIndifference-Regular.otf', 50)
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.stat = 0
        self.sizeChar, self.pChar = '_', '_'
        self.pNum = 0

    def play(self):
        self.screen.fill((22, 8, 36))
        if self.stat == 0:
            self.screen.blit(self.font.render('Enter Board Size (3 ~ 9)', True, (250, 230, 210)), ((SCREEN_W - self.font.size('Enter Board Size (3 ~ 9)')[0]) // 2, 30))
            self.screen.blit(self.font.render(self.sizeChar, True, (220, 210, 250)), ((SCREEN_W - self.font.size(self.sizeChar)[0]) // 2, (SCREEN_H - self.font.size(self.sizeChar)[1]) // 2))
        if self.stat == 1:
            self.screen.blit(self.font.render('Enter Number of Players (2 ~ 9)', True, (250, 230, 210)), ((SCREEN_W - self.font.size('Enter Number of Players (2 ~ 9)')[0]) // 2, 30))
            self.screen.blit(self.font.render(self.pChar, True, (220, 210, 250)), ((SCREEN_W - self.font.size(self.pChar)[0]) // 2, (SCREEN_H - self.font.size(self.pChar)[1]) // 2))
        if self.stat == 2:
            self.board.draw(self.screen)

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
                    if self.stat == 1:
                        if self.pChar == '_':
                            continue
                        self.stat = 2
                        self.pNum = int(self.pChar)
                if event.key <= pygame.K_9 and event.key >= pygame.K_3 and self.stat == 0:
                    if self.sizeChar == '_':
                        self.sizeChar = str(event.key - ord('1') + 1)
                if event.key == pygame.K_BACKSPACE and self.stat == 0:
                    self.sizeChar = '_'
                if event.key <= pygame.K_9 and event.key >= pygame.K_3 and self.stat == 1:
                    if self.pChar == '_':
                        self.pChar = str(event.key - ord('1') + 1)
                if event.key == pygame.K_BACKSPACE and self.stat == 1:
                    self.pChar = '_'
        pygame.display.update()
        self.clock.tick(60)
        
# --------------- MAIN ---------------
main = FW_Main()
while True:
    main.play()


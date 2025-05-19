# MONOPOLY Version 1.0.6

"""
Version Updates:

1.0.1 Initialized countries and their corresponding colors
1.0.2 Pygame cell creation (country, color, price)
1.0.3 Framework organization (code visual)
1.0.4 Board Setup
1.0.5 Start Cell
1.0.6 More Cells

"""

import pygame, sys, numpy, random, math, time

SCREEN_W, SCREEN_H = 1500, 900

# Class of Cells:
class CLS_Cell(object):
    def __init__(self, x, y, cSize, cellType, name, price, cColor):
        self.x, self.y = x, y
        self.cSize = cSize
        self.cellType = cellType
        self.name, self.price, self.cColor = name, price, cColor
        self.font = pygame.font.Font('GlacialIndifference-Regular.otf', self.cSize * 3 // 11)
        self.font2 = pygame.font.Font('GlacialIndifference-Regular.otf', self.cSize // 3)

    def draw(self, scr):
        if self.cellType == 'country':
            pygame.draw.polygon(scr, self.cColor, ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (40, 5, 77), ((self.x, self.y + self.cSize - 4), (self.x - self.cSize * 3 ** 0.5 // 2 + 4, self.y + self.cSize // 2 - 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 4, self.y - self.cSize // 2 + 2), (self.x, self.y - self.cSize + 4), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 4, self.y - self.cSize // 2 + 2), (self.x + self.cSize * 3 ** 0.5 // 2 - 4, self.y + self.cSize // 2 - 2)))
            scr.blit(self.font.render(self.name, True, self.cColor), (self.x - self.font.size(self.name)[0] // 2, self.y))
            scr.blit(self.font.render('$' + str(self.price), True, self.cColor), (self.x - self.font.size('$' + str(self.price))[0] // 2, self.y + self.cSize // 3))
        elif self.cellType == 'start':
            pygame.draw.polygon(scr, (67, 125, 85), ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (103, 150, 111), ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font2.render('START', True, (255, 255, 255)), (self.x - self.font2.size('START')[0] // 2, self.y - self.font2.size('START')[1] // 2))
        elif self.cellType == 'jail':
            pygame.draw.polygon(scr, (30, 30, 30), ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (170, 170, 170), ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font2.render('Jail', True, (20, 20, 20)), (self.x - self.font2.size('Jail')[0] // 2, self.y - self.font2.size('Jail')[1] // 2))
        elif self.cellType == 'surprise':
            pygame.draw.polygon(scr, (150, 100, 54), ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (210, 190, 170), ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font.render('Surprise', True, (110, 70, 24)), (self.x - self.font.size('Surprise')[0] // 2, self.y + self.cSize // 3))
        elif self.cellType == 'punishment':
            pygame.draw.polygon(scr, (0, 0, 0), ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (190, 190, 190), ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font.render('Punishment', True, (0, 0, 0)), (self.x - self.font.size('Punishment')[0] // 2, self.y + self.cSize // 3))
        elif self.cellType == 'treasure':
            pygame.draw.polygon(scr, (130, 110, 70), ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (230, 219, 200), ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font.render('Treasure', True, (50, 50, 20)), (self.x - self.font.size('Treasure')[0] // 2, self.y + self.cSize // 3))
        else:
            tWords = self.cellType.split()
            pygame.draw.polygon(scr, (30, 50, 30), ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (230, 250, 230), ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font.render(tWords[0].title(), True, (30, 50, 30)), (self.x - self.font.size(tWords[0].title())[0] // 2, self.y))
            scr.blit(self.font.render(tWords[1].title(), True, (30, 50, 30)), (self.x - self.font.size(tWords[1].title())[0] // 2, self.y + self.cSize // 3))

class CLS_Board(object):
    def __init__(self, size, countries, prices, colors):
        self.size = size
        self.countries = countries
        self.prices = prices
        self.colors = colors
        self.cellNum = self.size * (self.size - 1) * 3 + 1
        self.indices = list(range(self.cellNum))
        self.distribution = [0] * self.cellNum
        
        # Start Cell
        self.distribution[self.cellNum // 2] = 'start'
        self.indices.remove(self.cellNum // 2)
        
        # Jail Cell
        jailNum = random.randint(1, self.cellNum // 50 + 1)
        for i in range(jailNum):
            newI = random.choice(self.indices)
            self.indices.remove(newI)
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
            self.distribution[i] = random.choice(['surprise', 'treasure', 'punishment', 'electric company', 'water company', 'oil company'])
            
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
                newCell = CLS_Cell(self.cX, self.cY, self.cSize, 'country', self.countries[info[0]][info[1]], self.prices[info[0]][info[1]], self.colors[info[0]])
            else:
                newCell = CLS_Cell(self.cX, self.cY, self.cSize, info, -1, -1, -1)
                
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
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.size = 10
        self.board = CLS_Board(self.size, self.countries, self.prices, self.colors)

    def play(self):
        self.screen.fill((22, 8, 36))
        self.board.draw(self.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        self.clock.tick(60)
        
# --------------- MAIN ---------------
main = FW_Main()
while True:
    main.play()


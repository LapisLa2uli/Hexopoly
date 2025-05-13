# MONOPOLY Version 1.0.4

"""
Version Updates:

1.0.1 Initialized countries and their corresponding colors
1.0.2 Pygame cell creation (country, color, price)
1.0.3 Framework organization (code visual)
1.0.4 Board Setup

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

    def draw(self, scr):
        if self.cellType == 'country':
            pygame.draw.polygon(scr, self.cColor, ((self.x, self.y + self.cSize), (self.x - self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x, self.y - self.cSize), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2, self.y - self.cSize // 2), (self.x + self.cSize * 3 ** 0.5 // 2, self.y + self.cSize // 2)))
            pygame.draw.polygon(scr, (40, 5, 77), ((self.x, self.y + self.cSize - 2), (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y + self.cSize // 2 - 1), \
                                              (self.x - self.cSize * 3 ** 0.5 // 2 + 2, self.y - self.cSize // 2 + 1), (self.x, self.y - self.cSize + 2), \
                                              (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y - self.cSize // 2 + 1), (self.x + self.cSize * 3 ** 0.5 // 2 - 2, self.y + self.cSize // 2 - 1)))
            scr.blit(self.font.render(self.name, True, self.cColor), (self.x - self.font.size(self.name)[0] // 2, self.y))
            scr.blit(self.font.render('$' + str(self.price), True, self.cColor), (self.x - self.font.size('$' + str(self.price))[0] // 2, self.y + self.cSize // 3))

class CLS_Board(object):
    def __init__(self, size, countries, prices, colors):
        self.size = size
        self.countries = countries
        self.prices = prices
        self.colors = colors
        self.cellNum = self.size * (self.size - 1) * 3 + 1
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
            cI = [random.randint(0, 27), random.randint(0, 6)]
            newCell = CLS_Cell(self.cX, self.cY, self.cSize, 'country', self.countries[cI[0]][cI[1]], self.prices[cI[0]][cI[1]], self.colors[cI[0]])
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
        self.size = 6
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


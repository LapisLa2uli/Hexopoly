# MONOPOLY Version 1.0.3

"""
Version Updates:

1.0.1 Initialized countries and their corresponding colors
1.0.2 Pygame cell creation (country, color, price)
1.0.3 Framework organization (code visual)

"""

import pygame, sys, numpy, random, math, time

SCREEN_W, SCREEN_H = 1500, 900

# Class of Cells:
class CLS_cell(object):
    def __init__(self, x, y, size, cellType, name, price, cColor):
        self.x, self.y = x, y
        self.size = size
        self.cellType = cellType
        self.name, self.price, self.cColor = name, price, cColor
        self.font = pygame.font.Font('GlacialIndifference-Regular.otf', size * 2 // 7)
        # self.font = pygame.font.Font(None, size // 3)

    def draw(self, scr):
        if self.cellType == 'country':
            pygame.draw.polygon(scr, self.cColor, ((self.x + self.size, self.y), (self.x + self.size // 2, self.y - self.size * 3 ** 0.5 // 2), \
                                              (self.x - self.size // 2, self.y - self.size * 3 ** 0.5 // 2), (self.x - self.size, self.y), \
                                              (self.x - self.size // 2, self.y + self.size * 3 ** 0.5 // 2), (self.x + self.size // 2, self.y + self.size * 3 ** 0.5 // 2)))
            pygame.draw.polygon(scr, (40, 5, 77), ((self.x + self.size - 2, self.y), (self.x + self.size // 2 - 1, self.y - self.size * 3 ** 0.5 // 2 + 2), \
                                              (self.x - self.size // 2 + 1, self.y - self.size * 3 ** 0.5 // 2 + 2), (self.x - self.size + 2, self.y), \
                                              (self.x - self.size // 2 + 1, self.y + self.size * 3 ** 0.5 // 2 - 2), (self.x + self.size // 2 - 1, self.y + self.size * 3 ** 0.5 // 2 - 2)))
            scr.blit(self.font.render(self.name, True, self.cColor), (self.x - self.font.size(self.name)[0] // 2, self.y))
            scr.blit(self.font.render('$' + str(self.price), True, self.cColor), (self.x - self.font.size('$' + str(self.price))[0] // 2, self.y + self.size // 3))

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

        self.cI = [random.randint(0, 27), random.randint(0, 6)]
        self.nCell = CLS_cell(500, 400, 50, 'country', self.countries[self.cI[0]][self.cI[1]], self.prices[self.cI[0]][self.cI[1]], self.colors[self.cI[0]])

    def play(self):
        self.screen.fill((22, 8, 36))
        self.nCell.draw(self.screen)

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


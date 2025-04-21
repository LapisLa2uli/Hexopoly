# MONOPOLY Version 1.0.1

"""
Version Updates:

1.0.1 Initialized countries and their corresponding colors

"""

import pygame, sys, numpy, random, math, time

# Initialization of countries
cFile = open("countries.txt", 'r')
cList = cFile.readlines()
cFile.close()
countries = []
for group in cList:
    countries.append(group.strip().split(', '))

# Initialization of colors
rFile = open("colors.txt", 'r')
rList = rFile.readlines()
rFile.close()
colors = []
for color in rList:
    nC = color[:-1]
    a, b, c = list(map(int, nC.strip('()').split(', ')))
    colors.append((a, b, c))

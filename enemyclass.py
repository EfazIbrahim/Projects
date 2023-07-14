import random
import pygame

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 736)
        self.y = 50
        self.xchange = random.choice([10, -10])
        self.ychange = 0
        self.state = 'alive'
        self.rect = pygame.Rect((self.x, self.y), (64, 64))


    def setxchange(self, newx):
        self.xchange = newx

    def setychange(self, newy):
        self.ychange = newy

    def setx(self, newx):
        self.x = newx

    def sety(self, newy):
        self.y = newy

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def updatex(self):
        self.x += self.xchange

    def updatey(self):
        self.y += self.ychange

    def updaterect(self):
        self.rect = enemyrect = pygame.Rect((self.x, self.y), (64, 64))

    def getrect(self):
        return self.rect

import random
import time
import pygame
from pygame.locals import *
from sys import *
from mysprite import *
from words import *
from toutouzi import *
from player import *


class Screen():
    def __init__(self,size,caption):
        self.size = size
        self.caption = caption
        self.showlist = []
        self.screen = None
        pygame.init()

    def create(self):
        self.screen = pygame.display.set_mode(self.size, 0, 32)
        pygame.display.set_caption(self.caption)

    def close_on(self):
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

    def addpic(self,pic,pos):
        self.showlist.append([pic,pos])


    def showit(self):
        for i in self.showlist:

            self.screen.blit(i[0],i[1])

    def update(self):
        pygame.display.update()


mouse_filename = 'image/mouse.png'

screen = Screen((900, 500),'001')
screen.create()
mouse_icon = pygame.image.load(mouse_filename).convert_alpha()
while 1:
    screen.close_on()
    screen.addpic(mouse_icon, (100, 100))
    screen.showit()
    screen.update()


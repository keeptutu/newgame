import pygame
from pygame.locals import *
from sys import exit

dice_file_name = 'image/两排128.png'


class Mysprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    def _getx(self):
        return self.rect.x

    def _setx(self,value):
        self.rect.x = value

    x = property(_getx, _setx)

    def _gety(self):
        return self.rect.x

    def _sety(self,value):
        self.rect.x = value

    y = property(_getx,_setx)

    def _getpos(self):
        return self.rect.topleft

    def _setpos(self,pos):
        self.rect.topleft = pos

    position = property(_getpos, _setpos)

    def load(self,filename,width,height,columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(self.pos, (width, height))
        self.columns = columns

        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) -1

    def update(self,current_time,rate=200):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x,frame_y,self.frame_width,self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame


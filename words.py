import pygame


def make_words(pygame,text,size,color=(0,0,0)):
    myfont = pygame.font.Font('rex2.ttf',size)
    words = myfont.render(text,True,color)
    return words



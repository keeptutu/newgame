


def make_words(pygame,text,size,color=(0,0,0)):
    myfont = pygame.font.Font('rex2.ttf',size)
    words = myfont.render(text,True,color)
    return words


def make_right_word(pygame, s, size):
    test = make_words(pygame, s, size)
    test = pygame.transform.rotate(test, 90)
    return test


def make_left_word(pygame, s, size):
    test = make_words(pygame, s, size)
    test = pygame.transform.rotate(test, 270)
    return test

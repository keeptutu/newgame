import random
import time
st = 0
tou = 0
n = 0
dice = 0


def toutouzi():
    global tou,st,n,dice
    dice = random.randint(1,6)
    tou = 1
    if n == 0:
        st = time.clock()
        n = 1


if tou == 1 and time.clock() - st <= 2:
    eval('group.draw(screen)')
    n = 0

if tou == 1 and 2 < time.clock() - st <= 4:
    eval('screen.blit(tou)' + str(dice) + ',(720,225))')
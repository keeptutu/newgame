from words import *
import pygame
pygame.init()
# 定义土地类
class Block:
    def __init__(self,name, num, price, passmoney, buildmoney, belong=0, buildlevel=0):
        self.name = name
        self.num = num
        self.price = price
        self.passmoney = passmoney + buildlevel*1000
        self.belong = belong
        self.buildlevel = buildlevel
        self.buildmoney = buildmoney
        self.test = make_words(pygame, self.name, 28)

    def show(self):
        print('--------------------------')
        print('name:', self.name)
        print('编号:', self.num)
        print('价格:', self.price)
        print('过路费:', self.passmoney)
        print('归属:', self.belong)
        print('建房价格:', self.buildmoney)
        print('房屋等级:', self.buildlevel)
        print('--------------------------')






block0 = Block('000', 0, 5000, 500, 1000)
block1 = Block('001', 0, 6000, 500, 1000)
block2 = Block('002', 0, 6500, 500, 1000)
block3 = Block('003', 0, 7500, 500, 1000)
block4 = Block('004', 0, 8000, 500, 1500)
block5 = Block('005', 0, 8500, 500, 1500)
block6 = Block('006', 0, 9000, 500, 1800)
block7 = Block('007', 0, 10000, 500, 1800)
block8 = Block('008', 0, 12000, 500, 2000)
block9 = Block('009', 0, 13000, 500, 2100)
block10 = Block('010', 0, 15000, 500, 2200)
block11 = Block('011', 0, 16000, 500, 2300)
block12 = Block('012', 0, 16500, 500, 2300)
block13 = Block('013', 0, 18000, 500, 2300)
block14 = Block('014', 0, 19000, 500, 2400)
block15 = Block('015', 0, 19500, 500, 2500)
block16 = Block('016', 0, 20000, 500, 2600)
block17 = Block('017', 0, 21000, 500, 2700)
block18 = Block('018', 0, 23000, 500, 2800)
block19 = Block('019', 0, 24000, 500, 3000)
block20 = Block('020', 0, 26000, 500, 3200)
block21 = Block('021', 0, 26500, 500, 3400)
block22 = Block('022', 0, 28000, 500, 3600)
block23 = Block('023', 0, 30000, 500, 3800)
block24 = Block('024', 0, 32000, 500, 3900)
block25 = Block('025', 0, 35000, 500, 4000)
block26 = Block('026', 0, 38000, 500, 4300)
block27 = Block('027', 0, 40000, 500, 4500)
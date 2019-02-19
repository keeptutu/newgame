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


block0 = Block('000', 0, 5000, 1500, 1000)
block1 = Block('001', 1, 6000, 1500, 1000)
block2 = Block('002', 2, 6500, 1500, 1000)
block3 = Block('003', 3, 7500, 1500, 1000)
block4 = Block('004', 4, 8000, 1500, 1500)
block5 = Block('005', 5, 8500, 1500, 1500)
block6 = Block('006', 6, 9000, 1500, 1800)
block7 = Block('007', 7, 10000, 1500, 1800)
block8 = Block('008', 8, 12000, 1500, 2000)
block9 = Block('009', 9, 13000, 1500, 2100)
block10 = Block('010', 10, 15000, 1500, 2200)
block11 = Block('011', 11, 16000, 1500, 2300)
block12 = Block('012', 12, 16500, 1500, 2300)
block13 = Block('013', 13, 18000, 1500, 2300)
block14 = Block('014', 14, 19000, 1500, 2400)
block15 = Block('015', 15, 19500, 1500, 2500)
block16 = Block('016', 16, 20000, 1500, 2600)
block17 = Block('017', 17, 21000, 1500, 2700)
block18 = Block('018', 18, 23000, 1500, 2800)
block19 = Block('019', 19, 24000, 1500, 3000)
block20 = Block('020', 20, 26000, 1500, 3200)
block21 = Block('021', 21, 26500, 1500, 3400)
block22 = Block('022', 22, 28000, 1500, 3600)
block23 = Block('023', 23, 30000, 1500, 3800)
block24 = Block('024', 24, 32000, 1500, 3900)
block25 = Block('025', 25, 35000, 1500, 4000)
block26 = Block('026', 26, 38000, 1500, 4300)
block27 = Block('027', 27, 40000, 1500, 4500)

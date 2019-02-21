from words import *
import pygame
pygame.init()
l0_filename = 'image/l00.png'
l1_filename = 'image/l01.png'
l2_filename = 'image/l02.png'
l3_filename = 'image/l03.png'
pygame.display.set_mode((500,373))
l0 = pygame.image.load(l0_filename).convert_alpha()
l1 = pygame.image.load(l1_filename).convert_alpha()
l2 = pygame.image.load(l2_filename).convert_alpha()
l3 = pygame.image.load(l3_filename).convert_alpha()
# 定义土地类
class Block:
    def __init__(self,name, num, price, passmoney, buildmoney, belong=0, buildlevel=0):
        self.name = name
        self.num = num
        self.price = price
        self.passmoney = passmoney
        self.belong = belong
        self.buildlevel = buildlevel
        self.buildmoney = buildmoney
        self.test = make_words(pygame, self.name, 28)
        self.info_flag = 0
        self.show_passmoney = make_words(pygame, str(self.passmoney), 16)

    def uppassmoney(self):
        self.passmoney = self.passmoney + self.buildlevel*(self.buildmoney//2)
        self.show_passmoney = make_words(pygame, str(self.passmoney), 16)

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

    def make_info(self):
        self.info_name = make_words(pygame, self.name,27)
        self.info_belong = make_words(pygame, '归属: ' + str(self.belong) ,27)
        self.info_price = make_words(pygame, '土地售价: ' + str(self.price), 27)
        self.info_passmoney = make_words(pygame, '过路费: ' + str(self.passmoney), 27)
        self.info_buildmoney = make_words(pygame, '建造费: ' + str(self.buildmoney), 27)
        self.info_buildlevel = make_words(pygame, '建筑等级: ' + str(self.buildlevel), 27)

        if self.buildlevel == 0:
            pass
    def infoshow(self,screen):
        if self.info_flag == 1:
            screen.screen.blit(self.info_name, (14, 300))
            screen.screen.blit(self.info_belong, (14, 326))
            screen.screen.blit(self.info_price, (14, 352))
            screen.screen.blit(self.info_passmoney, (14, 378))
            screen.screen.blit(self.info_buildmoney, (14, 404))
            screen.screen.blit(self.info_buildlevel, (14, 430))
            if self.buildlevel == 0:
                screen.screen.blit(l0, (1400,460))
            elif self.buildlevel == 1:
                screen.screen.blit(l1, (1400, 390))
            elif self.buildlevel == 2:
                screen.screen.blit(l2, (1400, 390))
            elif self.buildlevel == 3:
                screen.screen.blit(l3, (1400, 340))

block0 = Block('start', 0, 5000, 1500, 1000)
block1 = Block('埃索达', 1, 6000, 1500, 1000)
block2 = Block('暴风城', 2, 6500, 1500, 1000)
block3 = Block('铁炉堡', 3, 7500, 1500, 1000)
block4 = Block('雷霆崖', 4, 8000, 1500, 1500)
block5 = Block('斯坦索姆', 5, 8500, 1500, 1500)
block6 = Block('锦绣谷', 6, 9000, 1500, 1800)
block7 = Block('达拉然', 7, 10000, 1500, 1800)
block8 = Block('抽卡1', 8, 12000, 1500, 2000)
block9 = Block('湖畔镇', 9, 13000, 1500, 2100)
block10 = Block('闪金镇', 10, 15000, 1500, 2200)
block11 = Block('幽暗城', 11, 16000, 1500, 2300)
block12 = Block('银月城', 12, 16500, 1500, 2300)
block13 = Block('风暴峭壁', 13, 18000, 1500, 2300)
block14 = Block('监狱', 14, 19000, 1500, 2400)
block15 = Block('祖阿曼', 15, 19500, 1500, 2500)
block16 = Block('加基森', 16, 20000, 1500, 2600)
block17 = Block('达纳苏斯', 17, 21000, 1500, 2700)
block18 = Block('西部荒野', 18, 23000, 1500, 2800)
block19 = Block('夜色镇', 19, 24000, 1500, 3000)
block20 = Block('辛特兰', 20, 26000, 1500, 3200)
block21 = Block('赤脊山', 21, 26500, 1500, 3400)
block22 = Block('抽卡2', 22, 28000, 1500, 3600)
block23 = Block('灰谷', 23, 30000, 1500, 3800)
block24 = Block('千针石林', 24, 32000, 1500, 3900)
block25 = Block('永歌森林', 25, 35000, 1500, 4000)
block26 = Block('丹莫罗', 26, 38000, 1500, 4300)
block27 = Block('奥格瑞玛', 27, 40000, 1500, 4500)

#! /usr/bin/env python
import pygame
import random

class Player:
    '''定义人物初始属性'''
    def __init__(self,name,cash=50000,land=0,deposit=50000,human=True):
        self.human = human                              # 判断是玩家还是机器
        props_card = []                                 # 卡片存储
        self.deposit = deposit                          # 存款
        self.cash = cash                                # 现金
        self.money = self.deposit + self.cash           # 总资产
        self.name = name                                # 玩家姓名
        self.land = land                                # 玩家土地数量
        self.props_card = props_card                    # 道具卡
        self.lottery1()                                  # 调用两次抽卡函数，人物出身会随机分配两张卡
        self.lottery1()

    def show(self):
        '''显示人物基础信息'''
        print('玩家姓名：', self.name)
        print('总资产：', self.money)
        print('玩家土地：', self.land,'块')
        print('现金：', self.cash)
        print('存款：', self.deposit)
        print('道具卡%d张'%len(self.props_card))
        for card in self.props_card:
            print(card.__name__)

    def lottery(self):
        '''抽卡，调用后会在人物道具卡列表随机增加一张道具卡'''
        n = random.randint(1, 100)
        if n == 1:  # 百分之一的几率抽中运气卡 直接胜利
            self.props_card.append(fate_card)
        elif 2 <= n <= 27:
            self.props_card.append(Luck_Card)
        elif 28 <= n <= 63:
            self.props_card.append(HouseBuild_card)
        elif 64 <= n <= 84:
            self.props_card.append(StagnantCard)
        else:
            self.props_card.append(OpenHouse_card)


    def lottery1(self):
        '''抽卡，调用后会在人物道具卡列表随机增加一张道具卡'''
        n = random.randint(1, 100)
        if 1 <= n <= 27:
            self.props_card.append(Luck_Card)
        elif 28 <= n <= 63:
            self.props_card.append(HouseBuild_card)
        elif 64 <= n <= 84:
            self.props_card.append(StagnantCard)
        else:
            self.props_card.append(OpenHouse_card)


class Building:
    '''定义土地初始文档'''
    def __init__(self,price=2000,passmoney=0,belong='',level=0,upgrade=0):
        self.belong = belong                    # 土地归属 0(无人) 1(玩家1) 2(玩家2)
        self.price = price                      # 初始土地价格
        self.level = level                      # 建筑等级
        self.passmoney = passmoney              # 过路费
        self.upgrade = upgrade                  # 土地升级费


def buy(player,map):
    '''定义土地购买事件，玩家归属'''
    player.cash -= map.price
    player.land += 1
    player.money = player.cash + player.deposit
    map.belong = player.name
    if map.level < 3:
        map.level += 1
    else:
        map.level == 3

def house_level(map):
    '''根据土地等级，划分过路费'''
    if map.level == 0:              # 0级
        map.price = 0
    elif map.level == 1:            # 1级
        map.price = 3000
    elif map.level == 2:            # 2级
        map.price = 7500
    else:                           # 3级
        map.price = 12000

def house_upgrade(map):
    '''土地升级费,土地等级变更,过路费变更'''
    if map.level == 0:          # 当土地等级为0时
        map.upgrade = 2500
        map.passmoney = 3000
    elif map.level == 1:
        map.upgrade = 5000
        map.passmoney = 7500
    elif map.level == 2:
        map.upgrade = 7500
        map.passmoney = 12000


def Pass_money(player,map,other):
    '''支付过路费'''
    house_upgrade(map)
    player.cash -= map.passmoney
    player.money = player.deposit + player.cash
    other.cash += map.passmoney
    other.money = other.deposit + other.cash

'''定义五张道具卡[胜利卡，建房卡，运气卡，停留卡，拆房卡]'''
def fate_card(player):
    '''胜利卡，1%几率抽中，使用直接胜利'''
    pass


def Luck_Card(player):
    """运气卡，百分之五十几率+现金20000，百分之五十-现金10000"""
    n = random.randint(1,10)
    if n <= 5:
        player.cash += 20000
        player.money += 20000
        print("恭喜你，中奖啦！现金+20000")
    else:
        player.cash -= 10000
        player.money -= 10000
        print("恭喜你，中奖啦！现金-10000")
    player.props_card.remove(Luck_Card)

def HouseBuild_card(map,player):
    '''建房卡，在无人的空地上使用'''
    map.price = 0
    buy(player,map)
    player.props_card.remove(HouseBuild_card)

def StagnantCard(player):
    '''原地停滞一回合卡'''
    pass

def OpenHouse_card(player,map):
    map.belong = player.name
    player.props_card.remove(OpenHouse_card)

def bank(player,money):
    '''银行，玩家能存取钱'''
    picking = input('1、存钱\n2、取钱\n')
    if picking == '1':
        player.cash -= money
        player.deposit += money
        player.money = player.cash + player.deposit
    else:
        player.cash += money
        player.deposit -= money
        player.money = player.cash + player.deposit





player1 = Player('张三')
player2 = Player('李四')
map = Building()
player1.show()
print('--------------------')
bank(player1,5000)
player1.show()
# player1.show()
# print('--------------------')
# player2.show()
# Pass_money(player1,map,player2)
# print('--------------------')
# player1.show()
# print('--------------------')
# player2.show()













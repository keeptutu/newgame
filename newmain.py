import random
import time
import pygame
from pygame.locals import *
from sys import *
from mysprite import *
from words import *
from toutouzi import *
from player import *
from blockdata import *



# 文件名导入
title_icon_filename = 'image/titles.ico'
big_bg_filename = 'image/背景.png'
mouse_filename = 'image/mouse.png'
player_show_filename = 'image/人物头像框.png'
player_info_left_filename = 'image/数据框向右.png'
player_info_right_filename = 'image/数据框向左.png'
big_block_filename = 'image/四角块.png'
top_light_blue_filename = 'image/上边浅蓝色.png'
top_pink_filename = 'image/上边粉.png'
top_dark_blue_filename = 'image/上边蓝.png'
right_light_purple_filename = 'image/右边粉紫.png'
right_pink_filename = 'image/右边粉.png'
right_dark_purple_filename = 'image/右边紫.png'
bottom_dark_purple_filename = 'image/下边紫.png'
bottom_pink_filename = 'image/下边粉.png'
bottom_orange_filename = 'image/下边棕.png'
left_green_filename = 'image/左边绿.png'
left_pink_filename = 'image/左边粉色.png'
left_light_blue_filename = 'image/左边浅蓝色块.png'
# 骰子文件
tou1_filename = 'image/tou1.png'
tou2_filename = 'image/tou2.png'
tou3_filename = 'image/tou3.png'
tou4_filename = 'image/tou4.png'
tou5_filename = 'image/tou5.png'
tou6_filename = 'image/tou6.png'
# 按钮
button_out_filename = 'image/按钮红.png'
button_in_filename = 'image/按钮绿.png'
button_tou_filename = 'image/touzi2.png'
# 玩家
player_test_filename = 'image/testplayer.png'
p1_filename = 'image/p1.png'
p2_filename = 'image/p2.png'
p3_filename = 'image/p3.png'
p4_filename = 'image/p4.png'
# 玩家头像
t1 = 'image/t01.png'
t2 = 'image/t02.png'
t3 = 'image/t03.png'
t4 = 'image/t04.png'

# 特殊block的贴图
start_block_filename = 'image/start.png'
jianyu_block_filename = 'image/jianyu.png'
# 对话框
forword_filename = 'image/forword.png'
# start界面图片
startbg = 'image/start_bg.jpg'


# 创建屏幕类
class Myscreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 373), 0, 32)
        self.pic_group = []

    def sc_add(self,pic,pos):
        self.pic_group.append((pic,pos))

    def sc_show(self):
        for i in self.pic_group:
            self.screen.blit(i[0], i[1])

    def sc_update(self):
        pygame.display.update()

    def sc_set(self):
        self.screen = pygame.display.set_mode((1600, 860), 0, 32)


# 创建鼠标类
class Gamemouse:
    def __init__(self):
        self.x = None
        self.y = None
        self.pos = None

    def get_mouse(self):
        self.x, self.y = self.pos = pygame.mouse.get_pos()

    def show(self):
        screen.screen.blit(mouse_icon, self.pos)


# 创建选项按钮和对话框内容类(将按钮和对话框作为一个整体)
class Button:
    def __init__(self):
        self.flag = 0
        self.touflag = 0
        self.word_yes = make_words(pygame, '是', 30)
        self.word_no = make_words(pygame, '否', 30)


    def newset(self):
        self.flag = 1



    def show_button(self):
        if self.flag == 1:
            if button_yes.collidepoint(mouse.x, mouse.y):
                screen.screen.blit(button_in, (515, 620)) # 添加yes按钮至屏幕显示列表
            else:
                screen.screen.blit(button_out, (515, 620))
            if button_no.collidepoint(mouse.x,mouse.y):
                screen.screen.blit(button_in, (865, 620)) # 添加no按钮至屏幕显示按钮
            else:
                screen.screen.blit(button_out, (865, 620))

            screen.screen.blit(self.word_yes, (595, 634))
            screen.screen.blit(self.word_no, (945, 634))

    def tou(self):
        if self.touflag == 1:
            screen.screen.blit(button_tou, (750, 600))  # 显示投骰子按钮

    def show_tou(self):
        self.touflag = 1

    def tou_disappear(self):
        self.touflag = 0

    def disappear(self):
        self.flag = 0

    def yes_or_no(self):
        self.flag = 1
        if event.type == MOUSEBUTTONDOWN and button.flag == 1:
            if button_yes.collidepoint(mouse.x, mouse.y):
                self.flag = 0
                print('yes')
                return True
            if button_no.collidepoint(mouse.x, mouse.y):
                self.flag = 0
                print('no')
                return False


# 创建投骰子和人物移动的相关动作类
class Tou:
    def __init__(self):
        self.framerate = pygame.time.Clock()
        self.dice = Mysprite((720, 225))
        self.dice.load('image/两排128.png', 128, 128, 3)
        self.group = pygame.sprite.Group()
        self.group.add(self.dice)
        self.show_flag = 0
        self.showend_flag = 0
        # print(1)

    def setself(self):
        self.st = time.clock()
        self.framerate.tick(60)
        self.ticks = pygame.time.get_ticks()
        self.group.update(self.ticks, 120)

    def show(self):
        self.show_flag = 1

    def disappear(self):
        self.show_flag = 0

    def showend(self):
        self.showend_flag = 1

    def enddisappear(self):
        self.showend_flag = 0


# 文字类
class Word():
    def __init__(self):
        self.test1 = make_words(pygame, "埃索达", 28)  # 1号块名称
        self.test2 = make_words(pygame, "暴风城", 28)  # 2号块名称
        self.test3 = make_words(pygame, "铁炉堡", 28)  # 3号块名称
        self.test4 = make_words(pygame, "雷霆崖", 28)  # 4号块名称
        self.test5 = make_words(pygame, "斯坦索姆", 24)  # 5号块名称
        self.test6 = make_words(pygame, "锦绣谷", 28)  # 6号块名称
        self.test7 = make_words(pygame, "达拉然", 28)  # 7号块名称
        self.test8 = make_words(pygame, '002', 24)
        self.test9 = make_right_word(pygame, '湖畔镇', 28)
        self.test10 = make_right_word(pygame, '闪金镇', 28)
        self.test11 = make_right_word(pygame, '幽暗城', 28)
        self.test12 = make_right_word(pygame, '银月城', 28)
        self.test13 = make_right_word(pygame, '斯坦索姆', 24)
        self.test14 = make_words(pygame, '塞拉摩', 28)
        self.test15 = make_words(pygame, '祖阿曼', 28)
        self.test16 = make_words(pygame, '加基森', 28)
        self.test17 = make_words(pygame, '达纳苏斯', 24)
        self.test18 = make_words(pygame, '西部荒野', 24)
        self.test19 = make_words(pygame, '夜色镇', 28)
        self.test20 = make_words(pygame, '辛特兰', 28)
        self.test21 = make_words(pygame, '赤脊山', 28)
        self.test22 = make_words(pygame, '022', 28)
        self.test23 = make_left_word(pygame, '奥格瑞玛', 24)
        self.test24 = make_left_word(pygame, '丹莫罗', 28)
        self.test25 = make_left_word(pygame, '永歌森林', 24)
        self.test26 = make_left_word(pygame, '千针石林', 24)
        self.test27 = make_left_word(pygame, '灰  谷', 28)


    def show(self):
        screen.screen.blit(self.test1, (444, 94))
        screen.screen.blit(self.test2, (549, 94))
        screen.screen.blit(self.test3, (649, 94))
        screen.screen.blit(self.test4, (749, 94))
        screen.screen.blit(self.test5, (847, 94))
        screen.screen.blit(self.test6, (956, 94))
        screen.screen.blit(self.test7, (1056, 94))
        screen.screen.blit(self.test9, (1187, 179))
        screen.screen.blit(self.test10, (1187, 283))
        screen.screen.blit(self.test11, (1187, 387))
        screen.screen.blit(self.test12, (1187, 491))
        screen.screen.blit(self.test13, (1187, 586))
        screen.screen.blit(self.test15, (1056, 721))
        screen.screen.blit(self.test16, (956, 721))
        screen.screen.blit(self.test17, (847, 721))
        screen.screen.blit(self.test18, (749, 721))
        screen.screen.blit(self.test19, (649, 721))
        screen.screen.blit(self.test20, (549, 721))
        screen.screen.blit(self.test21, (444, 721))
        screen.screen.blit(self.test23, (361, 177))
        screen.screen.blit(self.test24, (361, 283))
        screen.screen.blit(self.test25, (361, 381))
        screen.screen.blit(self.test26, (361, 483))
        screen.screen.blit(self.test27, (361, 591))


# 创建对话框类
class DialogBox:
    def __init__(self):
        self.forbuy = make_words(pygame, '是否购买当前土地?', 30)
        self.forbuild = make_words(pygame, '是否在当前土地升级建筑?', 30)
        self.showbuy = 0
        self.showbuild = 0

    def ifbuy(self):
        if self.showbuy == 1:
            screen.screen.blit(self.forbuy, (530, 500))
            screen.screen.blit(forword, (500, 470))

    def ifbuild(self):
        if self.showbuild == 1:
            screen.screen.blit(self.forbuild, (530, 500))
            screen.screen.blit(forword, (500,470))

    def show_buy(self):
        self.showbuy = 1

    def show_build(self):
        self.showbuild = 1

    def disappear(self):
        if self.showbuy == 1:
            self.showbuy = 0
        if self.showbuild == 1:
            self.showbuild = 0

# 创建信息框
class Info:
    def __init__(self):
        pass

    def t_show(self):
        screen.screen.blit(p1t, (8, 8))
        screen.screen.blit(p2t, (1454, 8))
        screen.screen.blit(p3t, (8, 688))
        screen.screen.blit(p4t, (1454, 688))

    def p1_info(self):
        name = make_words(pygame, p1.name, 28)
        screen.screen.blit(name, (50, 133))
        money = make_words(pygame, '资金:' + str(p1.money), 26)
        screen.screen.blit(money, (46, 218))

    def p2_info(self):
        name = make_words(pygame, p2.name, 28)
        screen.screen.blit(name, (1486, 133))
        money = make_words(pygame, '资金:' + str(p2.money), 26)
        screen.screen.blit(money, (1420, 218))

    def p3_info(self):
        name = make_words(pygame, p3.name, 28)
        screen.screen.blit(name, (46, 815))
        money = make_words(pygame, '资金:' + str(p3.money), 26)
        screen.screen.blit(money, (44, 615))

    def p4_info(self):
        name = make_words(pygame, p4.name, 28)
        screen.screen.blit(name, (1486, 815))
        money = make_words(pygame, '资金:' + str(p4.money), 26)
        screen.screen.blit(money, (1420, 615))

    def player_info_show(self):
        self.p1_info()
        self.p2_info()
        self.p3_info()
        self.p4_info()
# 全局用 nn  表示回合内阶段
nn = 0  # 用以区分阶段
# 定义的全局函数
def turn():
    global player, nn
    print(player.name)
    block = player.block
    if block.num in [0,8,14,22]:
        turn_end()
    if nn == 0:  # 0代表还未投骰子阶段
        button.show_tou()
    if nn == 1:
        if block.belong == 0:
            if player.money >= block.price:
                button.newset()
                dialogbox.show_buy()
                if button.yes_or_no() is True:
                    button.disappear()
                    dialogbox.disappear()
                    nn += 1
                    player.money -= block.price
                    print(1)
                    block.belong = player.num
                if button.yes_or_no() is False:
                    button.disappear()
                    dialogbox.disappear()
                    nn += 1
        elif block.belong == player.num:
            if block.buildlevel == 3:
                nn += 1
            if block.buildlevel < 3:
                if player.money >= block.buildmoney:
                    button.newset()
                    if button.yes_or_no() is True:
                        button.disappear()
                        player.money -= block.buildmoney
                        block.buildlevel += 1
                        nn += 1
                    if button.yes_or_no() is False:
                        button.disappear()
                        nn += 1
                else:
                    nn += 1
        else:
            if player.money >= block.passmoney:
                player.money -= block.passmoney
                exec('p'+str(block.belong)+'.money+=block.passmoney')
                nn += 1
            else:
                exec('p'+str(block.belong)+'.money+=player.money')
                player.pc()
                players.remove(player)
                nn += 1
    if nn == 2:
        if len(players) == 1:
            print(players[0].name + '---winner')

        else:
            nn -= 2
            turn_end()







# 回合结束函数
def turn_end():
    global player
    if players.index(player) <= 2:
        player = players[players.index(player) + 1]
        return
    else:
        player = players[0]
        return


# buy_block 购买土地函数
def buy_block(player,block):
    player.money -= block.price
    block.belong = player.num


# build_block 土地建筑函数
def build_block(player, block):
    block.buildlevel += 1
    player.money -= block.buildmoney


# pay_passmoney 支付过路费函数
def pay_passmoney(player,block):
    player.money -= block.passmoney
    exec('p'+str(block.belong)+'.money+=block.passmoney')


# payd_passmoney  现金不够支付过路费时,清算破产
def payd_passmoney(player,block):
    exec('p' + str(block.belong) + '.money+=player.money')
    players.remove(eval('p' + str(block.belong)))


# 游戏的回合显示逻辑函数

# 创建屏幕对象实例
screen = Myscreen()
# 创建鼠标对象实例
mouse = Gamemouse()
# 创建文字实例
word = Word()
# 创建按钮对象实例
button = Button()
# 创建对话框实例
dialogbox = DialogBox()

# 为每个方块和按钮建立rect对象
# 为按钮创建rect对象
button_yes = pygame.Rect((515, 620), (198, 72))
button_no = pygame.Rect((865, 620), (198, 72))
button_toutouzi = pygame.Rect((750, 600), (64, 64))
# 为地图快创建rect对象
block_rect0 = pygame.Rect((262, 0), (174, 174))  # 为0号方块创建rect对象
block_rect1 = pygame.Rect((438, 0), (100, 140))  # 为1号方块创建rect对象
block_rect2 = pygame.Rect((540, 0), (100, 140))  # 为2号方块创建rect对象
block_rect3 = pygame.Rect((642, 0), (100, 140))  # 为3号方块创建rect对象
block_rect4 = pygame.Rect((744, 0), (100, 140))  # 为4号方块创建rect对象
block_rect5 = pygame.Rect((846, 0), (100, 140))  # 为5号方块创建rect对象
block_rect6 = pygame.Rect((948, 0), (100, 140))  # 为6号方块创建rect对象
block_rect7 = pygame.Rect((1050, 0), (100, 140))  # 为7号方块创建rect对象
block_rect8 = pygame.Rect((1152, 0), (174, 174))  # 为8号方块创建rect对象
block_rect9 = pygame.Rect((1186, 174), (140, 100))  # 为9号方块创建rect对象
block_rect10 = pygame.Rect((1186, 276), (140, 100))  # 为10号方块创建rect对象
block_rect11 = pygame.Rect((1186, 378), (140, 100))  # 为11号方块创建rect对象
block_rect12 = pygame.Rect((1186, 480), (140, 100))  # 为12号方块创建rect对象
block_rect13 = pygame.Rect((1186, 582), (140, 100))  # 为13号块创建rect对象
block_rect14 = pygame.Rect((1152, 684), (174, 174))  # 为14号块创建rect对象
block_rect15 = pygame.Rect((1050, 718), (100, 140))  # 为15号块创建rect对象
block_rect16 = pygame.Rect((948, 718), (100, 140))  # 为16号块创建rect对象
block_rect17 = pygame.Rect((846, 718), (100, 140))  # 为17号块创建rect对象
block_rect18 = pygame.Rect((744, 718), (100, 140))  # 为18号块创建rect对象
block_rect19 = pygame.Rect((642, 718), (100, 140))  # 为19号块创建rect对象
block_rect20 = pygame.Rect((540, 718), (100, 140))  # 为20号块创建rect对象
block_rect21 = pygame.Rect((438, 718), (100, 140))  # 为21号块创建rect对象
block_rect22 = pygame.Rect((262, 684), (174, 174))  # 为22号块创建rect对象
block_rect23 = pygame.Rect((262, 582), (140, 100))  # 为23号块创建rect对象
block_rect24 = pygame.Rect((262, 480), (140, 100))  # 为24号块创建rect对象
block_rect25 = pygame.Rect((262, 378), (140, 100))  # 为25号块创建rect对象
block_rect26 = pygame.Rect((262, 276), (140, 100))  # 为26号块创建rect对象
block_rect27 = pygame.Rect((262, 174), (140, 100))  # 为27号块创建rect对象

# 游戏图片预载
icon = pygame.image.load(title_icon_filename)
big_bg = pygame.image.load(big_bg_filename).convert()  # 预载背景大图
mouse_icon = pygame.image.load(mouse_filename).convert_alpha()  # 预载鼠标贴图
player_show = pygame.image.load(player_show_filename).convert_alpha()  # 预载人物头像框
player_info_left = pygame.image.load(player_info_left_filename).convert_alpha()  # 预载左侧人物信息框
player_info_right = pygame.image.load(player_info_right_filename).convert_alpha()  # 预载右侧人物信息框
big_block = pygame.image.load(big_block_filename).convert_alpha()  # 预载四角大方块 _alpha设置透明
top_lightblue_block = pygame.image.load(top_light_blue_filename).convert_alpha()  # 预载上方浅蓝色方块 透明
top_pink_block = pygame.image.load(top_pink_filename).convert_alpha()  # 预载上方粉色块 透明
top_darkblue_block = pygame.image.load(top_dark_blue_filename).convert_alpha()  # 预载上方深蓝方块 透明
right_light_purple_block = pygame.image.load(right_light_purple_filename).convert_alpha()  # 预载右方粉紫块
right_pink_block = pygame.image.load(right_pink_filename).convert_alpha()  # 预载右方粉色块
right_dark_purple_block = pygame.image.load(right_dark_purple_filename).convert_alpha()  # 预载右方深紫块
bottom_dark_purple_block = pygame.image.load(bottom_dark_purple_filename).convert_alpha()  # 预载下方深紫块
bottom_pink_block = pygame.image.load(bottom_pink_filename).convert_alpha()  # 预载下方粉块
bottom_orange_block = pygame.image.load(bottom_orange_filename).convert_alpha()  # 预载下方橘色方块
left_green_block = pygame.image.load(left_green_filename).convert_alpha()  # 预载左侧绿色块
left_pink_block = pygame.image.load(left_pink_filename).convert_alpha()  # 预载左侧粉色方块
left_lightblue_block = pygame.image.load(left_light_blue_filename).convert_alpha()  # 预载左侧淡蓝色块
# 骰子点数图预载
tou1 = pygame.image.load(tou1_filename).convert_alpha()
tou2 = pygame.image.load(tou2_filename).convert_alpha()
tou3 = pygame.image.load(tou3_filename).convert_alpha()
tou4 = pygame.image.load(tou4_filename).convert_alpha()
tou5 = pygame.image.load(tou5_filename).convert_alpha()
tou6 = pygame.image.load(tou6_filename).convert_alpha()
# 按钮预载
button_in = pygame.image.load(button_in_filename).convert_alpha()
button_out = pygame.image.load(button_out_filename).convert_alpha()
button_tou = pygame.image.load(button_tou_filename).convert_alpha()
# 玩家人物预载
testplayer = pygame.image.load(player_test_filename).convert_alpha()
p1p = pygame.image.load(p1_filename).convert_alpha()
p2p = pygame.image.load(p2_filename).convert_alpha()
p3p = pygame.image.load(p3_filename).convert_alpha()
p4p = pygame.image.load(p4_filename).convert_alpha()
# 玩家人物预载
p1t = pygame.image.load(t1).convert_alpha()
p2t = pygame.image.load(t2).convert_alpha()
p3t = pygame.image.load(t3).convert_alpha()
p4t = pygame.image.load(t4).convert_alpha()

# start界面图像预载
start_bg = pygame.image.load(startbg).convert_alpha()
# 特殊方块的贴图
start_block = pygame.image.load(start_block_filename).convert_alpha()
jianyu_block = pygame.image.load(jianyu_block_filename).convert_alpha()
# 对话框图片预载
forword = pygame.image.load(forword_filename).convert_alpha()

# 给画面添加图片元素
# 添加背景图片
screen.sc_add(big_bg, (0, 0))
screen.sc_add(player_show, (8, 8))
screen.sc_add(player_info_left, (8, 182))
screen.sc_add(player_show, (8, 688))
screen.sc_add(player_info_left, (8, 577))
screen.sc_add(player_show, (1454, 8))
screen.sc_add(player_info_right, (1376, 182))
screen.sc_add(player_show, (1454, 688))
screen.sc_add(player_info_right, (1370, 578))
screen.sc_add(big_block, (262, 0))  # 显示0处大方块 定义左上角第一块为0号 编号顺时针依次递增1
screen.sc_add(top_lightblue_block, (438, 0))  # 显示1处方块
screen.sc_add(top_pink_block, (540, 0))  # 显示2处方块
screen.sc_add(top_lightblue_block, (642, 0))  # 显示3处方块
screen.sc_add(top_darkblue_block, (744, 0))  # 显示4处方块
screen.sc_add(top_darkblue_block, (846, 0))  # 显示5处方块
screen.sc_add(top_pink_block, (948, 0))  # 显示6处方块
screen.sc_add(top_darkblue_block, (1050, 0))  # 显示7处方块
screen.sc_add(big_block, (1152, 0))  # 显示8处大方块
screen.sc_add(right_light_purple_block, (1186, 174))  # 显示9处方块
screen.sc_add(right_pink_block, (1186, 276))  # 显示10处方块
screen.sc_add(right_light_purple_block, (1186, 378))  # 显示11处方块
screen.sc_add(right_light_purple_block, (1186, 480))  # 显示12处方块
screen.sc_add(right_dark_purple_block, (1186, 582))  # 显示13处方块
screen.sc_add(big_block, (1152, 684))  # 显示14处大方块
screen.sc_add(bottom_dark_purple_block, (1050, 718))  # 显示15处方块
screen.sc_add(bottom_pink_block, (948, 718))  # 显示16处块
screen.sc_add(bottom_dark_purple_block, (846, 718))  # 显示17处块
screen.sc_add(bottom_orange_block, (744, 718))  # 显示18处块
screen.sc_add(bottom_orange_block, (642, 718))  # 显示19处块
screen.sc_add(bottom_pink_block, (540, 718))  # 显示20处块
screen.sc_add(bottom_orange_block, (438, 718))  # 显示21处块
screen.sc_add(big_block, (262, 684))  # 显示22处块
screen.sc_add(left_green_block, (262, 582))  # 显示23处块
screen.sc_add(left_pink_block, (262, 480))  # 显示24处块
screen.sc_add(left_green_block, (262, 378))  # 显示25处块
screen.sc_add(left_green_block, (262, 276))  # 显示26处块
screen.sc_add(left_lightblue_block, (262, 174))  # 显示27处块
screen.sc_add(start_block, (262,0)) # 0号方块的贴图
screen.sc_add(jianyu_block, (1152, 684)) # 14号块的贴图
# screen.sc_add(forword, (500, 470)) # 对话框

pygame.mouse.set_visible(False)
n = 0  # 阶段标记数
pygame.init()
# 建立游戏开始界面的循环
# 由于流程比较简单 所以用面向过程的方式来解决
pygame.display.set_caption('大富翁')
pygame.display.set_icon(icon)

# 游戏开始界面的各种元素
# 文字
test_st1 = make_words(pygame, '单人游戏', 28)
test_st2 = make_words(pygame, '多人游戏', 28)

button_1 = pygame.Rect((150, 100), (198, 72))
button_2 = pygame.Rect((150, 200), (198, 72))
while n == 0:

    startscreen = pygame.display.set_mode((500,373))
    startscreen.blit(start_bg, (0, 0))
    mouse.get_mouse()
    startscreen.blit(button_out, (150, 100))
    startscreen.blit(button_out, (150, 200))
    if button_1.collidepoint(mouse.x,mouse.y):
        startscreen.blit(button_in, (150, 100))

    if button_2.collidepoint(mouse.x,mouse.y):
        startscreen.blit(button_in, (150, 200))
    startscreen.blit(test_st1, (190, 115))
    startscreen.blit(test_st2, (190, 215))

    for event in pygame.event.get():  # pygame模块自带的事件捕捉
        if event.type == QUIT:  # 发生点击右上角退出的事件
            exit()
        if event.type == K_ESCAPE:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if button_1.collidepoint(mouse.x,mouse.y):
                n = 2
            if button_2.collidepoint(mouse.x,mouse.y):
                n = 3

    mouse.show()
    pygame.display.update()


pygame.init()
screen.sc_set()
tou = Tou()
# 单人游戏模式下的实例
p1 = Player('test', 10000, 0, p1p)
p2 = Player('test2', 10000, 2, p2p)
p3 = Player('test3', 10000, 4, p3p)
p4 = Player('test4', 10000, 6, p4p)
# 创建信息框实例
info = Info()
# 建立人物循环
player = p1
players = [p1, p2, p3, p4]


# 建立游戏单机模式主体循环
pygame.display.set_caption('大富翁----【单人模式】')
# 循环外部变量
tou.show_flag = 0
move = 0

while n == 2:

    for event in pygame.event.get():  # pygame模块自带的事件捕捉
        if event.type == QUIT:  # 发生点击右上角退出的事件
            exit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                button.disappear()
            if event.key == pygame.K_SPACE:
                button.newset()
            if event.key == K_d:
                dialogbox.show_buy()
            if event.key == K_b:
                dialogbox.show_build()
            if event.key == K_a:
                dialogbox.disappear()
            if event.key == K_n:
                button.show_tou()
            if event.key == K_m:
                button.tou_disappear()

        if event.type == MOUSEBUTTONDOWN and button.touflag == 1:
            if button_toutouzi.collidepoint(mouse.x,mouse.y):
                button.touflag = 0
                nn += 1
                # print(0)
                st = time.clock()
                # print(st)
                tou.show()
                dice = random.randint(1, 6)
                tou.showend_flag = 1
                move = 1

    turn()

    tou.setself()
    screen.sc_show()
    mouse.get_mouse()
    button.show_button()
    button.tou()
    dialogbox.ifbuy()
    dialogbox.ifbuild()

    if tou.show_flag == 1:
        tou.group.draw(screen.screen)
    if tou.showend_flag == 1 and 5 < time.clock() - st < 6.5:
        eval('screen.screen.blit(tou' + str(dice) + ',(720,225))')
    if time.clock() - st > 5:
        tou.disappear()
    if 6.5 < time.clock() - st and move == 1:
        player.move(dice)
        move = 0


    # 显示block上的文字名称

    p1.show_player(screen.screen)
    p2.show_player(screen.screen)
    p3.show_player(screen.screen)
    p4.show_player(screen.screen)
    word.show()

    info.t_show()
    info.player_info_show()

    mouse.show()
    screen.sc_update()

# 多人模式的游戏循环
# 创建实例

# pygame.display.set_caption('大富翁----【多人游戏】')
# while n == 3:
#
#     for event in pygame.event.get():  # pygame模块自带的事件捕捉
#         if event.type == QUIT:  # 发生点击右上角退出的事件
#             exit()
#         if event.type == KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 button.disappear()
#             if event.key == pygame.K_SPACE:
#                 button.newset()
#
#     screen.sc_show()
#     mouse.get_mouse()
#     button.show_button()
#     button.show_tou()
#     mouse.show()
#
#     screen.sc_update()

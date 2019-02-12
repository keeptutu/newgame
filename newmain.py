import random
import time
import pygame
from pygame.locals import *
from sys import *
from mysprite import *
from words import *
from toutouzi import *
from player import *

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


# 创建屏幕类
class Myscreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1600, 860), 0, 32)
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


# 创建投骰子和人物移动的相关动作类
class Tou:
    def __init__(self):
        pass

# 创建屏幕对象实例
screen = Myscreen()
# 创建鼠标对象实例
mouse = Gamemouse()

# 游戏图片预载
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
screen.sc_add(button_out, (515, 620))  # 显示yes按钮
screen.sc_add(button_out, (865, 620))  # 显示no按钮
screen.sc_add(button_tou, (750, 600))  # 显示投骰子按钮
pygame.mouse.set_visible(False)
n = 1
# 建立游戏开始界面的循环
while n == 1:
    for event in pygame.event.get():  # pygame模块自带的事件捕捉
        if event.type == QUIT:  # 发生点击右上角退出的事件
            n = 0

    startscreen = pygame.display.set_mode((700,600))

pygame.init()
screen.sc_set()
# 建立游戏主体循环
while 1:

    for event in pygame.event.get():  # pygame模块自带的事件捕捉
        if event.type == QUIT:  # 发生点击右上角退出的事件
            exit()

    screen.sc_show()
    mouse.get_mouse()
    mouse.show()
    screen.sc_update()


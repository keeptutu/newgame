import random
import time
import pygame
from pygame.locals import *
from sys import *
from mysprite import *
from words import *
from toutouzi import *
from player import *
'''
建立了游戏的主循环
显示了地图块
建立了点击投骰子的事件
创建了yes和no和投骰子三个互动按钮
为每个地图块和按钮块创建了对应的rect对象
'''

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

pygame.init()  # 游戏初始化 让电脑硬件做好准备

screen = pygame.display.set_mode((1600, 860), 0, 32)  # 创建游戏主屏幕
pygame.display.set_caption('大富翁demo')  # 给游戏窗口建立名称

icon = pygame.image.load(title_icon_filename)  # 加载窗口图标
pygame.display.set_icon(icon)  # 设置窗口图标

# 游戏图片加载
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
# 初始化玩家
p1 = Player('tutu')


# 文字
# 定义文字Surface对象旋转的函数
def make_right_word(pygame,s,size):
    test = make_words(pygame,s,size)
    test = pygame.transform.rotate(test, 90)
    return test


test1 = make_words(pygame, "太吾村", 28)  # 在1号块上显示名称
test2 = make_words(pygame, "暴风城", 28)  # 在2号块上显示名称
test3 = make_words(pygame, "浣熊市", 28)  # 在3号块上显示名称
test4 = make_words(pygame, "雷霆崖", 28)  # 在4号块上显示名称
test5 = make_words(pygame, "斯坦索姆", 24)  # 在5号块上显示名称
test6 = make_words(pygame, "锦绣谷", 28)  # 在6号块上显示名称
test7 = make_words(pygame, "达拉然", 28)  # 在7号块上显示名称
test9 = make_right_word(pygame, "艾欧尼亚", 24)  # 在9号块上显示名称
test10 = make_right_word(pygame, "湖畔镇", 28)  # 在10号块上显示名称
test11 = make_right_word(pygame, "闪金镇", 28)  # 在11号块上显示名称
test12 = make_right_word(pygame, "幽暗城", 28)  # 在12号块上显示名称


# 精灵事件
framerate = pygame.time.Clock()  # 精灵事件计时
dice = Mysprite((720, 225))  # 精灵的显示位置
dice.load('image/两排128.png', 128, 128, 3)  # 精灵图片的载入及选中框的大小和每行的帧图数
group = pygame.sprite.Group()  # 创建精灵组对象
group.add(dice)  # 在精灵组中加入dice精灵

#  循环外部变量
st = 0
tou = 0
n = 0
pm = 0
player = 'player1'
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

# 游戏主循环 (用于刷新屏幕)
while 1:
    framerate.tick(100)  # 主循环的刷新率
    ticks = pygame.time.get_ticks()  # tick获取时间
    group.update(ticks, 150)  # 精灵画面的刷新 此处的第二个参数越大 刷新越慢
    mouse_pos = x, y = pygame.mouse.get_pos()  # 捕获鼠标的位置
    screen.blit(big_bg, (0, 0))  # (0,0)处绘制对象图片 屏幕左上角点坐标为(0,0) x取右为正 y取下为正
    screen.blit(player_show, (8, 8))  # 绘制左上角人物头像框
    screen.blit(player_info_left, (8, 182))  # 绘制左上角人物信息框
    screen.blit(player_show, (8, 688))  # 绘制左下角人物头像框
    screen.blit(player_info_left, (8, 577))  # 绘制左下角人物信息框
    screen.blit(player_show, (1454, 8))  # 绘制右上人物头像框
    screen.blit(player_info_right, (1376, 182))  # 绘制右上人物信息框
    screen.blit(player_show, (1454, 688))  # 绘制右下人物头像框
    screen.blit(player_info_right, (1370, 578))
    screen.blit(big_block, (262, 0))  # 显示0处大方块 定义左上角第一块为0号 编号顺时针依次递增1
    screen.blit(top_lightblue_block, (438, 0))  # 显示1处方块
    screen.blit(top_pink_block, (540, 0))  # 显示2处方块
    screen.blit(top_lightblue_block, (642, 0))  # 显示3处方块
    screen.blit(top_darkblue_block, (744, 0))  # 显示4处方块
    screen.blit(top_darkblue_block, (846, 0))  # 显示5处方块
    screen.blit(top_pink_block, (948, 0))  # 显示6处方块
    screen.blit(top_darkblue_block, (1050, 0))  # 显示7处方块
    screen.blit(big_block, (1152, 0))  # 显示8处大方块
    screen.blit(right_light_purple_block, (1186, 174))  # 显示9处方块
    screen.blit(right_pink_block, (1186, 276))  # 显示10处方块
    screen.blit(right_light_purple_block, (1186, 378))  # 显示11处方块
    screen.blit(right_light_purple_block, (1186, 480))  # 显示12处方块
    screen.blit(right_dark_purple_block, (1186, 582))  # 显示13处方块
    screen.blit(big_block, (1152, 684))  # 显示14处大方块
    screen.blit(bottom_dark_purple_block, (1050, 718))  # 显示15处方块
    screen.blit(bottom_pink_block, (948, 718))  # 显示16处块
    screen.blit(bottom_dark_purple_block, (846, 718))  # 显示17处块
    screen.blit(bottom_orange_block, (744, 718))  # 显示18处块
    screen.blit(bottom_orange_block, (642, 718))  # 显示19处块
    screen.blit(bottom_pink_block, (540, 718))  # 显示20处块
    screen.blit(bottom_orange_block, (438, 718))  # 显示21处块
    screen.blit(big_block, (262, 684))  # 显示22处块
    screen.blit(left_green_block, (262, 582))  # 显示23处块
    screen.blit(left_pink_block, (262, 480))  # 显示24处块
    screen.blit(left_green_block, (262, 378))  # 显示25处块
    screen.blit(left_green_block, (262, 276))  # 显示26处块
    screen.blit(left_lightblue_block, (262, 174))  # 显示27处块
    screen.blit(button_out,(515, 620))  # 显示yes按钮
    screen.blit(button_out,(865, 620))  # 显示no按钮
    screen.blit(button_tou,(750, 600))  # 显示投骰子按钮
    if button_yes.collidepoint(x, y):  # 如果鼠标位于按钮yes上
        screen.blit(button_in, (515, 620))   # 按钮加载绿色图像来反应
    if button_no.collidepoint(x, y):  # no按钮同yes按钮
        screen.blit(button_in, (865, 620))
    for event in pygame.event.get():  # pygame模块自带的事件捕捉
        if event.type == QUIT:  # 发生点击右上角退出的事件
            exit()  # 通过sys模块导入的exit退出
        if event.type == KEYDOWN:  # 捕捉到键盘事件
            if event.key == pygame.K_ESCAPE:  # 检测到按下esc键
                exit()  # 退出
        if event.type == MOUSEBUTTONDOWN and button_toutouzi.collidepoint(x, y):  # 如果鼠标点击了投骰子按钮
            dice = random.randint(1,6)  # 通过randint获得本次投骰子投得的点数 作为本回合玩家移动的步数
            tou = 1  # 将外部变量tou的值改为1 表示骰子显示
            if n == 0:  # 使用外部变量n
                st = time.clock()  # 点击时开始一个计时
                n = 1  # 将n改为1

        if event.type == MOUSEBUTTONDOWN and button_yes.collidepoint(x, y):
            print(1)
        if event.type == MOUSEBUTTONDOWN and button_no.collidepoint(x, y):
            print(2)

    if tou == 1 and time.clock() - st <= 2.5:  # 从点击时开始计时 2.5秒内
        eval('group.draw(screen)')  # 显示骰子精灵动图
        n = 0  # 将n改回1 返回原状态

    if tou == 1 and 2.5 < time.clock() - st <= 4:  # 计时的2.5-5秒内 显示点数对应的骰子图
        eval('screen.blit(tou' + str(dice) + ',(720,225))')  # 通过eval语句来显示不同情况下对应的骰子图
        pm = 1
    if 4 < time.clock() - st < 5 and pm == 1:
        p1.move(dice)
        pm = 0
    p1.show_player(screen, testplayer)
    pygame.mouse.set_visible(False)  # 关闭原始鼠标贴图
    screen.blit(test1, (444, 94))  # 显示1号block名称
    screen.blit(test2, (549, 94))  # 显示2号block名称
    screen.blit(test3, (649, 94))  # 显示3号block名称
    screen.blit(test4, (749, 94))  # 显示4号block名称
    screen.blit(test5, (847, 94))  # 显示5号block名称
    screen.blit(test6, (956, 94))  # 显示6号block名称
    screen.blit(test7, (1056, 94))  # 显示7号block名称
    screen.blit(test9, (1187, 179))  # 显示9号block名称
    screen.blit(test10, (1187, 283))  # 显示10号block名称
    screen.blit(test11, (1187, 387))  # 显示10号block名称

    screen.blit(mouse_icon, mouse_pos)  # 在鼠标位置显示自定义的鼠标贴图
    pygame.display.update()  # 屏幕刷新 使画面更新

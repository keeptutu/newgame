import pygame
from pygame.locals import *
from sys import *
from words import *
'''

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

# 文字
test1 = make_words(pygame,"太吾村",28)


# 游戏主循环 (用于刷新屏幕)
while 1:
    for event in pygame.event.get():  # pygame模块自带的事件捕捉
        if event.type == QUIT:  # 发生点击右上角退出的事件
            exit()  # 通过sys模块导入的exit退出
        if event.type == KEYDOWN:  # 捕捉到键盘事件
            if event.key == pygame.K_ESCAPE:  # 检测到按下esc键
                exit()  # 退出
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
    block_rect1 = pygame.Rect((262, 0), (174, 174))  # 为1号方块创建rect对象
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

    pygame.mouse.set_visible(False)  # 关闭原始鼠标贴图
    screen.blit(test1, (444, 94))  # 显示1号block名称
    screen.blit(mouse_icon, mouse_pos)  # 在鼠标位置显示自定义的鼠标贴图
    if block_rect1.collidepoint(x,y):
        print(1)

    pygame.display.update()  # 屏幕刷新 使画面更新


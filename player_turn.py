import random
players = ['player1','player2','player3','player4']


def turn_start():
    global player
    player = 'player1'


def is_my_turn(pp):
    if pp == 'player1':
        return True

    else:
        return False


def turn_end():
    global player
    if players.index(player) <= 2:
        player = players[players.index(player) + 1]
        return player
    else:
        player = players[0]
        return player

# 掷骰子操作
def tou():
    return random.randint(1,6)

# 具体建造函数
def jianzao():
    #玩家点击对话框确定是否建造,提供对话框显示,玩家点击选择true或false
    # 返回结果为布尔值
    result = input("您金钱足够,是否需要建造?true/false")
    return result

# 参数为建筑等级,返回过路费
def pass_moneys(block_buildlevel):
    # 如果建筑等级为1
    if block_buildlevel == 1:
        pass_money=2400
    #为2 
    elif block_buildlevel == 2:
        pass_money=4800
    # 为3
    elif block_buildlevel == 3:
        pass_money=8800
    # 返回过路费
    return pass_money



# 回合结束
def button_for_turnend():
    turn_end()

# 占地方法
def buy_block():
    #玩家点击对话框确定是否占空地,提供对话框显示,玩家点击选择true或false
    # 返回结果为布尔值
    res = input("此处为空地,是否占地?true/false")
    return res


def turn(player,block,block_buildlevel):
    # 掷骰子
    tou()
    # 如果土地归属为玩家归属
    if block.belong == player.belong:
        # 建筑等级小于3
        if block_buildlevel < 3:
            # 玩家金钱大于建筑升级所需金钱
            if player.money >= block.update_money:
                # 建造
                if jianzao():
                    # 玩家金币扣除操作
                    player.money -= block.update_money
                    # 建筑等级加一
                    block_buildlevel += 1
                #玩家取消建造,本回合结束
                else:
                    button_for_turnend()
            # 玩家金钱小于建筑升级所需金钱
            else:
                button_for_turnend()
        # 建筑已满级
        else:
            button_for_turnend()
    # 如果土地归属为空
    elif block.belong == 0:
        # 如果玩家金钱大于土地金币
        if player.money >= block.buymoney:
            # 是否购买土地(占地)
            if buy_block():
                # 扣除所需金币
                player.money -= block.buymoney
                # 土地归属玩家
                block.belong = player.belong
                # 玩家占地
                block_buildlevel = 0
                # 结束回合
                button_for_turnend()
            # 不购买
            else:
                button_for_turnend()
        #金币缺少
        else:
            button_for_turnend()
    # 该地被其他玩家占有
    else:
        # 根据建筑等级计算出过路费,用pass_money接收
        pass_money = pass_moneys(block_buildlevel)
        # 玩家金币大于过路费
        if player.money >= pass_money:
            # 扣除所需金币
            player.money -= pass_money
            # 显示执行
            eval('player'+str(block.belong)+'.money+=pass_money')
            # 结束
            button_for_turnend()
        # 玩家金币加上抵押房产金币大于过路费
        elif player.money + player.diyamoney >= pass_money:
            # 抵押操作
            player.mortgage()
            # 扣除
            player.money -= pass_money
            # 显示
            eval('player' + str(block.belong) + '.money+=pass_money')
        else:
            # 游戏结束
            player.lose()



if __name__ == '__main__':
    turn_start()
    print(turn_end())
    print(turn_end())
    print(turn_end())
    print(turn_end())
    print(turn_end())
    print(turn_end())







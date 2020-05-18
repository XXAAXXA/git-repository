import time, random

# 开始菜单
print('\n\n————————【21点1.0版本】————————')
print('\n制作人：。')
print('''\n规则介绍：
·本游戏由玩家和一名看不清样貌的庄家(简单的电脑)对抗；
·使用除大小王之外的52张牌，每五局换一副新牌；
·游戏者的目标是使手中的牌的点数之和不超过21点且尽量大；
·K、Q、J和10牌都算作10点，A 牌既可算作1点也可算作11点，由玩家自己决定；
·BlackJack由一张A和一张点数为10的牌组成，比其余任何牌都大，并且输赢筹码翻倍；
·赢得对方所有的筹码获得最终的胜利吧！''')
while True:
    start = input('\n是否开始游戏？\n请输入是：')
    if start == '是':
        break

previously = '''\n\n【前情梗概】：
五分钟前...
你看了一眼手里仅剩的2张红色大钞...
离发工资还有27天...
咬了咬牙走进了面前这家赌场......'''

for words in previously:
    print(words, end='')
    time.sleep(0.2)

# 创建结局
ending = 0    # 没有触发结局
ending1 = '\n     你输了，损失一倍赌注'
ending2 = '\n     你输了，庄家的牌是BlackJack，损失两倍赌注'
ending3 = '\n     你赢了，赢得一倍赌注'
ending4 = '\n     你赢了，你的牌是BlackJack，赢得两倍赌注'
ending5 = '\n     平局，拿回各自的赌注'
ending6 = '\n     下了保险金，庄家是BlackJack'

# 创建筹码
chip_player = 200
chip_dealer = 200

# 扑克牌代表的点数
points_poker = {'A': [1, 11], 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}


# 去'A'函数
def count(copy):
    demo = copy[:]
    demo.remove('A')
    return demo


# 显示筹码函数
def show_chip(chipplayer, chipdealer):
    time.sleep(1.5)
    print('\n————————————————————————————————————')
    print('你现在拥有的筹码数为：%d' % chipplayer)
    print('庄家现在拥有的筹码数：%d' % chipdealer)
    print('————————————————————————————————————')


# 开始游戏
game = 1        # 局数
while game > 0:
    ending = 0  # 重置结局

    time.sleep(3)
    print('\n\n-------【第%d局】-------' % game)
    print('-------【游戏开始】-------')
    # 创建扑克列表
    if game == 1 or game % 5 == 0:
        time.sleep(1)
        print('这是一副新的扑克牌：')
        poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        poker = poker * 4
        print(poker)
        time.sleep(1)
        print('正在洗牌。。。。。。')
        random.shuffle(poker)

    player = []          # 玩家手牌
    count_player = []    # 用于计算的玩家手牌
    dealer = []          # 庄家手牌
    count_dealer = []    # 用于计算的庄家手牌
    points_player = 0    # 玩家点数
    points_dealer = 0    # 庄家点数

    # 下注环节
    time.sleep(2)
    print('\n【下注阶段】')
    time.sleep(1)
    print('     你拥有的筹码数：', chip_player)
    print('     庄家拥有的筹码数：', chip_dealer)
    while True:
        bet = input('\n     请下注：')
        if not bet.isdigit():
            print('     不能下注{}个筹码哦，请重新下注'.format(bet))
            continue
        bet = int(bet)
        if 0 < bet <= chip_player:
            print('     你下注了{}个筹码'.format(bet))
            break
        else:
            print('     不能下注{}个筹码哦，请重新下注'.format(bet))
            continue

    time.sleep(2)
    print('\n【发牌阶段】')
    for i in range(2):
        # 给玩家发两张牌
        a = poker.pop(0)
        player.append(a)
        time.sleep(1)
        print('\n     发给你的第%d张牌是：' % (i + 1), a)

        # 给庄家发两张牌
        b = poker.pop(0)
        dealer.append(b)
        time.sleep(1)
        if i == 0:
            print('     发给庄家一张明牌：', b)
        else:
            print('     发给庄家一张暗牌')

    # 判断玩家是否为BlackJack
    if 'A' in player:
        if points_poker[count(player)[0]] == 10:
            points_player = 'BlackJack'

    # 判断庄家是否为BlackJack
    if 'A' in dealer:
        if points_poker[count(dealer)[0]] == 10:
            points_dealer = 'BlackJack'

    time.sleep(1)
    print('\n     你的手牌为：', player)
    print('     庄家的明牌：', dealer[0])

    if points_player == 'BlackJack':
        time.sleep(2)
        print('     因为BlackJack是最大的牌了，直接进入结算阶段~')
        ending = 1

    # 判断是否需要保险金
    if ending == 0:
        if dealer[0] == 'A':
            time.sleep(1)
            print("\n     因为庄家的明牌为'A'，请问是否要下保险金？")
            print('     （保险金为赌注的一半，即%d个筹码）' % (bet//2))
            print('     （保险金不会退还，但是如果庄家是BlackJack，退还一半赌注）')

            while True:
                insurance = input('\n     请输入是或否：')
                if insurance == '是':
                    chip_player -= bet // 2
                    chip_dealer += bet // 2
                    show_chip(chip_player, chip_dealer)
                    time.sleep(1)
                    if points_dealer == 'BlackJack':
                        print('\n     庄家的牌是BlackJack')
                        ending = ending6
                    else:
                        print('     庄家的牌不是BlackJack，游戏继续')
                    break
                elif insurance == '否':
                    break
                else:
                    continue

    # 开始要牌阶段
    if ending == 0:
        time.sleep(2)
        print('\n【要牌阶段】')
        time.sleep(1)
        if points_player == 'BlackJack':
            print('     你现在的手牌是BlackJack，不需要要牌了')
        else:
            i = 0
            while i >= 0:
                time.sleep(1.5)
                hit = input('\n     （第%d轮要牌）\n     是否要牌？请输入是或否：' % (i + 1))
                if hit == '是':
                    a = poker.pop(0)
                    player.append(a)
                    time.sleep(1)
                    print('\n     第{}轮要牌：{}'.format((i + 1), a))
                    time.sleep(1)
                    print('\n     你的手牌为：', player)
                    print('     庄家的明牌：', dealer[0])
                    i += 1

                    if 'A' not in player:
                        for np in player:
                            count_player.append(points_poker[np])
                        if sum(count_player) > 21:
                            ending = ending1
                            time.sleep(1)
                            print('\n     你爆牌了！')
                            break
                        del count_player[:]     # 还原count_player,以便下次计算
                    else:
                        for np in count(player):
                            count_player.append(points_poker[np])
                        if (sum(count_player) + (player.count('A')) * 1) > 21:
                            time.sleep(1)
                            print('\n     你爆牌了！')
                            ending = ending1
                            break
                        del count_player[:]     # 还原count_player,以便下次计算
                elif hit == '否':
                    break
                else:
                    continue

        # 如果没有触发结局，庄家开始要牌环节
        if ending == 0:
            time.sleep(2)
            print('\n【庄家拿牌阶段】')
            print('（如果庄家的牌小于17点，则需要拿牌直到不小于17点）')
            time.sleep(1.5)
            print('\n     你的手牌为：', player)
            print('     庄家的牌为：', dealer)
            time.sleep(1)

            if points_player != 'BlackJack':
                # 计算玩家点数
                if 'A' not in player:
                    for np in player:
                        count_player.append(points_poker[np])
                    points_player = sum(count_player)
                else:
                    for np in count(player):
                        count_player.append(points_poker[np])
                    if (sum(count_player) + 11 + player.count('A') - 1) > 21:
                        points_player += sum(count_player) + player.count('A')
                    else:
                        points_player += sum(count_player) + 11 + player.count('A') - 1

            # 计算庄家目前点数，判断是否小于17需要拿牌
            if points_dealer != 'BlackJack':
                dealer17 = True     # 用于判断庄家是否需要拿牌到17点, 默认需要

                if 'A' not in dealer:
                    for nd in dealer:
                        count_dealer.append(points_poker[nd])       # 将庄家点数加入count_dealer
                        if sum(count_dealer) >= 17:
                            print('     庄家不需要拿牌')
                            dealer17 = False
                            points_dealer += sum(count_dealer)
                elif dealer[0] == 'A' and dealer[1] == 'A':
                    pass
                else:
                    if (count(dealer)[0] + 11) >= 17:
                        print('     庄家不需要拿牌')
                        dealer17 = False
                        count_dealer.extend([points_poker[count(dealer)[0]], 11])
                        points_dealer += sum(count_dealer)

                # 判断是否需要拿牌
                if dealer17:
                    del count_dealer[:]

                    if 'A' in dealer:
                        for nd in count(dealer):
                            count_dealer.append(points_poker[nd])
                    else:
                        for nd in dealer:
                            count_dealer.append(points_poker[nd])

                    while dealer17:
                        b = poker.pop(0)
                        dealer.append(b)
                        time.sleep(1)
                        print('\n     庄家需要持续拿牌直至点数不小于17')
                        time.sleep(1.5)
                        print('     庄家正在拿牌。。。')
                        time.sleep(2)
                        print('     庄家现在的手牌为：', dealer)
                        if 'A' in dealer:
                            if b == 'A':
                                if 17 <= (sum(count_dealer) + 11 + (dealer.count('A') - 1)) <= 21:
                                    points_dealer += sum(count_dealer) + 11 + (dealer.count('A') - 1)
                                    break
                                elif 17 <= (sum(count_dealer) + (dealer.count('A'))) <= 21:
                                    points_dealer += sum(count_dealer) + (dealer.count('A'))
                                    break
                                elif (sum(count_dealer) + 11 + (dealer.count('A') - 1)) < 17:
                                    continue
                                elif 10 < (sum(count_dealer) + dealer.count('A')) < 17:
                                    continue
                                else:
                                    print('\n     庄家爆牌了！')
                                    ending = ending3
                                    break
                            else:
                                count_dealer.append(points_poker[b])
                                if 17 <= (sum(count_dealer) + 11 + (dealer.count('A') - 1)) <= 21:
                                    points_dealer += sum(count_dealer) + 11 + (dealer.count('A') - 1)
                                    break
                                elif 17 <= (sum(count_dealer) + (dealer.count('A'))) <= 21:
                                    points_dealer += sum(count_dealer) + (dealer.count('A'))
                                    break
                                elif (sum(count_dealer) + 11 + (dealer.count('A') - 1)) < 17:
                                    continue
                                elif 10 < (sum(count_dealer) + dealer.count('A')) < 17:
                                    continue
                                else:
                                    print('\n     庄家爆牌了！')
                                    ending = ending3
                                    break
                        else:
                            count_dealer.append(points_poker[b])
                            if sum(count_dealer) < 17:
                                continue
                            elif sum(count_dealer) > 21:
                                print('\n     庄家爆牌了！')
                                ending = ending3
                                break
                            else:
                                points_dealer += sum(count_dealer)
                                break

    # 如果没有触发结局(没有人爆牌)，开始判断大小
    if ending == 1:
        if points_player == points_dealer == 'BlackJack':
            ending = ending5

        elif points_player == 'BlackJack' and points_dealer != 'BlackJack':
            ending = ending4

        elif points_player != 'BlackJack' and points_dealer == 'BlackJack':
            ending = ending2

    elif ending == 0:
        if points_player > points_dealer:
            ending = ending3

        elif points_player < points_dealer:
            ending = ending1

        else:
            ending = ending5

    # 最后结算筹码阶段
    time.sleep(2.5)
    print('\n【结算阶段】')
    time.sleep(2)
    print('\n     你的手牌为：', player)
    print('     庄家的牌为：', dealer)
    time.sleep(3)
    if ending == ending6:
        if points_player == 'BlackJack':
            print('\n     平局，退还赌注，失去保险金')
            show_chip(chip_player, chip_dealer)
        else:
            print('\n     你输了，但是你下了保险金，退还一半的赌注')
            show_chip(chip_player, chip_dealer)
    elif ending == ending1:
        print(ending1)
        chip_player -= bet
        chip_dealer += bet
        show_chip(chip_player, chip_dealer)
    elif ending == ending2:
        print(ending2)
        chip_player -= bet * 2
        chip_dealer += bet * 2
        show_chip(chip_player, chip_dealer)
    elif ending == ending3:
        print(ending3)
        chip_player += bet
        chip_dealer -= bet
        show_chip(chip_player, chip_dealer)
    elif ending == ending4:
        print(ending4)
        chip_player += bet * 2
        chip_dealer -= bet * 2
        show_chip(chip_player, chip_dealer)
    elif ending == ending5:
        print(ending5)
        show_chip(chip_player, chip_dealer)
    else:
        print('\n     你和庄家都是BlackJack，平局')
        show_chip(chip_player, chip_dealer)

    time.sleep(2)
    if chip_player > 0 and chip_dealer > 0:
        while True:
            new_game = input('\n是否开始第%d局？\n请输入是或否：' % (game + 1))
            if new_game == '是':
                game += 1
                break
            if new_game == '否':
                game = 0
                break
            else:
                continue
    elif chip_player == 0:
        if game == 1:
            print('\n你一局就输光了所有的筹码...')
            time.sleep(1)
            print('这下你这个月只能吃土了...')
            time.sleep(1)
            print('“珍爱生命，远离赌博”\n【GAMEOVER】\n感谢游玩~')
        elif game <= 3:
            print('\n你在三局内就输光了所有的筹码...')
            time.sleep(1)
            print('这下你这个月只能吃土了...')
            time.sleep(1)
            print('下次请理性下注\n【GAMEOVER】\n感谢游玩~')
        else:
            print('\n你输光了所有的筹码...')
            time.sleep(1)
            print('这下你这个月只能吃土了\n【GAMEOVER】\n感谢游玩~')
        game = 0
    elif chip_player < 0:
        if game == 1:
            print('\n你一局就输光了所有的筹码，还要在赌场洗半个月的碗')
            time.sleep(1)
            print('但是赌场包吃包住，这个月不用吃土了，并且你成为了一名优秀的刷碗工')
            time.sleep(1)
            print('“珍爱生命，远离赌博”\n【GAMEOVER】\n感谢游玩~')
        elif game <= 3:
            print('\n你在三局内就输光了所有的筹码，还要在赌场洗半个月的碗')
            time.sleep(1)
            print('但是赌场包吃包住，这个月不用吃土了，并且你成为了一名优秀的刷碗工')
            time.sleep(1)
            print('下次请理性下注\n【GAMEOVER】\n感谢游玩~')
        else:
            print('\n你输光了所有的筹码，还要在赌场洗半个月的碗')
            time.sleep(1)
            print('但是赌场包吃包住，这个月不用吃土了，并且你成为了一名优秀的刷碗工\n【GAMEOVER】\n感谢游玩~')

        game = 0
    elif chip_dealer == 0:
        if game == 1:
            print('\n你一局就赢得了庄家所有的筹码！')
            time.sleep(1)
            print('你可真是个大赌徒！\n感谢游玩~')
        elif game <= 3:
            print('\n你在三局内就赢得了庄家所有的筹码！')
            time.sleep(1)
            print('你的运气不错哦！\n感谢游玩~')
        else:
            print('\n你赢得了庄家所有的筹码！\n感谢游玩~')
        game = 0
    else:
        if game == 1:
            print('\n你一局就赢得了庄家所有的筹码，外加身上所有衣物！')
            time.sleep(1)
            print('你可真是个大赌徒！\n感谢游玩~')
        elif game <= 3:
            print('\n你在三局内就赢得了庄家所有的筹码，外加身上所有衣物！')
            time.sleep(1)
            print('你的运气不错哦！\n感谢游玩~')
        else:
            print('\n你赢得了庄家所有的筹码，外加身上所有衣物！\n感谢游玩~')
        game = 0

    if game == 0:
        time.sleep(5)

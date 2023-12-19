import time
import random

def distribute(card_lst): # 카드분배
    global card_list, card_entire
    card = random.sample(card_entire, 1)
    for number in card:
        card_entire.remove(number)
    card_lst.append(card)

def distribute_small(card_lst):
    global card_list, card_entire
    card = random.sample(card_entire, 1)
    for number in card:
        card_entire.remove(number)
    card_lst.append(card)
    return card


def find_A(chat, i):
    global bring_A
    if 'A' in chat:
        bring_A[int(i/2)] += 1

def check_point(card, j):
    global all_point, temp_lst
    card_1 = card[0]
    for i in range(0, 14):
        if lst_point[i] in card_1:
            all_point[j] += card_point[i]
            temp_lst[j].append(lst_point[i])

def decision(x):
    global all_point
    if bring_A[x] == 2:
        print(f'{character[x]}가 A 하나를 1로 A 하나를 11로 지정하였습니다')
        all_point[x] += 12
    elif bring_A[x] == 1:
        if all_point[x] <=5:
            print(f'{character[x]}가 A를 1로 지정하였습니다')
            all_point[x] += 1
        elif all_point[x] <=10:
            print(f'{character[x]}가 A를 11로 지정하였습니다')
            all_point[x] += 11
        else:
            print(f'{character[x]}가 A를 1로 지정하였습니다')
            all_point[x] += 1

def dicision_small(x):
    global all_point
    if all_point[x] <=5:
        print(f'{character[x]}가 A를 1로 지정하였습니다')
        all_point[x] += 1
    elif all_point[x] <=10:
        print(f'{character[x]}가 A를 11로 지정하였습니다')
        all_point[x] += 11
    else:
        print(f'{character[x]}가 A를 1로 지정하였습니다')
        all_point[x] += 1


def random_boolean(probability):
    return random.random() < probability

character = ['딜러', 'ai1', 'ai2', 'person']
card_list = [[],[],[],[]] # 딜러, ai1, ai2, person
card_entire = ['♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♠A',
'♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K','♣A', '♥2', '♥3', 
'♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A', '◆2', '◆3', 
'◆4', '◆5', '◆6', '◆7', '◆8', '◆9', '◆10', '◆J', '◆Q', '◆K', '◆A']
lst_point = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'Q', 'J', 'K', ' ']
card_point = [10, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 10, 10]
bring_A = [0, 0, 0, 0]
all_point = [0, 0, 0, 0]
taken_coin = [100, 100, 100, 100]
pay_coin = [0, 0, 0, 0]
a = -1
# 배팅
while 1:
    card_list = [[],[],[],[]] # 딜러, ai1, ai2, person
    card_entire = ['♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♠A',
    '♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K','♣A', '♥2', '♥3', 
    '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A', '◆2', '◆3', 
    '◆4', '◆5', '◆6', '◆7', '◆8', '◆9', '◆10', '◆J', '◆Q', '◆K', '◆A']
    lst_point = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'Q', 'J', 'K', ' ']
    card_point = [10, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 10, 10]
    bring_A = [0, 0, 0, 0]
    all_point = [0, 0, 0, 0]
    temp_lst = [[], [], [], []]
    a = -1
    print('지금부터 카드를 나누기 전에 배팅을 하겠습니다')
    for i in range(1, 3):
        random_number = random.randint(1, 10)
        random_number *= 0.1
        coin = taken_coin[i] * random_number
        coin = int(coin)
        print(f'{character[i]} : {coin}')
        taken_coin[i] = taken_coin[i] - coin
        pay_coin[i] = coin
        time.sleep(3)

    coin = int(input(f'얼마를 배팅하시겠습니끼?최대({taken_coin[3]}) : '))
    while coin > taken_coin[3]:
        print('가지고 있는 코인의 최대를 초과하였습니다')
        coin = int(input(f'얼마를 배팅하시겠습니끼?최대({taken_coin[3]}) : '))
    taken_coin[3] -= coin
    pay_coin[3] = coin

    print(f'{character[1]} 배팅금 {pay_coin[1]}')
    print(f'{character[2]} 배팅금 {pay_coin[2]}')
    print(f'{character[3]} 배팅금 {pay_coin[3]}')
    print(' ')


    # 1번째 카드 배분
    print('1번째 카드를 나누는 중.')
    time.sleep(1)
    print('1번째 카드를 나누는 중..')
    time.sleep(1)
    print('1번째 카드를 나누는 중...')
    time.sleep(1)
    for player_cards in card_list:
        distribute(player_cards)

    print('첫번째 카드 전달 완료')
    for i in range(4):
        print(f'{character[i]} : {card_list[i]}')
    print(' ')
    time.sleep(10)

    # 2번째 카드 배분
    print('2번째 카드를 나누는 중.')
    time.sleep(1)
    print('2번째 카드를 나누는 중..')
    time.sleep(1)
    print('2번째 카드를 나누는 중...')
    time.sleep(1)
    for player_cards in card_list:
        distribute(player_cards)

    print(f'딜러 : {card_list[0][0]}')
    print(f'ai1 : {card_list[1]}')
    print(f'ai2 : {card_list[2]}')
    print(f'person : {card_list[3]}')

    time.sleep(10)

    # A가 있으면 몇 개 있는지 확인
    for i in card_list[0:4]:
        for j in i:
            a += 1
            charter = j[0]
            find_A(charter, a)

    # 카드 점수화
    for i in range(0, 3):
        for j in range(0, 2):
            check_point(card_list[i][j], i)
    

    # 같은 숫자일 경우 1을 추가
    if temp_lst[1][0] == temp_lst[1][1]:
        all_point[1] += 1
    if temp_lst[2][0] == temp_lst[2][1]:
        all_point[2] += 1



    # A를 1 아니면 11로 무엇을 할지 결정
    for i in range(1, 3):
        if bring_A[i] > 0:
            decision(i)

    # 사용자 점수화
    for i in range(2):
        check_point(card_list[3][i], 3)

    if temp_lst[3][0] == temp_lst[3][1]:
        all_point[3] += 1
    
    # 사용자 A 카드 소지 점수화
    if bring_A[3] > 0:
        print(f'당신이 가지고 있는 카드는 {card_list[3][0]}, {card_list[3][1]}입니다')
        for i in range(0, bring_A[3]):
            num = int(input('A카드 하나를 1과 11중에 무엇으로 지정하시겠습니까(1 / 11): '))
            while num!=1 and num!=11:
                print('입력이 잘못되었습니다(1 / 11): ')
                num = int(input('A카드 하나를 1과 11중에 무엇으로 지정하시겠습니까(1 / 11): '))
            all_point[3] += num
    
    # 블랙잭일 경우
    if 21 in all_point:
        lst = []
        for i in range(4):
            if all_point[i] == 21:
                lst.append(i)
        if len(lst)==1:
            print(f'{character[lst[0]]}이 블랙잭으로 승리하였습니다')
            taken_coin[lst[0]] += pay_coin[lst[0]] * 2
            pay_coin = [0, 0, 0, 0]
        elif len(lst)>1:
            print('무승부입니다')
            for i in win:
                taken_coin[i] += pay_coin[i]
            pay_coin = [0, 0, 0, 0]
    else:
        # 카드 받기
        for i in range(1, 3):
            while 1:
                print(f'{character[i]}님 카드를 받으시겠습니까?')
                time.sleep(1)
                point = (21 - all_point[i]) * 0.1
                custom_probability = point
                result = random_boolean(custom_probability)
                if result == True:
                    print(f'{character[i]} : 네')
                    card = distribute_small(card_list[i])
                    print(f'{character[i]}님이 뽑으신 카드는 {card}입니다.')
                    if 'A' in card:
                        dicision_small(i)
                    else:
                        check_point(card, i)
                else:
                    print(f'{character[i]} : 아니요')
                    break

        #카드 ai1, ai2상황 보여주기
        print(f'{character[0]} : {card_list[0][0]}', end=' ')
        for i in range(1, 3):
            print(' ')
            print(f'{character[i]} : {card_list[i][0]}', end=' ')
            for j in card_list[i][1:]:
                print(f', {j}', end=' ')
        print(' ')

        # 플레이어 카드 받기
        print(' ')
        print(f'플레이어의 현재 카드는 {card_list[3]}입니다')
        n = input('카드를 추가로 받으시겠습니까(Y/N) : ')
        while n=='Y':   
            card = distribute_small(card_list[3])
            if 'A' in card[0]:
                num = int(input(f'뽑으신 카드는 {card}입니다. 1과 11 중 무엇을 하시겠습니까?(1 / 11) : '))
                while num!=1 and num!=11:
                    print('입력이 잘못되었습니다(1 / 11): ')
                    num = int(input(f'뽑으신 카드는 {card}입니다. 1과 11 중 무엇을 하시겠습니까?(1 / 11) : '))
                all_point[3] += num
            else:
                check_point(card, 3)
            if all_point[3] > 21:
                break
            print(f'플레이어의 현재 카드는 {card_list[3]}입니다')
            n = input('카드를 추가로 받으시겠습니까(Y/N) : ')

        print(f'{character[0]} : {card_list[0][0]}')
        for i in range(1, 4):
            print(f'{character[i]} : {card_list[i][0]}', end=' ')
            for j in card_list[i][1:]:
                print(f', {j}', end=' ')
            print(' ')

        # 딜러 카드 뽑기
        if temp_lst[0][0] == temp_lst[0][1]:
            all_point[0] += 1
        if bring_A[0] > 0:
            decision(0)
        while all_point[0] <= 16:
            card = distribute_small(card_list[0])
            if 'A' in card:
                dicision_small(0)
            else:
                check_point(card, 0)
            print('딜러가 카드를 가져갑니다')

        time.sleep(2)
        for i in range(0, 4):
            print(f'{character[i]} : {card_list[i][0]}', end=' ')
            for j in card_list[i][1:]:
                print(f', {j}', end=' ')
            print(' ')
        print(' ')

        # 판정 (승리자)
        # 21 승리
        win = []
        if all_point[0]==21:
            print('딜러가 승리하였습니다')
        elif 21 in all_point:
            for i in range(1, 3):
                if all_point[i]==21:
                    win.append(i)
            if len(win)==1:
                print(f'승리자는 {character[win[0]]}입니다')
                taken_coin[win[0]] += pay_coin[win[0]] * 2
                pay_coin = [0, 0, 0, 0]
            if len(win)>1:
                print('무승부입니다')
                for i in win:
                    taken_coin[i] += pay_coin[i]
                pay_coin = [0, 0, 0, 0]

        # 21에 가까운 승리
        else:
            max_num, wichi = 0, -1
            for i in range(4):
                if all_point[i] < 22 and all_point[i] > max_num:
                    max_num = all_point[i]
                    wichi = i
            win.append(wichi)

            for i in range(4):
                if wichi!=i and max_num==all_point[i]:
                    win.append(i)

            if len(win)>1:
                print('무승부입니다')
                for i in win:
                    taken_coin[i] += pay_coin[i]
                pay_coin = [0, 0, 0, 0]
            else:
                print(f'승리자는 {character[win[0]]}입니다')
                taken_coin[win[0]] += pay_coin[win[0]] * 2
                pay_coin = [0, 0, 0, 0]

    print(taken_coin)
    x = input('다시 하시겠습니까?(Y / N) : ')
    while x!='Y' and x!='N':
        print('입력을 잘못하였습니다')
        x = input('다시 하시겠습니까?(Y / N) : ')
    if x=='N':
        break

print('The End')
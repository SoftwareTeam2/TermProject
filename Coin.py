money = int(input('입력 금액 : '))
one = 0
two = 0
thr = 0
four = 0
while True:
    if money >= 500:
        money -= 500
        one += 1
    elif money >= 100:
        money -= 100
        two += 1
    elif money >= 50:
        money -= 50
        thr += 1
    elif money >= 10:
        money -= 10
        four += 1
    elif money == 00:
        print('500 : ', one, '개')
        print('100 : ', two, '개')
        print('50 : ', thr, '개')
        print('10 : ', four, '개')
        break
    else:
        print('입력 오류')
        break
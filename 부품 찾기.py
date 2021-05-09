n = int(input())
partList = list(map(int,input().split()))
m = int(input())
orderList = list(map(int,input().split()))

for i in orderList:
    if i in partList:
        print('yes',end=' ')
    else:
        print('no',end=' ')
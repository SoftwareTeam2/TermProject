money = int(input())
change=0
coins=[500,100,50,10]
for coin in coins:
    change+=money//coin
    money=money%coin
print(change)
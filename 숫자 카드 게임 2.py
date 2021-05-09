n, m = map(int,input().split())
cards=[]
for i in range(n):
    cards.append(list(map(int,input().split())))
maxValue = 0
for i in range(n):
    minValue=min(cards[i])
    if maxValue<minValue:
        maxValue=minValue
print(maxValue)
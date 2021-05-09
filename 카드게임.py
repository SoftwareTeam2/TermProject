import numpy as np
n,m = map(int, input().split())
numList = list(map(int, input().split()))
cards = np.reshape(np.array(numList), (n,m))

c_max = 0

for i in range(len(cards)):
    c_min=cards[i,0]
    for num in cards[i,:]:
        if(c_min>num):
            c_min=num
    if(c_max<c_min):
        c_max=c_min

print(c_max)

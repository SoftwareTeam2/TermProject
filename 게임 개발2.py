import sys
from numpy import array
input=sys.stdin.readline
n, m =map(int,input().split())
a, b, d = map(int,input().split())
Pos = array([a,b])
dungeonMap=[]
for i in range(n):
    dungeonMap.append(list(map(int,input().split())))
dungeonMap=array(dungeonMap)
def turn():
    global d
    count=0
    while dungeonMap[(Pos+goahead.get(d))[0],(Pos+goahead.get(d))[1]] != 0:
        d-=1
        count+=1
        if d<0:
            d=3
        if count==4:
            return False
    return True
allClear=True
goahead = {0:array([-1,0]),1:array([0,1]),2:array([1,0]),3:array([0,-1])}
fallback = {0:array([1,0]),1:array([0,-1]),2:array([-1,0]),3:array([0,1])}
conquer = 0
while allClear:
    if turn():
        dungeonMap[Pos]=1
        conquer +=1
        Pos=Pos+goahead.get(d)        
        print(Pos)
    else:
        if dungeonMap[(Pos+fallback.get(d))[0],(Pos+fallback.get(d))[1]] != 1:
            Pos+=fallback.get(d)
        else:
            allClear=False
print(conquer+1)
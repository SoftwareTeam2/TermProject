import numpy as np

mapRow, mapCol = map(int, input('맵 사이즈 : ').split())
charLoc = np.array(list(map(int, input('캐릭터 위치 : ').split())))
moves = {0:np.array([-1,0]),1:np.array([0,1]),2:np.array([1,0]),3:np.array([0,-1])}
mapConfig = np.ones((mapRow,mapCol))
moveCount=0
isMovable = True

def charView() :
    global charLoc
    charLoc -= np.array([0,0,1])
    if charLoc[2] < 0 :
        charLoc += np.array([0,0,4])

def setCharLoc():
    charView()
    pos = moves.get(charLoc[2])
    global xPos, yPos
    xPos = pos[0]
    yPos = pos[1]

for i in range(mapRow):
    oneLine = np.array(list(map(int, input().split())))
    mapConfig[i] *= oneLine

charView()
pos = moves.get(charLoc[2])
xPos = pos[0]
yPos = pos[1]

while isMovable:
    failCount=0
    while mapConfig[charLoc[0]+xPos,charLoc[1]+yPos]!=0:
        setCharLoc()
        failCount+=1
        if failCount==4:
            isMovable=False
            break
    if isMovable:
        mapConfig[charLoc[0],charLoc[1]]=1
        charLoc[0]+=xPos
        charLoc[1]+=yPos
        setCharLoc()
        moveCount+=1
moveCount+=1
print(moveCount)

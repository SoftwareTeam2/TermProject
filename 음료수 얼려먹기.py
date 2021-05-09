import numpy as np

row, column = map(int,input().split())
iceMold = []
ice = 0
for i in range(row):
    iceMold.append(list(map(int,input())))
visited = np.full((row,column),False)

def fillMold(xpos,ypos):
    if (xpos>=0 and xpos<=row-1) and (ypos>=0 and ypos<=column-1):
        if iceMold[xpos][ypos]==0 and visited[xpos][ypos]==False:
            visited[xpos,ypos]=True
        fillMold(xpos+1,ypos)
        fillMold(xpos,ypos+1)

def icecream(xpos, ypos):
    if (xpos>=0 and xpos<=row-1) and (ypos>=0 and ypos<=column-1):
        if visited[xpos][ypos]==True:
            visited[xpos][ypos]=False
            icecream(xpos+1,ypos)
            icecream(xpos-1,ypos)
            icecream(xpos,ypos-1)
            icecream(xpos,ypos+1)
            return True
        else:                                                                                                         
            return False

fillMold(0,0)
for i in range(row):
    for j in range(column):
        if icecream(i,j):
            ice+=1
print(ice)
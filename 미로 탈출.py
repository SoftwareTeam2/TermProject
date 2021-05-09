from collections import deque
n, m = map(int,input().split())
dungeon = []

for i in range(n):
    dungeon.append(list(map(int,input())))

xpos = 0
ypos=0
count=0
while xpos!=n-1 or ypos!=m-1:
    print(xpos,ypos)
    if xpos<n-1 and dungeon[xpos+1][ypos]==1:
        xpos+=1
        count+=1
    elif ypos<m-1 and dungeon[xpos][ypos+1]==1:
        ypos+=1
        count+=1
    elif ypos>0 and dungeon[xpos][ypos-1]==1:
        ypos-=1
        count+=1
    else:
        dungeon[xpos][ypos]=0
        count-=1
        xpos-=1
count+=1
print(count)
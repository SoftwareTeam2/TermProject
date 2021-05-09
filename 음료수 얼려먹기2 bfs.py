from collections import deque
n, m = map(int,input().split())
iceMold = []
for i in range(n):
    iceMold.append(list(input()))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(xpos,ypos):
    result=0
    queue = deque()
    queue.append((xpos,ypos))
    while queue:
        x,y = queue.popleft()
        if iceMold[x][y]=='0':
            iceMold[x][y]='1'
        count=0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                count+=1
            elif iceMold[nx][ny]=='1':
                count+=1
            if  not(nx<0 or ny<0 or nx>=n or ny>=m) and (nx,ny) not in queue:
                queue.append((nx,ny))
            if count==4:
                result+=1
    return result
print(bfs(0,0))

     
n,m = map(int,input().split())
iceMold = []
for i in range(n):
    iceMold.append(list(input()))
def dfs(xpos, ypos):
    if (xpos<0 or xpos>=n) or (ypos<0 or ypos>=m):
        return False
    if iceMold[xpos][ypos]=='0':
        iceMold[xpos][ypos]='1'
        dfs(xpos-1,ypos)
        dfs(xpos+1,ypos)
        dfs(xpos,ypos-1)
        dfs(xpos,ypos+1)
        return True
    else:
        return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1 
print(result)
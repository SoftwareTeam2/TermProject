import sys
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

def findTeam(parent, a):
    if parent[a]!=a:
        parent[a]=findTeam(parent,parent[a])
    return parent[a]

def unionTeam(a, b):
    a= findTeam(parent,a)
    parent[b]=a
    
for i in range(m):
    o, a, b = map(int,input().split())
    if o==0:
        unionTeam(a,b)
    elif o==1:
        if findTeam(parent,a) == findTeam(parent,b):
            print('yes')
        else:
            print('no')
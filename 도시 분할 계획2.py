import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cityMap=[]
parent=[0]*(n+1)
for i in range(m):
    a,b,c = map(int,input().split())
    cityMap.append((c,a,b))

for i in range(1,n+1):
    parent[i]=i

def findParent(parent,a):
    if parent[a]!=a:
        parent[a]=findParent(parent,parent[a])
    return parent[a]

def unionParent(parent,a,b):
    a=findParent(parent,a)
    b=findParent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

cityMap.sort()

maxCost = 0
result = 0
for road in cityMap:
    cost, source, dest = road
    if findParent(parent,source) != findParent(parent,dest):
        if maxCost<cost:
            maxCost=cost
        unionParent(parent,source,dest)
        result+=cost
print(result-maxCost)

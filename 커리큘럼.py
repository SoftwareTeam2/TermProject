import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[[]]
costs=[0]*(n+1)

for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(1,n+1):
    costs[i]+=graph[i][0]
for i in range(1,n+1):
    for j in range(1,len(graph[i])):
        if graph[i][j]==-1:
            continue
        costs[i]+=costs[graph[i][j]]
for i in range(1,n+1):
    print(costs[i])

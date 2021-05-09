"""      플로이드 워셜 알고리즘
import sys
from numpy import array
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())

distance = [[INF]*(n+1)for i in range(n+1)]
for i in range(m):
    source, dest = map(int,input().split())
    distance[source][dest]=1
    distance[dest][source]=1
x, k = map(int, input().split())

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            distance[a][b]=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            distance[j][k] = min(distance[j][k], distance[j][i]+distance[i][k])
print(distance[1][k]+distance[k][x])
"""
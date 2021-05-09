import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int,input().split())
graph=[[]for i in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(start,0))
    distance[start]=0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for dest in graph[now]:
            cost = dist+dest[1]
            if cost<distance[dest[0]]:
                distance[dest[0]]=cost
                heapq.heappush(q,(dest[0],cost))
dijkstra(c)

def notINF(x):
    return x!=INF

distance=list(filter(notINF,distance))
print(len(distance)-1,max(distance))


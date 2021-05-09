from collections import deque
INF = int(1e9)
n,m,k,x = map(int,input().split())
graph= [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
q=deque([x])
distance[x] = 0
while q:
    curr = q.popleft()
    for next_node in graph[curr]:
        if distance[next_node] == INF:
            distance[next_node] = distance[curr]+1
            q.append(next_node)
check = False
for i in range(1,len(distance)):
    if distance[i] == k:
        print(i)
        check=True
if check == False:
    print(-1)
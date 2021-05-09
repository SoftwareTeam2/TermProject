import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())
indegree = [0]*(n+1)
costs=[[]]
followCourse = [[] for i in range(n+1)]

for i in range(1,n+1):
    course = list(map(int,input().split()))
    costs.append(course[0])
    indegree[i] = len(course[1:-1])
    for precourse in course[1:-1]:
        followCourse[precourse].append(i)

def topologySort():
    q=deque()
    minTime = copy.deepcopy(costs)
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in followCourse[now]:
            minTime[i] = max(minTime[i],minTime[now]+costs[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    print(minTime[1:])
topologySort()
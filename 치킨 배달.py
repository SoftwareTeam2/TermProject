import sys
from itertools import combinations
input = sys.stdin.readline

chickenLoc = []
houseLoc = []
n, m = map(int,input().split())

for i in range(n):
    avenue = list(map(int,input().split()))
    for j in range(n):
        if avenue[j]==2:
            chickenLoc.append((i,j))
        elif avenue[j]==1:
            houseLoc.append((i,j))

availableComb = []
for i in range(1,m+1):
    availableComb.append(list(combinations(chickenLoc,i)))

distance = [[0 for _ in range(len(chickenLoc))] for _ in range(len(houseLoc))]
for i in range(len(houseLoc)):
    for j in range(len(chickenLoc)):
        distance[i][j] = abs(chickenLoc[j][0]-houseLoc[i][0])+abs(chickenLoc[j][1]-houseLoc[i][1])

sumOfDistance = int(1e9)
for comb in availableComb:
    for each in comb:
        sumOfStoreDistance = 0
        for i in range(len(houseLoc)):
            mindis = int(1e8)
            for store in each:
                index = chickenLoc.index(store)
                mindis = min(mindis,distance[i][index])
            sumOfStoreDistance += mindis
        sumOfDistance = min(sumOfDistance,sumOfStoreDistance)
print(sumOfDistance)


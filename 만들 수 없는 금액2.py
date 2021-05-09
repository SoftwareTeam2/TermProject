import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
coins = list(map(int,input().split()))

sums = []
for i in range(len(coins)+1):
    temp = list(combinations(coins,i))
    for i in range(len(temp)):
        temp[i] = sum(temp[i])
    for item in temp:
        sums.append(item)

sums = set(sums)

for i in range(1,max(sums)+1):
    if i not in sums:
        print(i)
        break
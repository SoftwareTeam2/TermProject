import sys
from numpy import array
input = sys.stdin.readline
n = int(input())
command = list(map(str, input().split()))
standard = {'R': array([0, 1]), 'L': array(
    [0, -1]), 'U': array([-1, 0]), 'D': array([1, 0])}
initialPosition = array([0, 0])
for move in command:
    nextMove = standard.get(move)
    if initialPosition[0]+nextMove[0]>=0 and initialPosition[0]+nextMove[0]<n and initialPosition[1]+nextMove[1]>=0 and initialPosition[1]+nextMove[1]<n:
        initialPosition+=standard.get(move)
initialPosition+=array([1,1])
print(initialPosition[0],initialPosition[1])

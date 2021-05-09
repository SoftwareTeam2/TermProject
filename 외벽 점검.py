import sys
input = sys.stdin.readline
import numpy as np

def solution(n, weak, dist):
    fromZero = []
    for i in range(1,len(weak)):
        fromZero.append(weak[i]-weak[i-1])
    fromZero.append(weak[0]+n - weak[len(weak)-1])

    for i in range(len(fromZero)):
        index = i
        sumOfDistance = 0
        for _ in range(len(fromZero)-1):
            sumOfDistance += fromZero[index]
            index+=1
            if index == len(fromZero):
                index=0
        if sumOfDistance in dist:
            return 1
        else:
            return -1

    for i in range(len(dist)):
        group = []
        sum1 = 0
        for j in range(i,i+2):
            sum1+=fromZero[j]
        index = i+2
        for _ in range(i):
            print(i)

    
print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
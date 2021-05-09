import sys
from collections import deque
import numpy as np
input = sys.stdin.readline

n = int(input())
snakeMap = [[0 for col in range(n)] for row in range(n)]
snakeMap[0][0] = 1
k = int(input())
apples = deque()
for i in range(k):
    appleX, appleY = map(int, input().split())
    apple = [appleX-1, appleY-1]
    apples.append(apple)

l = int(input())
dirCommands = deque()
for i in range(l):
    dirCommands.append(tuple(map(str, input().split())))


def turnSnakeView(currentView, snakeView, nextDir):
    if nextDir == 'L':
        if currentView == 0:
            return 3
        else:
            return currentView-1
    else:
        if currentView == 3:
            return 0
        else:
            return currentView+1


def snakeGame(snakeMap, apples, dirCommands):
    gameValid = True
    ateApple = True
    currentTail = [0, 0]
    currentHead = [0, 0]
    nextQuarter, nextDir = dirCommands.popleft()
    nextApple = apples.popleft()
    currentView = 1
    tailView = currentView
    snakeView = {0: [-1, 0], 1: [0, 1],
                 2: [1, 0], 3: [0, -1]}
    dirQue = deque()
    timer = 0
    while gameValid:
        turn = False
        if timer == int(nextQuarter):
            turn = True
        if turn:
            if currentView == 0 or currentView==1:
                while snakeMap[currentHead[0]-((snakeView.get(currentView)))[0]][currentHead[1]] != 0:
                    dirQue.append(currentView)
            else:
                while snakeMap[currentHead[0]][currentHead[0]-((snakeView.get(currentView)))[0]] != 0:
                    dirQue.append(currentView)
            currentView = turnSnakeView(currentView, snakeView, nextDir)
            if dirCommands:
                nextQuarter, nextDir = dirCommands.popleft()
        currentHead[0] += (snakeView.get(currentView))[0]
        currentHead[1] += (snakeView.get(currentView))[1]
        if currentHead[0] < 0 or currentHead[0] >= n or currentHead[1] < 0 or currentHead[1] >= n or snakeMap[currentHead[0]][currentHead[1]] == 1:
            timer += 1
            break
        snakeMap[currentHead[0]][currentHead[1]] = 1
        if currentHead[0] == nextApple[0] and currentHead[1] == nextApple[1]:
            print('yes')
            if apples:
                nextApple = apples.popleft()
            ateApple = True
        else:
            ateApple = False
        timer += 1
        if not ateApple:
            snakeMap[currentTail[0]][currentTail[1]] = 0
            if snakeView.get(currentView) != snakeView.get(tailView) and dirQue:
                direction = dirQue.popleft()
                print(direction)
                currentTail[0] += snakeView.get(direction)[0]
                currentTail[1] += snakeView.get(direction)[1]
            elif not dirQue:
                tailView = currentView
                currentTail[0] += (snakeView.get(currentView))[0]
                currentTail[1] += (snakeView.get(currentView))[1]
        print(timer)
        print(currentTail)
        print(currentHead)
        print(ateApple)
        print(np.array(snakeMap))
    return timer


print(snakeGame(snakeMap, apples, dirCommands))

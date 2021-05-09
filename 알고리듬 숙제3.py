import sys
def addOneTwoThree(n):
    dp = [0 for _ in range(n+1)] # 부분 문제의 결과를 저장할 리스트
    dp[1]=1; dp[2]=2; dp[3]=4 # base case인 1,2,3에 대한 초기화
    for i in range(4,n+1):
        # 4부터 n까지 i에 해당 하는 경우의 수를 계산
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3] 
    return dp[n]

#print(addOneTwoThree(int(input())))

"""
def eatingCheese(n,cheeseLoc):
    dp=[[0 for _ in range(n+1)] for _ in range(n+1)] # 2차원 dp 리스트 초기화
    # 치즈가 존재하는 곳은 값을 1로 바꿔줌.
    for crd in cheeseLoc:
        dp[n+1-crd[1]][crd[0]] = 1
    # 각 칸을 돌며 현재 칸에서 먹을 수 있는 치즈의 최댓값을 구함
    for i in range(n,0,-1):
        for j in range(1,n+1):
            if i==n and j==1: #시작지점은 넘김
                continue
            elif i==n: # 현재 위치가 마지막 행일 경우
                if dp[i][j] == 1: # 현재 칸에 치즈가 있으면 왼쪽 칸 + 1
                    dp[i][j] = dp[i][j-1]+1
                else: # 현재 칸에 치즈가 없으면 왼쪽 칸의 값을 저장
                    dp[i][j] = dp[i][j-1]
            elif j==1: # 현재 위치가 첫번째 열일 경우
                if dp[i][j] == 1: # 현재 칸에 치즈가 있으면 밑의 칸 + 1
                    dp[i][j] = dp[i+1][j]+1
                else: # 현재 칸에 치즈가 없으면 밑의 칸의 값을 저장
                    dp[i][j] = dp[i+1][j]
            else:
                if dp[i][j] == 1: # 현재 칸에 치즈가 있다면 왼쪽 아래 칸 중 최댓값 + 1
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])+1
                else: # 치즈가 없다면 왼쪽 아래 중 최댓값을 저장
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])    
    return dp[1][n]

n, m = map(int,input().split())
cheeseLoc = [tuple(map(int, input().split())) for _ in range(m)]
print(eatingCheese(n,cheeseLoc))
"""

"""
def coinMaker(k,coins):
    dp = [0 for _ in range(k+1)] # 1원부터 k원까지 동전의 개수를 저장할 리스트
    # k보다 작은 base case들을 1로 초기화
    for coin in coins:
        if coin>k:
            break
        dp[coin] = 1
    """"""
    for문의 i 보다 큰 다음 coin값의 인덱스, 만약 i가 73이면
    이보다 큰 coin은 91이므로 coinIndex에는 6이 저장된다.
    """"""
    coinIndex = 0
    # for문을 돌며 i원의 가정 적은 개수의 동전을 계산
    for i in range(1,k+1):
        # i와 coins[coinIndex]를 비교하고 필요하다면 coinIndex 값을 갱신
        if i > coins[coinIndex]:
            coinIndex+=1
        # 아직 i번째 dp 테이블이 계산되지 않았다면
        if dp[i]==0:
            """"""
            i원은 i원과 i원보다 작은 단위 화폐들 즉, coins의 원소 중 i 보다 작은 동전들의
            차이 + 1개로 이루어질 수 있음. 그리고 이 중 최솟값 + 1이 dp[i]에 채워짐
            만약 i가 73이면 73원은 73-1, 73-4, 73-7, 73-13, 73-28, 73-52 중 최솟값에 1을 더한 값임
            """"""
            dp[i] = min([dp[i-coin] for coin in coins[:coinIndex]])+1
    return dp[k]

coins = [1,4,7,13,28,52,91,365]
print(coinMaker(int(input())))
"""

"""
def maxConsecutiveSum(inputAry):
    maxRange = [0,0,0,0] # 이전 부분 문제의 결과를 저장할 리스트 
    # 0~n-1까지 루프를 돌며 계산 진행
    for i in range(len(inputAry)):
        curr = inputAry[i]+maxRange[0] # 현재 인덱스의 값을 넣는다고 가정한 값
        # 3번 조건에 해당
        if curr > maxRange[1] and maxRange[0] < 0:
            maxRange = [inputAry[i],inputAry[i],i,i]
        # 1번 조건에 해당
        elif curr >= maxRange[1]:
            maxRange[0] += inputAry[i]
            maxRange[1] = maxRange[0]
            maxRange[3] = i
        # 2번 조건에 해당
        elif curr < maxRange[1]:
            maxRange[0] += inputAry[i]
    return maxRange[2:]

print(maxConsecutiveSum([31,-41,59,26,-53,58,97,-93,-23,84]))
"""
inputAry= [-8,5]

def recMaxConsecutiveMul(i):
    if i==0 and inputAry[0] < 0:
        return [-inputAry[0],1,1]
    elif i==0 and inputAry[0] > 0:
        return [inputAry[0],0,1]
    elif i==0 and inputAry[0] == 0:
        return [1,0,1]
    returnList = recMaxConsecutiveMul(i-1)
    if inputAry[i]<0:
        returnList[1]+=1
    if returnList[1]%2==0 and abs(returnList[0]*inputAry[i])>returnList[2]:
        returnList[2] = abs(returnList[0]*inputAry[i])
        returnList[0] = returnList[2]
        return returnList
    elif inputAry[i] > 0:
        return [returnList[0]*inputAry[i],returnList[1],returnList[2]]
    elif inputAry[i]<0:
        return [abs(returnList[0]*inputAry[i]),returnList[1]+1,returnList[2]]
    else:
        return [1,0,returnList[2]]

#resultTable = recMaxConsecutiveMul(1)
#print(resultTable)
from random import randint
inputAry= [-6,12,-7,14,-7,5]
#print(inputAry)
"""
def dpMaxConsecutiveMul():
    dp=[1,0,1,0,0,0]
    for i in range(len(inputAry)):
        if inputAry[i]<0:
            dp[1]+=1
        if dp[1]%2==0 and abs(dp[0]*inputAry[i])>dp[2]:
            if dp[5]!=0:
                dp[3]=dp[5]
            dp[2] = abs(dp[0]*inputAry[i])
            dp[0] = dp[2]
            dp[4] = i
        elif inputAry[i]!=0:
            dp[0] = abs(dp[0]*inputAry[i])
        else:
            dp = [1,0,dp[2],dp[3],dp[4],i+1]
    return dp
        
print(dpMaxConsecutiveMul())
"""
inputAry= [-2,8,-3,10,-3,-1]
def maxc():
    dp = [1,0,1]
    for i in range(len(inputAry)):
        if dp[1] >= 1 and inputAry[i] > 0:
            dp[1] *= inputAry[i]
        elif inputAry[i] < 0:
            dp[1]+=1
            continue

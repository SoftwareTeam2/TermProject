from itertools import combinations

n = int(input('동전의 갯수 : ')) # 동전의 갯수 입력 받기
money = list(map(int, input().split())) # 동전 당 가격 입력 받기
maxCoin = 0 # 만들 수 있는 가장 큰 동전의 값은?

# maxCoin 값 정하기
for coin in money: 
    maxCoin+=coin

# money를 이용하여 만들 수 있는 조합(부분집합)을 모두 구한다.
tempSet = []
for i in range(0,len(money)+1):
    c=combinations(money,i)
    tempSet.extend(c)

# 중복을 제거하여 각각 인덱스로 쓸 집합과 데이터를 추출할 집합 정의
subset=set(tempSet)
indexSet = set(tempSet)

# 입력 받은 동전으로 얻을 수 있는 합을 리스트에 저장한다.
sumList = []

# 부분 집합을 추출하여 그 안에 존재하는 원소의 합을 구한다.
for i in range(len(subset)):
    sum=0
    for num in indexSet.pop():
        sum+=num
    sumList.append(sum) # 구한 합을 sumList에 저장

# 1부터 maxCoin까지 순회하며 sumList에 값이 존재하는지 확인한다.
for i in range(1,maxCoin+1):
    if i not in sumList: # i 값이 sumList에 없으면 i를 출력하고 break
        print(i)
        break
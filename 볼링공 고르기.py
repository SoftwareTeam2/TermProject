from itertools import combinations

balls, maxWeight = map(int, input().split()) # 공의 갯수와 최대 무게 입력
weights = list(map(int, input().split())) # 각 공의 무게를 리스트에 저장

subset = [] # 공으로 만들 수 있는 조합을 저장할 변수

# 공으로 만들 수 있는 모든 조합을 계산
for i in range(0,len(weights)+1):
    c=combinations(weights,i)
    subset.extend(c)

answerSet = [] # 조건에 맞는 조합을 저장할 리스트

# 부분 집합의 원소의 갯수가 2이고 두 무게가 같지 않을 경우에만 리스트에 추가
for sets in subset:
    if len(sets)==2:
        if(sets[0] != sets[1]):
           answerSet.append(sets)
           
print(len(answerSet))

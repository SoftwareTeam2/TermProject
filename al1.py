from random import shuffle,randint

def findMin(ary): # 리스트 ary를 매개변수로 받는 함수
    if len(ary) == 1: # ary의 길이가 1이면
        return ary[0] # 가장 첫번째 원소를 리턴
    if ary[-1] >= ary[-2]: # 마지막 원소가 그 앞의 원소보다 크면
        return findMin(ary[:-1]) # 마지막 원소 전까지 리스트를 인자로 재귀호출
    else: # 마지막 원소가 그 앞의 원소보다 작은 경우
        ary[-1], ary[-2] = ary[-2], ary[-1] # 두 값을 바꿔주고
        return findMin(ary[:-1]) # 재귀호출

def arySum(ary,index): # 리스트 ary와 index를 매개변수로 받는 함수
    if index>=len(ary): # 인덱스가 ary의 길이 이상이 되면 
        return 0 # 0 리턴
    return ary[index]+arySum(ary,index+1) # ary[index] 와 ary[index+1]의 합을 재귀적으로 리턴

def selectionSort(ary):
    for i in range(len(ary)):
        for j in range(i,len(ary)):
            if ary[i] > ary[j]:
                minVal=ary[j]
                index = j
        ary[i],ary[index] = minVal, ary[i]
    return ary

def recursionSelect(ary,index): # 재귀적으로 정의된 SelectionSort
    if index >= len(ary): # base case : 현재 index가 리스트의 크기보다
        return  # 클 경우 재귀 종료
    minVal = findMin(ary[index:]) # findMin 함수를 통해 index 이후부터 최솟값 탐색
    minIndex = ary.index(minVal) # 최솟값의 인덱스 확인
    ary[index], ary[minIndex] = minVal, ary[index] # 값 스왑
    return recursionSelect(ary,index+1) # index+1을 인자로 재귀 호출
    
def flipPancake(pancakes):
    start = 0
    index = 0
    flipcount = 0
    """for j in range(len(pancakes)-1):
        if pancakes[j+1]>=pancakes[j]:
            pancakes[start:j+1] = reversed(pancakes[start:j+1])
            start = j
            """
    while index <= len(pancakes)-2:
        if pancakes[index+1] >= pancakes[index]:
            pancakes[start:index+1] = reversed(pancakes[start:index+1])
            start = index
            flipcount+=1
        index+=1
        

ary = [3]
print(arySum(ary,0))
pan = [5,3,2,1,4,9,7,6,8]
#flipPancake(pan)
#print(pan)
#shuffle(ary)
#print(ary)
#print(findMin(ary))
#findMin(ary)
#print(selectionSort(ary))
#recursionSelect(ary,0)
#print(ary)



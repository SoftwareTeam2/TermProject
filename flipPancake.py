pan = [2,1,3]

# 알고리즘의 전체적인 동작 방식
# 1. 우리가 볼 배열의 구간(처음부터 maximum까지) 중 최댓값 탐색
# 2. 최댓값이 맨앞에 오도록 배열의 처음~최댓값까지 리스트를 뒤집음
# 3. 이후 최댓값이 가장 밑에 올 수 있도록 배열의 구간(처음부터 maximum까지)를 뒤집음
# 4. 리스트는 구간에서 최댓값이 가장 뒤에 오게 되므로 maximum을 1감소 시키고 재귀호출
# 5. maximum이 1 == 탐색할 리스트의 길이가 1이면 종료

def flipPancake(ary,maximum): 
    if maximum == 1: # maximum이 1이면
        return # 종료
    maxIndex = ary.index(max(ary[:maximum])) # 처음부터 maximum까지 중 최댓값의 인덱스 탐색
    if maxIndex != 0: # 최댓값의 인덱스가 0이 아니면
        ary[:maxIndex+1] = reversed(ary[:maxIndex+1]) # 최댓값이 맨앞에 오도록 리스트를 뒤집음
        ary[:maximum] = reversed(ary[:maximum]) # 보고 있는 구간의 리스트를 통째로 뒤집음
        return flipPancake(ary,maximum-1) # maximum을 1 감소 시키고 재귀호출
    else: # 최댓값의 인덱스가 0이면 == 이미 최댓값이 맨앞임
        ary[:maximum] = reversed(ary[:maximum]) # 리스트를 통째로 뒤집기
        return flipPancake(ary,maximum-1) # maximum을 1 감소 시키고 재귀호출

flipPancake(pan,len(pan))
print(pan)



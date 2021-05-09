adventurer = int(input('모험가의 명수 : ')) # 사용자로부터 입력을 받음
if(adventurer!=0): # 명수가 0이 아니라면 if문 실행
    terrified = list(map(int, input('각 캐릭터의 공포도 : ').split())) # 사용자로부터 각 캐릭터의 공포도를 입력받음
    if(len(terrified)>adventurer): # 입력한 명수와 공포도 갯수 비교
        print('입력한 명수랑 안맞는데,,?') # 에러 출력
    else: # 맞으면 일로 와라
        terrified.sort(reverse=True) # 입력받은 공포도를 걲꾸로 정렬
        count = 0 # 그룹핑 갯수
        isGroupable = True # 그룹핑이 가능한가?
        while isGroupable: # 그룹핑이 가능하면 while
            if(len(terrified) == 0): # 남은 인원이 0인가?
                break  # 그러면 그만하자
            if terrified[0] <= len(terrified): # 제일 공포도가 큰 애랑 남은 인원이랑 그룹핑이 되나?
                for i in range(terrified[0]): # 제일 높은 공포도만큼 애들 데리고 나가자
                    terrified.pop(0) # 자 드가자~
                count += 1 # 그룹의 갯수 늘리기
            else: # 사람은 남았는데 공포도가 남아 있는 애들 명수보다 크네
                isGroupable = False # while 돌지마!
        print(count) # 결과 출력
else: # 명수가 0이면 0 출력
    print(0)

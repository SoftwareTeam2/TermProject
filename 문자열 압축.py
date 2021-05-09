def solution(s):
    if len(s) == 1:
        return 1
    if len(s) == 3:
        if list(s) == [s[0]] * 3:
            return 2
        else:
            return 3
    minAns = len(s)
    for i in range(len(s)//2,0,-1):
        answer = len(s)
        count=0
        for j in range(i,len(s),i):
            if s[j-i:j] == s[j:j+i]:
                count+=1
                if i!=1 and count==1:
                    answer-=i-1
                elif i!=1 and count>1:
                    answer-=i
                if count>=2 and i==1:
                    answer-=1
            else:
                answer+=len(str(count+1))-1
                count=0
        answer+=len(str(count+1))-1
        if minAns > answer:
            minAns = answer
    return minAns
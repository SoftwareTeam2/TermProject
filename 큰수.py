n, m, k = map(int, input().split())
numList = list(map(int, input().split()))

isValid = True
sum = 0
count = 0

if len(numList)>n:
    print('숫자 넘 많음')
else:
    numList.sort(reverse=True)

    while isValid:
        for i in range(k):
            sum+=numList[0]
            count+=1
            if(count>=m):
                isValid=False   
                break
        if(numList[0]==numList[1]):
            for i in range(k):
                sum+=numList[1]
                count+=1
                if(count>=m):
                    isValid=False
                    break
        else:
            sum+=numList[1]
            count+=1
            if(count>=m):
                isValid=False
                break
    print(sum)
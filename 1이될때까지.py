num,k = map(int, input().split())
count=0
while num!=1:
    if(num%k==0):
        num/=k
        count+=1
    else:
        num-=1
        count+=1

print(count)
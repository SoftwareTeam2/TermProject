s_num = input('숫자를 입력 : ') 
sum=1 
for num in s_num:
    if(num!='0' and num!='1'):
        sum*=int(num)
    else:
        sum+=int(num)
print(sum)
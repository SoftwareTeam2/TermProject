import sys
input=sys.stdin.readline

s_num = input()
s_list = list(s_num[:-1])
sum=0
for i in range(1,len(s_list)):
    if s_list[0]=='0' and i == 1:
        sum+=int(s_list[i])
    elif s_list[i]=='0' or s_list[i]=='1':
        sum+=int(s_list[i])
    else:
        sum*=int(s_list[i])
print(sum)

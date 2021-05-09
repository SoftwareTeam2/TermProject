import sys
input = sys.stdin.readline

s_list = input()

ones = 0
zeros = 0

o_flag = False
z_flag = False

if s_list[0]=='0':
    z_flag=True
else:
    o_flag=True

for ch in s_list:
    if ch=='0' and o_flag == True:
        ones+=1
        o_flag=False
        z_flag=True
    elif ch=='1' and z_flag == True:
        zeros+=1
        o_flag=True
        z_flag=False
if s_list[len(s_list)-1] == '0':
    zeros+=1
else:
    ones+=1

print(min(zeros,ones))
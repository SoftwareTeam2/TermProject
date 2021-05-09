u_input = input('문자 입력 : ')
o_unit = 0 # 연속해서 이어지는 0들을 한 단위로 저장할 변수
z_unit = 0 # 연속해서 이어지는 1들을 한 단위로 저장할 변수
index=0 # 문자열 탐색 변수

# 문자열을 끝까지 읽으면서 0의 묶음과 1의 묶음의 갯수를 계산한다.
while index<=len(u_input)-1:
    if u_input[index]=='0':
        while u_input[index]!='1' and index<=len(u_input)-1:
            index+=1
            if index==len(u_input):
                break
        z_unit+=1
    elif u_input[index]=='1':
        while u_input[index]!='0' and index<=len(u_input)-1:
            index+=1
            if index==len(u_input):
                break
        o_unit+=1

count = 0 # 뒤집는 횟수를 저장할 변수
index=0

# 0의 묶음의 수가 1의 묶음의 수보다 작을 때
if z_unit<o_unit:
    while index<len(u_input)-1:
        if u_input[index]=='0':
            while u_input[index]!='1' and index<=len(u_input)-1:
                index+=1
            count+=1
        else:
            index+=1
# 1의 묶음의 수가 0의 묶음의 수보다 작을 때
elif z_unit>o_unit:
    while index<len(u_input)-1:
        if u_input[index]=='1':
            while u_input[index]!='0' and index<=len(u_input)-1:
                index+=1
            count+=1
        else:
            index+=1
# 두 묶음의 수가 같을 때
else:
    while index<len(u_input)-1:
        if u_input[index]=='1':
            while u_input[index]!='0' and index<=len(u_input)-1:
                index+=1
            count+=1
        else:
            index+=1
print(count)
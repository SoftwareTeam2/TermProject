import sys
input = sys.stdin.readline

u_input = input()
s_list =[]
n_sum=0
for i in range(len(u_input)-1):
    if ord(u_input[i]) >= 65 and ord(u_input[i]) <= 90:
        s_list.append(u_input[i])
    else:
        n_sum+=int(u_input[i])
s_list.sort()
s_list.append(str(n_sum))
print(''.join(s_list))
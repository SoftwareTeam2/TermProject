n = int(input())
s_list=[]
for i in range(n):
    s_list.append(list(map(str,input().split())))
s_list.sort(key=lambda x:x[1])
for name in s_list:
    print(name[0],end=' ')
import sys
input = sys.stdin.readline

rating = int(input())
rating = str(rating)
r_sum = 0
l_sum = 0
for i in range(len(rating)//2):
    r_sum+=int(rating[i])
for i in range(len(rating)//2,len(rating)):
    l_sum+=int(rating[i])
if r_sum == l_sum:
    print('LUCKY')
else:
    print('READY')
from numpy import array

moves = array([[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[-1,-2],[1,-2]])
which = input('나이트의 위치 : ')
loc = array([ord(which[:1])-96, int(which[1:])])
count = 0

for move in moves:
    locT = loc+move
    if not(locT[0] <= 0 or locT[0] > 8 or locT[1] <=0 or locT[1] > 8) :
        count+=1

print(count)
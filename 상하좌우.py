from numpy import array
squareMap = array([1,1])
num = int(input('정사각형 크기 : '))
move = list(map(str, input().split()))
dic = {'r':array([0,1]),'l':array([0,-1]),'u':array([-1,0]),'d':array([1,0])}
for order in move:
    squareMap+=dic.get(order)
    if(squareMap[0]==0 or squareMap[0]==num+1 or squareMap[1]==0 or squareMap[1]==num+1):
        squareMap-=dic.get(order)
print(squareMap[0],squareMap[1])
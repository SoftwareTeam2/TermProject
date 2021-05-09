def hanoi(n,src,dst,tmp):
    if n>0:
        hanoi(n-1,src,tmp,dst)
        print(n,'번째 원판을 ',dst,'번 막대로 이동')
        hanoi(n-1,tmp,dst,src)
hanoi(3,1,3,2)
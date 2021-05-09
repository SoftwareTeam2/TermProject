import sys
from random import randint
def csum(a,k):
    if len(a)==1:
        return (a[0],k,k)
    mid = len(a)//2
    m1 = csum(a[:mid],k)
    m2 = csum(a[mid:],k+mid)
    sumval = sum(a[m1[1]-k:m2[2]+1-k])
    if m1[0] > m2[0] and m1[0] >= sumval:
        return (m1[0],m1[1],m1[2])
    elif m2[0]>m1[0] and m2[0]>=sumval:
        return (m2[0],m2[1],m2[2])
    elif sumval>m1[0] and sumval>m2[0]:
        return (sumval,m1[1],m2[2])

ex = [randint(-100,100) for _ in range(10)]
print(ex)
print(csum(ex,0))
print(sum(ex))
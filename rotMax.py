def aryRot(ary,k):
    if ary[0] < ary[-1]:
        return (ary[-1],len(ary)-1)
    if len(ary) == 1:
        return (ary[0],k)
    if len(ary) == 2:
        return (ary[0],k) if ary[0]>ary[1] else (ary[1],k+1)
    m = len(ary)//2

    if ary[:m+1][0] < ary[:m+1][-1]:
        m1 = (ary[:m+1][-1],m)
        m2 = aryRot(ary[m+1:],m+k+1)
    else:
        m2 = (ary[m+1:][-1],2*m-1) if len(ary)%2==0 else (ary[m+1:][-1],2*m)
        m1 = aryRot(ary[:m+1],k)
    return max(m1,m2)

print(aryRot([5,8,9,2,3,4],0))
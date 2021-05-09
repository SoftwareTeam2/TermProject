def subsetSum(a,i,t):
    if t==0:
        return True
    if t<0 or i>=len(a):
        return False
    else:
        notInclude = subsetSum(a,i+1,t)
        include = subsetSum(a,i+1,t-a[i])
        return notInclude or include
a = [i for i in range(1,10)]
print(subsetSum(a,0,5))


def coksecutiveSum(inputarray,k):
    if len(inputarray) == 1:
        return (inputarray[0],k,k)
    mid = len(inputarray)//2
    m1 = coksecutiveSum(inputarray[:mid],k)
    m2 = coksecutiveSum(inputarray[mid:],k+mid)
    sumValue = sum(inputarray[m1[1]-k:m2[2]+1-k])
    if m1[0]> m2[0] and m1[0]>=sumValue:
        return (m1[0],m1[1],m1[2])
    elif m2[0]>m1[0] and m2[0]>=sumValue:
        return (m2[0],m2[1],m2[2])
    elif sumValue > m1[0] and sumValue > m2[0]:
        return (sumValue,m1[1],m2[2])
print(coksecutiveSum([3, -7, 5, 8, 73, -57, 26, 43, 11, 8],0))
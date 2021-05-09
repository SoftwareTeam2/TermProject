from random import randint
def lis(last,i,length):
    if i >= len(a):
        return length
    if a[i] > last:
        l1 = lis(a[i],i+1,length+1)
        l2 = lis(last,i+1,length)
        return max(l1,l2)
    else:
        return lis(last,i+1,length)

def lisFirst(i):
    best = 0
    for j in range(i+1,len(a)):
        if a[j] > a[i]:
            best = max(best,lisFirst(j))
    return best+1

for _ in range(100):
    a=[randint(1,20) for _ in range(5)]
    a.insert(0,int(10**-6))
    if lis(0,0,0)+1 != lisFirst(0):
        print('not same')
        break
print('same')
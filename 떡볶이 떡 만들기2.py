import sys
input = sys.stdin.readline

n, m = map(int,input().split())
rice = list(map(int,input().split()))
d_list=[]

def bisearch(start, end):
    sum = 0
    mid = (start+end)//2
    if start > end : 
        return
    for ri in rice:
        if ri>mid:
            sum+=ri-mid
    if sum > m :
        d_list.append(mid)
        return bisearch(mid+1,end)
    elif sum < m :
        return bisearch(start, mid-1)
    else:
        d_list.clear()
        d_list.append(mid)
        return

rice.sort()
bisearch(0,max(rice))
d_list.sort(reverse=True)
print(d_list[0])
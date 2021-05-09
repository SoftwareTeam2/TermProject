n, m = map(int,input().split())
ddeok = list(map(int,input().split()))
lastTake=0

def binarysearch(start, end):
    global lastTake
    takeIt = 0
    mid = (start+end)//2
    for length in ddeok:
        if length>mid:
            takeIt+=length-mid
    if start>=end:
        return lastTake
    if takeIt<m:
        return binarysearch(start,mid-1)
    elif takeIt>m:
        lastTake=mid
        return binarysearch(mid+1,end)
    else:
        return mid

start = 0
end = max(ddeok)

print(binarysearch(start,end))
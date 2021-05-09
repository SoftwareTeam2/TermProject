import sys
input = sys.stdin.readline

n = int(input())
component = list(map(int,input().split()))
m = int(input())
order=[]
order = list(map(int,input().split()))
component.sort()

def bisearch(start, end, target):
    if start > end:
        return False
    mid = (start+end)//2
    if component[mid] < target:
        return bisearch(mid+1, end, target)
    elif component[mid] > target:
        return bisearch(start,mid-1,target)
    else:
        return True

for demand in order:
    if bisearch(0,len(component)-1,demand):
        print('yes')
    else:
        print('no')

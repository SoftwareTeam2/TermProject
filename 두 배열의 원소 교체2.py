n, k = map(int,input().split())
first = list(map(int,input().split()))
second = list(map(int,input().split()))
first.sort()
second.sort(reverse=True)
for i in range(k):
    if first[i]<second[i]:
        first[i]=second[i]
print(sum(first))
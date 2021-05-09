n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
result = 0
index = 0
while index<m:
    for i in range(k):
        if index+1<=m:
            result += nums[0]
            index += 1
    if nums[0] > nums[1]:
        if index+1<=m:
            result += nums[1]
            index += 1
print(result)
nums = []
for i in range(10):
    nums.append(int(input()))
remainders = []
for i in range(10):
    remainders.append(nums[i]%42)
print(len(set(remainders)))

def flip(arr, k):
  left = 0
  while left < k:
    arr[left], arr[k] = arr[k], arr[left]
    k -= 1
    left += 1

def max_index(arr, k):
  index = 0
  for i in range(k):
    if arr[i] > arr[index]:
      index = i
  return index

def pancake_sort(arr):
  n = len(arr)
  while n > 1:
    maxdex = max_index(arr, n)
    if maxdex != n:
      flip(arr, maxdex)
      flip(arr, n - 1)
    n -= 1

ary = [1,3,2]
pancake_sort(ary)
print(ary)
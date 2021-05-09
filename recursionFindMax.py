def findMax(array):
    if len(array) == 1:
        return array[0]
    m1 = findMax(array[:len(array)//2])
    m2 = findMax(array[len(array)//2+1:])
    return max(m1,m2)
print(findMax([1,3,5,2,5,6,9]))
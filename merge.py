def merge(A,m):
    i = 1
    j = m+1
    B = [0 for _ in range(len(A))]
    for k in range(1,len(A)):
        if j>len(A):
            B[k] = A[i]
            i+=1
        elif i>m:
            B[k]=A[j]
            j+=1
        elif A[i] < A[j]:
            B[k] = A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1
    for k in range(1,len(A)):
        A[k] = B[k]

def mergeSort(A):
    if len(A)>1:
        m = len(A)//2
        mergeSort(A[1:m])
        mergeSort(A[m+1:len(A)])
        merge(A,m)
array = [1,6,8,3,7,2,9,10,5,4]
mergeSort(array)
print(array)
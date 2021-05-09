import sys
import numpy as np
input = sys.stdin.readline

def solution(key, lock):
    key = np.array(key)
    extendedLock = np.zeros((len(lock)**2,len(lock)**2),dtype='int32')
    extendedLock[len(lock):2*len(lock),len(lock):2*len(lock)] = extendedLock[len(lock):2*len(lock),len(lock):2*len(lock)]+np.array(lock)
    found = False
    for i in range(4):
        for j in range(len(extendedLock)):
            for k in range(len(extendedLock)):
                if np.shape(extendedLock[j:j+len(key),k:k+len(key)]) == np.shape(key):         
                    extendedLock[j:j+len(key),k:k+len(key)] += key
                    if np.all(extendedLock[len(lock):2*len(lock),len(lock):2*len(lock)]==1) :
                        found = True
                    else:
                        extendedLock[j:j+len(key),k:k+len(key)] -= key
            if found:
                break
        if found:
            break
        else:
            key = np.rot90(key,i+1)
    return found
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
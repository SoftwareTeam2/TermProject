import sys, copy
input = sys.stdin.readline

n = int(input())
adventurer = list(map(int,input().split()))
adventurer.sort(reverse=True)
nominate = copy.deepcopy(adventurer)

isValid = True
party = 0

while isValid:
    for i in range(adventurer[0]):
        if nominate:
            nominate.pop(0)
        else:
            isValid=False
            break
    if isValid:
        party+=1
    if nominate:
        adventurer[0]=nominate[0]

print(party)

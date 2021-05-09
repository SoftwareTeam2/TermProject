def parenthesis(inputString):
    pDict = {'(':0,'{':0,'[':0,')':0,'}':0,']':0}
    pStack = []
    index = 0
    for ch in inputString:
        if ch in '({[':
            index+=1
            pDict[ch] = pDict.get(ch)+1
            pStack.append(index)
            print(index,end='')
        else:
                pDict[ch] = pDict.get(ch)-1
                if pDict.get(ch) < 0:
                    return 0
                print(pStack.pop(),end='')
    if pStack:
        return 0
    else:
        return 1
print(parenthesis('(){}[()]'))
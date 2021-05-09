def placeQueens(q,r):
    if r==len(q):
        print(q)
        return
    else:
        for j in range(len(q)):
            legal = True
            for i in range(r):
                if q[i]==j or q[i]==j+r-i or q[i]==j-r+i:
                    legal=False
            if legal:
                q[r]=j
                placeQueens(q,r+1)

placeQueens([0,0,0,0,0,0,0,0],0)
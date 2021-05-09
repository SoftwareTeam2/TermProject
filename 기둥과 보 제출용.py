def solution(n, build_frame):
    wall = [[0 for _ in range(n+1)] for _ in range(n+1)]
    finalWork = []
    for command in build_frame:
        x, y, sturcture, wizard = command
        if wizard == 1:
            if sturcture == 0:
                if y == 0 or wall[n-y][x] >= 1:
                    wall[n-y][x] = max(wall[n-y][x], 1)
                    wall[n-y-1][x] = max(wall[n-y-1][x], 1)
                    finalWork.append([x, y, sturcture])
            else:
                print((wall[n-y][x], wall[n-y+1][x],wall[n-y][x+1], wall[n-y+1][x+1],wall[n-y][x-1],wall[n-y][x+1]))
                if (wall[n-y][x] >= 1 and wall[n-y+1][x] >=1) or (wall[n-y][x+1] >= 1 and wall[n-y+1][x+1] >=1) or (wall[n-y][x-1] == 2 and wall[n-y][x+1] == 2): 
                    wall[n-y][x] = max(wall[n-y-1][x], 2)
                    wall[n-y][x+1] = max(wall[n-y-1][x], 2)
                    finalWork.append([x, y, sturcture])
        else:
            if sturcture == 0:
                temp1, temp2 = wall[n-y][x],wall[n-y-1][x]
                wall[n-y][x] = 0
                if wall[n-y-1][x]==2:
                    wall[n-y-1][x] = 1
                else:
                    wall[n-y-1][x] = 0
                if (wall[n-y-1][x-1] == 2 and wall[n-y-1][x+1] == 2 and wall[n-y-1][x] < 1) or (wall[n-y-1][x]==0 and wall[n-y-1][x+1]==2) or (wall[n-y-1][x]==0 and wall[n-y-1][x-1]==2):
                    wall[n-y][x] = temp1
                    wall[n-y-1][x] = temp2
                else:  
                    if [x,y,sturcture] in finalWork:
                        finalWork.remove([x, y, sturcture])               
            else:
                temp1, temp2 = wall[n-y][x],wall[n-y][x+1]
                wall[n-y][x] == 0
                wall[n-y][x+1] == 0
                if wall[n-y+1][x]>=1:
                    wall[n-y][x] = 1
                else:
                    wall[n-y-1][x] = 0
                if (wall[n-y][x-1]==2 and wall[n-y][x+2]==2) and (wall[n-y+1][x-1]<1 and wall[n-y+1][x]<1):
                    wall[n-y][x] == temp1
                    wall[n-y][x+1] == temp2
                else:
                    if [x,y,sturcture] in finalWork:
                        finalWork.remove([x, y, sturcture])       
    finalWork.sort()
    return finalWork

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
 
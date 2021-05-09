from numpy import array
def chessKnight(position):
    xPos = ord(position[0])-97
    yPos = int(position[1])-1
    position=array([xPos,yPos])
    moves = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    moves = array(moves)
    count=0
    for move in moves:
        print(position+move)
        if position[0]+move[0]>=0 and position[0]+move[0]<8 and position[1]+move[1]>=0 and position[1]+move[1]<8:
            count+=1
    print(count)
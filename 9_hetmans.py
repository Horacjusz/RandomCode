N = 4
board = [[0 for _ in range(N)] for _ in range(N)]

def printboard(board) :
    for _ in board :
        print(_)
    print()
        
printboard(board)

#jeśli sprawdzamy czy hetman bije
#   
#def is_free(board,x,y) :
#    global N
#    direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
#    
#    for d in direction :
#        print("Direction:",d)
#        for i in range(N) :
#            xi = x + (i*d[0])
#            yi = y + (i*d[1])
#            if xi < 0 or xi >= N or yi < 0 or yi >= N :
#                break
#            if (xi == x and yi == y) :
#                continue
#            if board[xi][yi] != 0 :
#                return False
#    return True

def place(board,x,y) :
    global N
    direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
    for d in direction :
        for i in range(N) :
            xi = x + (i*d[0])
            yi = y + (i*d[1])
            if xi < 0 or xi >= N or yi < 0 or yi >= N :
                break
            if (xi == x and yi == y) :
                continue
            board[xi][yi] = 1
    board[x][y] = 8
    return board


def hetmans(board) :
    global N
    def seek(T,placed = 0,a=0,b=0) :
        global N
        T = place(T,a,b)
        placed += 1
        print()
        print(placed,a,b)
        printboard(T)
        if placed == N :
            return
        for x in range(N) :
            for y in range(N) :
                print(x,y)
                if T[x][y] != 0 :
                    continue
                seek(T,placed,x,y)
    seek(board)
    printboard(board)
                
hetmans(board)
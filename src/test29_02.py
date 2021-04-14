from collections import deque
import sys

def s_bfs():    
    s_next = []
    while s_queue:
        x,y = s_queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] == '.':
                    board[nx][ny] = 'S'
                    s_next.append([nx,ny])
                if board[nx][ny] == 'D':
                    return True
    return s_next                    

def w_bfs():    
    w_next = []
    while w_queue:
        x,y = w_queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] == '.' or board[nx][ny] == 'S':
                    board[nx][ny] = '*'
                    w_next.append([nx,ny])
    return w_next                    


dx = [-1,1,0,0]
dy = [0,0,-1,1]

R,C = map(int,sys.stdin.readline().rstrip().split())
board = []
water = []
start = []
for i in range(R):
    board.append(list(sys.stdin.readline().rstrip()))
    for j in range(C):
        if board[i][j] == '*':
            water.append([i,j])
        if board[i][j] == 'S':
            start.append([i,j])

time = 0
while True:     
    time += 1
    s_queue = deque()       
    for s_x,s_y in start:
        s_queue.append([s_x,s_y])
    result = s_bfs()        

    if result == True:
        print(time)
        break
    if result == []:
        print("KAKTUS")
        break

    w_queue = deque()       
    for w_x,w_y in water:
        w_queue.append([w_x,w_y])
    water = w_bfs()                

    tmp_s = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':
                tmp_s.append([i,j])
    start = tmp_s                


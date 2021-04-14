from collections import deque
import sys

def bfs(start):
    q = deque()
    q.extend(start)
    next_q = []

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<R and 0<=ny<C:
                if board[x][y] == 'S' and board[nx][ny] == '.':
                    board[nx][ny] = 'S'
                    next_q.append([nx,ny])
                if board[x][y] == '*' and (board[nx][ny] == '.' or board[nx][ny] == 'S'):
                    board[nx][ny] = '*'
                    next_q.append([nx,ny]) 
                if board[x][y] == 'S' and board[nx][ny] == 'D':
                    return True
    return next_q                                       

R,C = map(int,sys.stdin.readline().rstrip().split())
board = []
water = []
for i in range(R):
    board.append(list(sys.stdin.readline().rstrip()))    
    for j in range(C):
        if board[i][j] == 'D':
            b_x,b_y = i,j
        if board[i][j] == 'S':
            start = [[i,j]]
        if board[i][j] == '*':
            water.append([i,j])
        
dx = [-1,0,1,0]
dy = [0,1,0,-1]

time = 0
while True:
    time += 1
    s_list = bfs(start)
    water = bfs(water)     
    if s_list == True:
        print(time)
        break
    if s_list == []:
        print("KAKTUS")
        break

    new_s = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':
                new_s.append([i,j])
    start = new_s

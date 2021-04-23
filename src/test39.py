from collections import deque
import sys

def s_move():
    flag = False
    while s_q:
        x,y = s_q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] == 'D':
                    return True
                if board[nx][ny] == '.':
                    board[nx][ny] = 'S'
                    flag = True
    if flag == False:
        return False
    return None

def w_move():
    while w_q:
        x,y = w_q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] == '.' or board[nx][ny] == 'S':
                    board[nx][ny] = '*'
                    w_list.append([nx,ny])

R,C = map(int,sys.stdin.readline().rstrip().split())
board = []
s_list = []
w_list = []
for i in range(R):
    board.append(list(sys.stdin.readline().rstrip()))
    for j in range(C):
        if board[i][j] == 'S':
            s_list.append([i,j])
        if board[i][j] == '*':
            w_list.append([i,j])   

dx = [-1,1,0,0]
dy = [0,0,-1,1]            
time = 0
while True:           
    time += 1
    s_q = deque()
    for s_x,s_y in s_list:
        s_q.append([s_x,s_y])
    result = s_move()
    if result == True:
        print(time)
        break
    if result == False:
        print("KAKTUS")
        break
    w_q = deque()
    for w_x,w_y in w_list:
        w_q.append([w_x,w_y])
    w_move()        

    s_list = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':
                s_list.append([i,j])
               

from collections import deque
import sys

def check():
    tmp = []
    dist = [[-1]*N for _ in range(N)]
    dist[s_x][s_y] = 0
    q = deque()
    q.append([s_x,s_y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] == -1 and board[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
                if 1 <= board[nx][ny] < size and dist[nx][ny] != -1:
                    tmp.append([dist[nx][ny],nx,ny])                            

    tmp.sort(key=lambda x:(x[0],x[1],x[2]))  
    return tmp


N = int(sys.stdin.readline().rstrip())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if board[i][j] == 9:
            s_x,s_y = i,j
            board[i][j] = 0

size = 2
dx = [-1,1,0,0]
dy = [0,0,-1,1]

time = 0
ate = 0
while True:
    result = check()
    if result == []:
        print(time)
        break
    
    dist,x,y = result[0]
    time += dist
    board[x][y] = 0
    s_x,s_y = x,y
    ate += 1

    if ate >= size:
        ate = 0 
        size += 1


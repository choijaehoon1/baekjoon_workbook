from collections import deque
import copy
import sys

def bfs(x,y):
    visit[x][y] = 1
    board[x][y] = -1
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny] == 0 and board[nx][ny] == 0:
                    visit[nx][ny] = 1
                    board[nx][ny] = -1
                    q.append([nx,ny])


def check(x,y):
    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == -1:
                cnt += 1
    if cnt >= 2:
        return True
    return False        

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,sys.stdin.readline().rstrip().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

time = 0
while True:
    tmp = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                tmp += 1
    if tmp == N*M:
        print(time)
        break             

    visit = [[0]*M for _ in range(N)]
    bfs(0,0)
    
    check_list = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                if check(i,j):
                    check_list.append([i,j])
    
    for cx,cy in check_list:
        board[cx][cy] = 0
    
    new_board = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                new_board[i][j] = board[i][j]
    board = copy.deepcopy(new_board)
    time += 1


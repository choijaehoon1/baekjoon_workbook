import copy
from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny] == 0 and new_board[nx][ny] != -1:
                    visit[nx][ny] = 1
                    new_board[nx][ny] = -1
                    q.append([nx,ny])


dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(sys.stdin.readline().rstrip())
board = []
max_height = 0
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if max_height < board[i][j]:
            max_height = board[i][j]

answer = 1
for h in range(1,max_height+1):
    visit = [[0]*N for _ in range(N)]
    new_board = copy.deepcopy(board)

    for i in range(N):
        for j in range(N):
            if new_board[i][j] <= h:
                new_board[i][j] = -1
                
    cnt = 0
    for i in range(N):
        for j in range(N):
            if new_board[i][j] != -1 and visit[i][j] == 0:
                cnt += 1
                bfs(i,j)
    answer = max(answer,cnt)
print(answer)


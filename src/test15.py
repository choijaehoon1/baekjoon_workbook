from collections import deque
import copy
import sys

def bfs(x,y,color,visited,board):
    visited[x][y] = 1
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] == 0 and color == board[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(sys.stdin.readline().rstrip())
board = []
new_board = []
for i in range(N):
    board.append(list(input()))

new_board = copy.deepcopy(board)    
for i in range(N):
    for j in range(N):
        if new_board[i][j] == 'G':
            new_board[i][j] = 'R'

visit = [[0]*N for _ in range(N)]
s_visit = [[0]*N for _ in range(N)]
cnt01 = 0
cnt02 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            cnt01 += 1
            bfs(i,j,board[i][j],visit,board)
        if s_visit[i][j] == 0:
            cnt02 += 1
            bfs(i,j,new_board[i][j],s_visit,new_board)

print(cnt01, cnt02)

